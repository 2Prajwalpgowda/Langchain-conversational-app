import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Streamlit UI setup
st.set_page_config(page_title="ChatModelApp", page_icon=":robot:")
st.header("Hey, I'm your Chat Bot")

# Initialize session messages
if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [SystemMessage(content="You are a helpful AI assistant.")]

# Function to load answer from the chatbot
def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question))

    assistant_answer  = chat.generate(st.session_state.sessionMessages )

    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


# Function to get user input
def get_text():
    return st.text_input("You: ")

# Initialize ChatOpenAI object
chat = ChatOpenAI(temperature=0)

# Streamlit UI components
user_input = get_text()
submit = st.button('Generate')

# Generate response when submit button is clicked
if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response)

