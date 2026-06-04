from groq import Groq
from dotenv import load_dotenv
import os
import json

from models.intent_models import Intent
from models.api_schema_model import APISchema
from models.auth_schema_model import AuthSchema

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_auth_schema(intent: Intent, api_schema: APISchema):

    prompt = f"""
You are a security architect.

Roles:
{intent.roles}

API Schema:
{api_schema}

Generate permissions for each role.

Return ONLY valid JSON.

Example:

{{
    "roles": [
        {{
            "name": "admin",
            "permissions": [
                "manage_users",
                "manage_data"
            ]
        }}
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

    return AuthSchema(**data)