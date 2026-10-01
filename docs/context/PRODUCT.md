# Product — Streamlit Greeter

> Absolute truth of the current product. Update when the product meaningfully changes.
> Human-maintained — `lane fold` does not write to this file.

## What it is
A minimal Streamlit web application that accepts a user's name via a text input field and displays a personalised greeting ("Good day, <name>") on the same page. It serves as a demonstration of Streamlit's input-output interaction pattern.

## Who uses it
Any user with a web browser who navigates to the running Streamlit app. No authentication or role differentiation.

## What it does
- Renders a text input labelled for name entry
- Displays "Good day, <name>" when a non-empty name is entered
- Shows nothing (no greeting) when the input is empty

## What it doesn't do
- User authentication or session management
- Persistent storage of names or interactions
- Multi-page navigation
- Custom theming or CSS overrides beyond Streamlit defaults
- Any backend API calls or external service integrations
