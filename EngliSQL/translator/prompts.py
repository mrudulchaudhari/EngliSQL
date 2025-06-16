import requests
import re

def generate_sql_from_english(english_text, schema_type, user_schema=""):
    prompt = f"""You are a professional SQL query generator. 
Your job is to translate natural language into accurate {schema_type} SQL queries.

ONLY return the SQL query.
DO NOT explain anything.
DO NOT include backticks or markdown syntax.
DO NOT say anything before or after the SQL.
"""
    if user_schema.strip():
        prompt += f"The database schema is: {user_schema}\n"
    prompt += f"English: {english_text}"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",  # You're using mistral
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()
        result = response.json()
        full_response = result["response"].strip()

        # Extract SQL code block using regex
        match = re.search(r"```sql\s+(.*?)```", full_response, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
        
        # Fallback: extract SELECT/INSERT/etc. if no code block is found
        lines = full_response.splitlines()
        for line in lines:
            if line.strip().lower().startswith(("select", "insert", "update", "delete", "create", "drop")):
                return line.strip()

        return full_response  # last resort

    except Exception as e:
        return f"== Error generating SQL: {str(e)}"
