import streamlit as st


def greeting(name: str) -> str | None:
    stripped = name.strip()
    if not stripped:
        return None
    return f"Good day, {stripped}"


name = st.text_input("Enter your name")
message = greeting(name)
if message:
    st.write(message)
