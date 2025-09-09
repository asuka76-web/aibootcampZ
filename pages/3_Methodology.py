import streamlit as st

st.set_page_config(page_title="Methodology", layout="wide")
st.title("🧠 Methodology")

st.markdown("""
### Overview
This app uses a combination of web scraping, language models, and Streamlit components to provide intelligent government service guidance.

---

### 📘 Use Case 1: Chatbot with Search
**Flowchart Steps:**
1. User inputs a government-related question.
2. App sends the query to **Google CSE** to get top 3 links.
3. These links are embedded as context and sent to **OpenAI GPT-4o**.
4. GPT returns an answer with cited URLs in Markdown format.
5. Answer is shown in the app with inline links.

---

### 💸 Use Case 2: CPF Retirement Simulator
**Flowchart Steps:**
1. User inputs age, CPF balance, contribution rate, etc.
2. App uses a simple monthly compounding interest formula.
3. It calculates and projects CPF amount until retirement.
4. Results are shown instantly.

---

### 📊 Data Flow
- User Input → API Calls / Simulation Logic → Result Displayed in UI

---

### 🗂️ Technologies Used
- **Streamlit** for UI
- **OpenAI API** for chat completions
- **Google Custom Search API** for official info lookup
""")
