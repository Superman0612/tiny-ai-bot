import streamlit as st
from app import ask_bot

st.title("🤖 Tiny AI Q&A Bot (Gemini 2.5)")
st.write("Ask me question below: ")

question = st.text_input("You: ")
if st.button("Ask"):
    if question.strip():
        answer = ask_bot(question)
        st.success(answer)