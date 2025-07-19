import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def explain_bug(log_chunk):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a senior backend engineer. Given logs, find the crash cause and suggest a fix."},
                {"role": "user", "content": f"Here are the logs:\n{log_chunk}"}
            ],
            extra_headers={
                "HTTP-Referer": "http://localhost:3000",  # optional
                "X-Title": "TimeTraveler"  # optional
            }
        )
        return response.choices[0].message.content
    except Exception as e:
        print("OpenRouter Error:", e)
        return f"Error from OpenRouter: {str(e)}"
