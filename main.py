import streamlit as st

st.title("Echo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# display messages on app rerun
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(
            message['content']
        )

# react to user input
if prompt := st.chat_input("What is up"):
    # display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # add user message to chat history
    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    response = f'Echo {prompt}'

    # display assistant response in chat essage container
    with st.chat_message("assistant"):
        st.markdown(response)

    # add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

