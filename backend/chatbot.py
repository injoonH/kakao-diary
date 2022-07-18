import os
from dotenv import load_dotenv
import openai
import models


load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_prompt_from_chats(chats: list[models.Chat]) -> str:
    tmp = [f'Friend: {ch.question}\nYou: {ch.answer}' for ch in chats]
    return '\n'.join(tmp)


def get_chat_response(prev_chats: list[models.Chat]) -> str:
    prompt = get_prompt_from_chats(prev_chats) + '\nFriend:'
    
    res = openai.Completion.create(
        model='text-davinci-002',
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=['You:']
    )
    question = res.choices[0].text.replace('\n', '')
    print('==== QUESTION ====')
    print(question)
    return question


def get_diary(prev_chats: list[models.Chat]) -> str:
    prompt = get_prompt_from_chats(prev_chats)
    
    title_command = 'Summarize my short hand into one sentence:'
    content_command = 'Convert my short hand into a first-hand account of the meeting:'
    
    title_res = openai.Completion.create(
        model='text-davinci-002',
        prompt=title_command + '\n\n' + prompt,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    content_res = openai.Completion.create(
        model='text-davinci-002',
        prompt=content_command + '\n\n' + prompt,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    title = title_res.choices[0].text.replace('\n', '')
    content = content_res.choices[0].text.replace('\n', '')
    
    print('==== DIARY TITLE ====')
    print(title)
    print('==== DIARY CONTENT ====')
    print(content)
    
    return title, content
