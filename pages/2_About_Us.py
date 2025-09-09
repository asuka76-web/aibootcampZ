import streamlit as st

st.set_page_config(page_title="About Us", layout="wide")
st.title("👥 About Us")

st.markdown("""
### Project Scope
This application is designed to help users better understand Singapore government services, especially those related to **CPF policies**.

### Objectives
- Provide a **chat-based Q&A tool** to simplify complex government content.
- Offer a **retirement planning simulator** to help users make informed financial decisions.

### Data Sources
- Official government websites via **Google Custom Search API**
- Responses generated using **OpenAI GPT-4o** model

### Features
- Natural language question answering with clickable citations.
- Interactive CPF savings projection based on user input.
""")

