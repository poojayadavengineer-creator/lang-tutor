
import os 
from openai import OpenAI, base_url
from prompt import SYSTEM_PROMPT

LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
API_KEY = os.getenv("API_KEY")

client = OpenAI(base_url=LLM_ENDPOINT, api_key=API_KEY)

def get_answer(user_question: str) -> str:
    print("User question received in get_answer:", user_question)  # Debugging line
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_question}
        ],
        temperature=0.3
    )
    print("Response from OpenAI:", response)  # Debugging line
    return response.choices[0].message.content



