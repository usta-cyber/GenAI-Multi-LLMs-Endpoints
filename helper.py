import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/openai/invoke",
                           json={'input':{'topic':input_text}})
    return response.json()['output']['content']



def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/ollama/invoke",
                           json={'input':{'topic':input_text}})
    return response.json()['output']
