import openai
import time
from openai.error import InvalidRequestError


OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
model_id = "gpt-3.5-turbo"

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

conversation = []
conversation.append({'role': 'system', 'content': 'How may I help you?'})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
while True:
    prompt = input("chat : ")
    if prompt=="good night":
        print("okay bye")
        time.sleep(2)
        break
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    res = conversation[-1]['content']
    print("response : ",res )        
    pass