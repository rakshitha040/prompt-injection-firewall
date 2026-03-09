from groq import Groq
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

class AIAgent:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def process_prompt(self, prompt):
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",   # Updated model
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=512
        )

        return response.choices[0].message.content