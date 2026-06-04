import json
import os

from groq import Groq
from dotenv import load_dotenv

from models.intent_models import Intent

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_intent(user_prompt: str):

    prompt = f"""
You are an application requirements analyzer.

Extract:
1. app_name
2. features
3. roles

Return ONLY valid JSON.

User Request:
{user_prompt}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    print("\n========== LLM RESPONSE ==========")
    print(content)
    print("==================================\n")

    # Remove markdown code fences
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    data = json.loads(content)

    return Intent(**data)