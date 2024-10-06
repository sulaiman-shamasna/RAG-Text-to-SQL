from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate
from langchain.utilities import SQLDatabase
from sqlalchemy import create_engine, MetaData, Table, Column, inspect
from langchain_experimental.sql import SQLDatabaseChain

import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print(f"OpenAI API Key: {openai_api_key}")
else:
    print("OpenAI API Key not found in .env file.")

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)