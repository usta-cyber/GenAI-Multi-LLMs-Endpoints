from helper import *
import streamlit as st

st.title("Langchain Multiple LLMS Endpints")
eassy=st.text_input("Enter Eassy Topic:")
poem=st.text_input("Enter Poem Topic:")

if eassy:
    st.write(get_openai_response(eassy))

if poem:
    st.write(get_ollama_response(poem))