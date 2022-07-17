# import requests

# url = 'https://kauth.kakao.com/oauth/token'
# rest_api_key = '877f0f5cafdb1c88993e56fad3d3827a'
# redirect_uri = 'https://example.com/oauth'
# authorize_code = 'FI3pTHhKvIlrtwA8uil7snDOK2aAKs1UuZ35QUZ5mHRbK99Dydjl-l5RjfwMUVOE85NO5QopcJ8AAAGCB3ZIfA'

# data = {
#     'grant_type':'authorization_code',
#     'client_id':rest_api_key,
#     'redirect_uri':redirect_uri,
#     'code': authorize_code,
#     }

# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)

# # json 저장
# import json
# with open(r"./kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

################################################################################################################################

# import requests
# import json

# #2.
# with open("./kakao_code.json","r") as fp:
#     tokens = json.load(fp)

# # print(tokens)
# # print(tokens["access_token"])

# friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# # GET /v1/api/talk/friends HTTP/1.1
# # Host: kapi.kakao.com
# # Authorization: Bearer {ACCESS_TOKEN}

# headers={"Authorization" : "Bearer " + tokens["access_token"]}

# result = json.loads(requests.get(friend_url, headers=headers).text)

# print(type(result))
# print("=============================================")
# print(result)
# print("=============================================")
# friends_list = result.get("elements")
# print(friends_list)
# # print(type(friends_list))
# print("=============================================")
# print(friends_list[0].get("uuid"))
# friend_id = friends_list[0].get("uuid")
# print(friend_id)

###############################################################################################################################
import requests
import json

with open(r"./kakao_code.json","r") as fp:
    tokens = json.load(fp)
# print(tokens)
# print(tokens["access_token"])

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# GET /v1/api/talk/friends HTTP/1.1
# Host: kapi.kakao.com
# Authorization: Bearer {ACCESS_TOKEN}

headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)

print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
# print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id)

send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"성공입니다!",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code