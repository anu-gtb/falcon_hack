from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

AI71_BASE_URL='https://api.ai71.ai/v1/'
AI71_API_KEY=os.environ['API_KEY']

chat=ChatOpenAI(
    model='tiiuae/falcon-180B-chat',
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=True
)

def check(text):
    base=chat.invoke([
        SystemMessage(
            content='You are a study tutor, designed to give detailed explaination of mistakes in text given by user in terms of correctness. Also, point out grammatical mistakes and spelling mistakes in each word used.'
        ),
        HumanMessage(content=text)
    ])
    ans=base.content
    return ans