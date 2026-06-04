from groq import Groq
from dotenv import load_dotenv
import os
import json

from models.intent_models import Intent
from models.design_model import Design

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_design(intent: Intent):

    prompt = f"""
You are a software architect.

Given this application intent:

App Name:
{intent.app_name}

Features:
{intent.features}

Roles:
{intent.roles}

Generate:

1. entities
2. flows

Return ONLY valid JSON.

Example:

{{
    "entities": [
        "User",
        "Contact"
    ],
    "flows": [
        "Login",
        "Manage Contacts"
    ]
}}
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

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    data = json.loads(content)

    return Design(**data)