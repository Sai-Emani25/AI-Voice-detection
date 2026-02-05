import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure with the new endpoint
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY"),
    transport='rest',
    client_options={'api_endpoint': 'https://generativelanguage.googleapis.com'}
)

print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
