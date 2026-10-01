# Behavior Spec — T-streamlit-greeter-4mm918: Name input renders personalised greeting
> Source: task card ACs + snapshot-TSD.md

## B-1 (tracer bullet): AC-1 [behavior]: When a non-empty name is entered, the greeting "Good day, <name>" is displayed
- Given: a `greeting` function that accepts a name string
- When: called with a non-empty name (e.g. "Alice")
- Then: returns the string "Good day, Alice"

## B-2: AC-2 [behavior]: When the input is empty or whitespace-only, no greeting is displayed
- Given: a `greeting` function that accepts a name string
- When: called with an empty string or a whitespace-only string (e.g. "" or "   ")
- Then: returns None (or falsy value) so the UI renders nothing

## B-3: AC-3 [e2e]: A user opening the app in a browser can type a name and see the greeting on the same page
- Given: the Streamlit app (`app.py`) is running
- When: the user sets the name text input to "Alice"
- Then: the page renders the text "Good day, Alice" and no other greeting text
