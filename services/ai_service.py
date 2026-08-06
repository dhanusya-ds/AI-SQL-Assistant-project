import os
import json
from groq import Groq  
from dotenv import load_dotenv 

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Load prompt from text file
def load_prompt(filename):
    prompt_path = os.path.join("prompts", filename)

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()


def analyze_sql_error(schema, query, error):

    prompt = load_prompt("sql_error_prompt.txt")

    prompt = prompt.format(
        schema=schema,
        query=query,
        error=error
    )

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

    content = response.choices[0].message.content.strip()

    # Remove Markdown code fences if present
    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.startswith("```"):
        content = content.replace("```", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        return {
            "mistake": "Unable to parse AI response",
            "correct_query": "",
            "explanation": content,
            "suggestion": ""
        } 

def generate_sql_learning(schema):

    prompt = load_prompt("sql_learning_prompt.txt")

    prompt = prompt.format(
        schema=schema
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown
    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.startswith("```"):
        content = content.replace("```", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        return {
            "error": "Unable to parse AI response",
            "raw_response": content
        }