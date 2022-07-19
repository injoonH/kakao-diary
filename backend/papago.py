import os
from dotenv import load_dotenv
import requests


load_dotenv()
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

PAPAGO_URL = 'https://openapi.naver.com/v1/papago/n2mt'


def get_translate(text):
    if text[0].encode().isalpha():
        a, b = 'en', 'ko'
    else:
        a, b = 'ko', 'en'
    
    data = {
        'text': text,
        'source': a,
        'target': b
    }
    header = {
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }

    response = requests.post(PAPAGO_URL, data=data, headers=header)
    
    if response.status_code != 200:
        return None
    return str.lower(response.json()['message']['result']['translatedText'])


if __name__ == '__main__':
    while True:
        text = input('> ')
        print(get_translate(text))
