import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

# Use the PORT environment variable if set; otherwise, default to 8501
port = int(os.getenv("PORT", 8501))

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)

# Run Streamlit on the specified port
if __name__ == "__main__":
    st.run(port=port, server_address="0.0.0.0")