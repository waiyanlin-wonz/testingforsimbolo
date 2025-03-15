import streamlit as st

st.title("Streamlit App")

st.title("Welcome to My Streamlit Web Page")

st.subheader("This is a simple Streamlit application")

st.write("Testing for assignment 4")

user_input = st.text_input("Enter your name:")
st.write(f"Hello, {user_input}!")

st.button("Click Me")

if st.checkbox("Show more info"):
    st.write("assignment 4")

st.sidebar.header("Sidebar Menu")
st.sidebar.write("You can add more options here.")
