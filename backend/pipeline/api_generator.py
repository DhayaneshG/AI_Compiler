from groq import Groq
from dotenv import load_dotenv
import os
import json

from models.db_schema_model import DBSchema
from models.api_schema_model import APISchema

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_api_schema(db_schema: DBSchema):

    prompt = f"""
You are a backend architect.

Given this database schema:

{db_schema}

Generate REST API endpoints.

Return ONLY valid JSON.

Example:

{{
    "endpoints": [
        {{
            "path": "/patients",
            "method": "GET"
        }},
        {{
            "path": "/patients",
            "method": "POST"
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

    return APISchema(**data)