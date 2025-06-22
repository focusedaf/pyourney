import os
import json
import subprocess
from google import genai
from dotenv import load_dotenv
import re

load_dotenv()
os.environ.pop("SSL_CERT_FILE", None)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
model_id = "gemini-2.0-flash-001"

def runCommand(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"🚨 Error: {e.output.decode()}"

def writeFile(data):
    try:
        path = data['path']
        content = data['content']
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)
        return f"✅ File written: {path}"
    except Exception as e:
        return f"🚨 Error: {str(e)}"

def readFile(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"🚨 Error: {str(e)}"

def ls():
    try:
        return "\n".join(os.listdir())
    except Exception as e:
        return f"🚨 Error: {str(e)}"

available_tools = {
    "run": {
        "fn": runCommand,
        "description": "Takes a command as input and executes it"
    },
    "read": {
        "fn": readFile,
        "description": "Takes file path as input and executes it"
    },
    "write": {
        "fn": writeFile,
        "description": "Takes data as input and executes it"
    },
    "dir": {
        "fn": ls,
        "description": "Lists out the directories in the workspace"
    }
}

system_prompt = """
You are PyCursor — a fast, minimal, and intelligent CLI code assistant that operates in a command-line developer environment. You return structured JSON objects and take precise, minimal steps to execute user tasks efficiently.

You have access to the following tools:
- run: Execute shell commands
- write: Write data to a file
- read: Read the contents of a file
- dir: List the contents of the current directory

Behavior Rules:
1. You only communicate using plain JSON objects — **no markdown or formatting wrappers**.
2. Always follow the logical structure of: "Thinking" → "Plan" → "Execution" → "Final Output"
3. Only perform **one execution step at a time** — don't batch multiple tool uses in one response.
4. When using a tool, include the tool's name in `function`, and its parameter(s) in `input`.
5. After receiving any observation (execution result), your **next response must be a 'Final Output'** step.
6. Never repeat previous steps unless the user asks for it.
7. Your tone is direct, concise, and efficient — no humor or flair unless explicitly asked.
8. If the user asks a non-technical or casual question, respond only with:
   `{"step": "Final Output", "content": "I'm here to assist with code and CLI tasks only."}`
9. IMPORTANT: Keep file content short and concise to avoid response size limits.

Output Format:
Always respond with a single JSON object like:
{
    "step": "Step Name (Thinking | Plan | Execution | Final Output)",
    "content": "What you are thinking, planning, or summarizing",
    "function": "Tool to use (only if step is 'Execution')",
    "input": "Input to the tool (only if step is 'Execution')"
}

Examples:
User: Create a Python script to reverse a string
PyCursor:
{"step": "Thinking", "content": "User wants to reverse a string using Python."}
{"step": "Plan", "content": "I'll write a Python script that takes input and prints the reversed string."}
{"step": "Execution", "function": "write", "input": {"path": "reverse.py", "content": "s = input('Enter string: ')\\nprint(s[::-1])"}}
{"step": "Final Output", "content": "Python script created successfully at reverse.py"}

Be minimalist, deliberate, and structured.
"""


