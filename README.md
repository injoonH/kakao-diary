# Kakao Diary (하루톡)

## About The Project
본 서비스는 봇(bot)과 사용자의 카카오톡 채팅 기록을 기반으로 한 일기를 작성합니다.
사용자가 봇에 챗을 보내면 영어로 번역 후 GPT-3 API를 이용해 다음 질문을 생성합니다.
사용자가 `!!!`를 입력하면 기록이 종료되며, 서버는 그날 주고받은 채팅 내역을 이용해 일기를 작성합니다.

앱을 열면 서버의 데이터베이스에 저장된 일기 목록을 가져와 달력 상에 표시합니다.
각 날짜를 클릭하면 일기 상세 정보를 확인할 수 있으며, 우측 상단의 연필 모양 아이콘을 클릭하여 내용을 수정할 수 있습니다.

## Built With
- Frontend - React Native
- Backend - FastAPI

## Used API's
- KakaoTalk REST API
- Naver Papago API
- OpenAI GPT-3 API

## Contact
- 김효정 ([@rb37lu71](https://github.com/rb37lu71))
- 황인준 ([@injoonH](https://github.com/injoonH))