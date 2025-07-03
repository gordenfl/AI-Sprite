from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
    )

prompt = PromptTemplate(
    input_variables=["news"],
    template="从这个新闻中请给我一个中文的大概意思: \n {news}"
)

chain = LLMChain(llm=llm, prompt=prompt)


def summarize_news(news_items):
    return [[item.split(":")[0], chain.run(news=item)] for item in news_items]
