import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
response = llm.invoke("Hello, world!")
print("LLM Response:", response.content)