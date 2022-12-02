import os
import openai
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

def call_api(userMsg):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=userMsg,
        temperature=0.2,
        max_tokens=300
        )
    
    return response['choices'][0]['text']