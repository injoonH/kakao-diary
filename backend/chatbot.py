import os
from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_chat_response(message: str) -> str:
    res = openai.Completion.create(
        model='text-davinci-002',
        prompt=f'You: {message}\nFriend:',
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=['You:']
    )
    print(res)
    return res.choices[0].text
