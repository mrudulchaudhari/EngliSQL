import openai
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_sql_from_english(english_text, schema_type, user_schema=""):
    system_prompt = f"You are a helpful assistant that converts English to {schema_type} SQL."

    if user_schema.strip():
        system_prompt += f" The database schema is: {user_schema}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"English: {english_text}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model = "o3-mini-2025-01-31",
            messages = messages,
            temperature = 0.3
        )
        return response['choices'][0]['message']['content'].strip()
    
    except Exception as e:
        return f"== Error generating SQL : {str(e)}" 