import streamlit as st
import requests

st.set_page_config(page_title="AI Knowledge Navigator")

st.title("📚 AI Knowledge Navigator")
st.write("Ask questions from Bhagavad Gita")

backend_url = "https://ai-knowledge-navigator.onrender.com/ask"

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if question:
        with st.spinner("Thinking..."):
            response = requests.post(
                backend_url,
                json={"question": question}
            )

        if response.status_code == 200:
            st.success(response.json()["answer"])
        else:
            st.error("Backend error")
