from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain`s server",
    version="1.0",
    description="This is Simple End Point for LLM applications"
)


openai_llm=ChatOpenAI(model='gpt-3.5-turbo')
ollama_llm=OllamaLLM(model='llama2')


prompt1=ChatPromptTemplate.from_template("Write an eassay on {topic} maximum 100 words")
prompt2=ChatPromptTemplate.from_template("write a joke on {topic} ")
chain_openai=prompt1|openai_llm
chain_ollama=prompt2|ollama_llm

add_routes(
    app,
    chain_openai,
    path="/openai"
)

add_routes(
    app,
    chain_ollama,
    path="/ollama"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)