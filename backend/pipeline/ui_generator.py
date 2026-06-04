from groq import Groq
from dotenv import load_dotenv
import os
import json

from models.design_model import Design
from models.ui_schema_model import UISchema

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_ui_schema(design: Design):

    prompt = f"""
You are a UI architect.

Given:

Entities:
{design.entities}

Flows:
{design.flows}

Generate a UI schema.

Return ONLY valid JSON.

Example:

{{
    "pages": [
        {{
            "name": "Dashboard",
            "components": [
                "Navbar",
                "Chart"
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

    return UISchema(**data)