import os
from google import genai
from dotenv import load_dotenv
from colorama import init, Fore, Style
import time

init()
load_dotenv()
os.environ.pop("SSL_CERT_FILE", None)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

persona = """
You are a helpful, smart financial assistant named C4. You guide users to make better investment decisions.

When a user asks you something, you should think through it step by step:
1. First understand what they're asking (planning)
2. Decide what approach to take (action) 
3. Analyze the current situation (observation)
4. Draw insights (conclusion)
5. Ask a relevant follow-up question

Be conversational, knowledgeable, and helpful like a smart friend who knows about investing.
"""

def get_planning(user_query, conversation_context):
    prompt = f"""
    Based on this user query: "{user_query}"
    
    What is your PLANNING for how to approach this? Think about what the user is really asking and what information you need to help them effectively.
    
    Respond with just your planning thoughts in 1-2 sentences.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[persona] + conversation_context + [prompt]
    )
    return response.text.strip()

def get_action(user_query, planning, conversation_context):
    prompt = f"""
    User query: "{user_query}"
    Your planning: "{planning}"
    
    What ACTION will you take to help the user? What specific approach or method will you use?
    
    Respond with just your action plan in 1-2 sentences.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[persona] + conversation_context + [prompt]
    )
    return response.text.strip()

def get_observation(user_query, planning, action, conversation_context):
    prompt = f"""
    User query: "{user_query}"
    Your planning: "{planning}"
    Your action: "{action}"
    
    What do you OBSERVE about the current situation? What relevant information or context should be considered?
    
    Respond with your observations in 1-2 sentences.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[persona] + conversation_context + [prompt]
    )
    return response.text.strip()

def get_conclusion(user_query, planning, action, observation, conversation_context):
    prompt = f"""
    User query: "{user_query}"
    Your planning: "{planning}"
    Your action: "{action}"
    Your observation: "{observation}"
    
    What is your CONCLUSION? What insights or advice can you provide based on your analysis?
    
    Respond with your conclusion and main advice.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[persona] + conversation_context + [prompt]
    )
    return response.text.replace("**", "").strip()


def get_follow_up(user_query, planning, action, observation, conclusion, conversation_context):
    prompt = f"""
    User query: "{user_query}"
    Your planning: "{planning}"
    Your action: "{action}"
    Your observation: "{observation}"
    Your conclusion: "{conclusion}"
    
    What FOLLOW-UP QUESTION should you ask to help the user further or gather more information they need?
    
    Respond with just the follow-up question.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[persona] + conversation_context + [prompt]
    )
    return response.text.strip()


conversation = []

print(f"{Fore.GREEN}{'='*60}")
print(f"C4 - YOUR AI INVESTMENT BUDDY WELCOMES YOU!")
print(f"{'='*60}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Ask me anything about investing and watch me think it through step by step!{Style.RESET_ALL}\n")


while True:
    try:
        user_input = input(f"{Fore.CYAN}You: {Style.RESET_ALL}")
        if user_input.lower() in ["exit", "quit", "bye", "stop"]:
            print(f"{Fore.YELLOW}\nCatch you later, investor buddy! Keep those gains coming!{Style.RESET_ALL}")
            break
        
        print(f"\n{Fore.GREEN}C4 is thinking...{Style.RESET_ALL}")
        print("-" * 50)
        
       
        print(f"{Fore.BLUE}PLANNING...{Style.RESET_ALL}")
        planning = get_planning(user_input, conversation)
        print(f"   {planning}")
        time.sleep(0.5)
        
       
        print(f"\n{Fore.YELLOW}ACTION...{Style.RESET_ALL}")
        action = get_action(user_input, planning, conversation)
        print(f"   {action}")
        time.sleep(0.5)
        
        
        print(f"\n{Fore.MAGENTA}OBSERVATION...{Style.RESET_ALL}")
        observation = get_observation(user_input, planning, action, conversation)
        print(f"   {observation}")
        time.sleep(0.5)
        
      
        print(f"\n{Fore.RED} CONCLUSION...{Style.RESET_ALL}")
        conclusion = get_conclusion(user_input, planning, action, observation, conversation)
        print(f"   {conclusion}")
        time.sleep(0.5)
        
       
        print(f"\n{Fore.GREEN}FOLLOW-UP QUESTION...{Style.RESET_ALL}")
        follow_up = get_follow_up(user_input, planning, action, observation, conclusion, conversation)
        print(f"   {follow_up}")
        
        print("-" * 50)
        
        
        conversation.append(f"User: {user_input}")
        conversation.append(f"Stock Bro: {conclusion} {follow_up}")
        
        print()
        
    except Exception as e:
        print(f"{Fore.RED}\nError: {e}{Style.RESET_ALL}")
        print("Let's try again...")
        continue