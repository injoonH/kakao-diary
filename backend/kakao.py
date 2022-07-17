import json
import os
from dotenv import load_dotenv
import requests


load_dotenv()
REST_API_KEY = os.environ.get('REST_API_KEY')
REDIRECT_URI = os.environ.get('REDIRECT_URI')
AUTH_CODE = os.environ.get('AUTH_CODE')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

KAKAO_AUTH_URL = 'https://kauth.kakao.com/oauth/authorize'
KAKAO_TOKEN_URL = 'https://kauth.kakao.com/oauth/token'
KAKAO_FRIENDS_URL = 'https://kapi.kakao.com/v1/api/talk/friends'
KAKAO_MESSAGE_URL = 'https://kapi.kakao.com/v1/api/talk/friends/message/default/send'


def get_auth_code() -> None:
    payload = {
        'client_id': REST_API_KEY,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
    }
    auth_res = requests.get(KAKAO_AUTH_URL, params=payload)
    print(auth_res.url)


def get_access_token() -> None:
    body = {
        'grant_type': 'authorization_code',
        'client_id': REST_API_KEY,
        'redirect_uri': REDIRECT_URI,
        'code': AUTH_CODE,
    }
    header = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    response = requests.post(KAKAO_TOKEN_URL, data=body, headers=header)
    tokens = response.json()
    print('TOKEN', tokens)


def get_friends():
    header = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    response = requests.get(KAKAO_FRIENDS_URL, headers=header).json()
    friends = response.get('elements')
    print(friends)
    return friends


def get_friend_uuid_by_nickname(nickname: str) -> str:
    friends = get_friends()
    target = list(filter(lambda friend: friend.get('profile_nickname') == nickname, friends))
    if len(target) < 1:
        return None
    return target[0].get('uuid')


def send_message(uuid: str, message: str) -> None:    
    data = {
        'receiver_uuids': '["{}"]'.format(uuid),
        'template_object': json.dumps({
            'object_type': 'text',
            'text': message,
            'link': {
                'web_url': 'http://google.com'
            }
        })
    }
    header = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    response = requests.post(KAKAO_MESSAGE_URL, data=data, headers=header)
    print('Status:', response.status_code)
    print(response.json())


if __name__ == '__main__':
    # get_auth_code()
    # get_access_token()
    friends = get_friends()
    send_message(friends[0].get('uuid'), 'lorem ipsum')
