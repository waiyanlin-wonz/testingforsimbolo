import streamlit as st

st.title("Streamlit App")

st.title("Welcome to My Streamlit Web Page")

st.subheader("This is a simple Streamlit application")

st.write("Streamlit makes it easy to build interactive web apps with Python.")

user_input = st.text_input("Enter your name:")
st.write(f"Hello, {user_input}!")

st.button("Click Me")

if st.checkbox("Show more info"):
    st.write("Streamlit is an open-source app framework for Machine Learning and Data Science projects.")

st.sidebar.header("Sidebar Menu")
st.sidebar.write("You can add more options here.")