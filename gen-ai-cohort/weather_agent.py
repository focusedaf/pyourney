import os
import json
import requests
import re
from google import genai
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()
os.environ.pop("SSL_CERT_FILE", None)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
model_id = "gemini-2.0-flash-001"

def get_weather(city: str):
    print("Tool Called: get_weather", city)
    url = f"https://wttr.in/{quote(city)}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text.strip()}"
    return "Something went wrong"

available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as input and returns the current weather for the city"
    }
}


system_prompt = """
You are a helpful AI assistant who is specialized in resolving user queries.
You work on start, plan, action, observe mode.
For the given user query and available tools, plan the step-by-step execution.
Based on the planning, select the relevant tool from the available tools,
and based on the tool selection you perform an action to call the tool.
Wait for the observation and based on the observation from the tool call, resolve the user query.

Rules: 
- Follow the Output JSON Format
- Always perform one step at a time
- Each query should follow a complete flow: plan → action → output
- DO NOT repeat planning steps
- DO NOT wrap your JSON responses in code blocks or any other formatting
- Once you receive an observation, move directly to the output step

Output JSON Format:
{
    "step":"string",
    "content":"string",
    "function":"The name of function if the step is action",
    "input":"The input parameter of the function"
}

Available Tools:
- get_weather : Takes a city name as an input and returns the current weather for the city

Example:
User Query: What is the weather of kalyan?
Output : {"step":"plan","content":"The user is interested in weather data of kalyan"}
Output : {"step":"action","function":"get_weather","input":"kalyan"}
Upon receiving: {"step":"observe","output":"The weather in kalyan is Sunny +31°C"}
Output : {"step":"output","content":"The weather for kalyan is Sunny +31°C"}
"""

def clean_json_output(raw_output):
    # Remove markdown code block syntax if present
    cleaned = re.sub(r'```(?:json)?\s*([\s\S]*?)\s*```', r'\1', raw_output)
    
    # Try to find JSON objects on separate lines
    json_lines = []
    for line in cleaned.split('\n'):
        line = line.strip()
        if line and (line.startswith('{') and line.endswith('}')):
            json_lines.append(line)
    
    if json_lines:
        return json_lines
    
    # If no individual lines look like JSON, try the whole string
    cleaned = cleaned.strip()
    if cleaned.startswith('{') and cleaned.endswith('}'):
        return [cleaned]
    
    # As a last resort, try to find any JSON-like structure
    matches = re.findall(r'(\{.*?\})', cleaned, re.DOTALL)
    if matches:
        return matches
    
    return []

while True:
    # Reset messages for each new user query
    messages = [{"role": "system", "content": system_prompt}]
    
    user_query = input("> ")
    messages.append({"role": "user", "content": user_query})
    
    # Track the current step in the process
    current_state = "planning"  # States: planning, executing, completed
    observation = None
    
    while current_state != "completed":
        # Combine chat history into one prompt text
        prompt_text = "\n".join([f"{m['role']}: {m['content']}" for m in messages])

        response = client.models.generate_content(
            model=model_id,
            contents=[{"role": "user", "parts": [{"text": prompt_text}]}]
        )

        try:
            raw_output = response.candidates[0].content.parts[0].text.strip()

            if not raw_output:
                print("⚠️ Empty model output.")
                break

            json_lines = clean_json_output(raw_output)
            
            if not json_lines:
                print("⚠️ No valid JSON found in response.")
                print("🔍 Raw Output:", raw_output)
                break

            # Process each JSON object found
            for json_str in json_lines:
                try:
                    parsed_output = json.loads(json_str)
                    step_type = parsed_output.get("step")

                    if step_type == "plan" and current_state == "planning":
                        print(f'🧠: {parsed_output.get("content")}')
                    
                    elif step_type == "action" and current_state == "planning":
                        tool_name = parsed_output.get("function")
                        tool_input = parsed_output.get("input")

                        if available_tools.get(tool_name):
                            current_state = "executing"
                            output = available_tools[tool_name]["fn"](tool_input)
                            observation = {"step": "observe", "output": output}
                            messages.append({"role": "assistant", "content": json.dumps(observation)})
                            break 
                    
                    elif step_type == "output":
                        print(f'🤖: {parsed_output.get("content")}')
                        current_state = "completed"
                        break
                        
                except json.JSONDecodeError:
                    continue  # Skip invalid JSON
                
            # If we're in executing state and haven't completed yet, we need to ensure the model gets a chance to respond to the observation
            if current_state == "executing" and observation:
                current_state = "planning"  
                observation = None  
                    
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            print("🔍 Raw Output:", raw_output)
            break