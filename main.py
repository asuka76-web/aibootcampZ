import streamlit as st
import requests
from openai import OpenAI

# --- Load API keys from Streamlit secrets ---
google_api_key = st.secrets["GOOGLE_API_KEY"]
google_cse_id = st.secrets["GOOGLE_CSE_ID"]

# Create OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Password
def check_password():  
    """Returns `True` if the user had the correct password."""  
    def password_entered():  
        """Checks whether a password entered by the user is correct."""  
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):  
            st.session_state["password_correct"] = True  
            del st.session_state["password"]  # Don't store the password.  
        else:  
            st.session_state["password_correct"] = False  
    # Return True if the passward is validated.  
    if st.session_state.get("password_correct", False):  
        return True  
    # Show input for password.  
    st.text_input(  
        "Password", type="password", on_change=password_entered, key="password"  
    )  
    if "password_correct" in st.session_state:  
        st.error("😕 Password incorrect")  
    return False


# --- App Title ---
st.set_page_config(page_title="AskGov SG - CPF Q&A", layout="wide")
st.title("🇸🇬 AskGov SG - CPF Policy Q&A")

# --- Disclaimer ---
with st.expander("📢 Important Disclaimer"):
    st.markdown("""
    **IMPORTANT NOTICE:** This web application is a prototype developed for educational purposes only. The information provided here is **NOT** intended for real-world usage and should **not** be relied upon for making any decisions, especially those related to **financial, legal, or healthcare matters**.

    Furthermore, please be aware that the LLM may generate **inaccurate or incorrect information**. You assume full responsibility for how you use any generated output.

    Always consult with **qualified professionals** for accurate and personalized advice.
    """)

# --- Sidebar ---
st.sidebar.header("User Info")
location = st.sidebar.selectbox("Where are you from?", ["Singapore", "Others"])
need = st.sidebar.selectbox("What do you need?", ["CPF"])

# --- Google CSE Function ---
def fetch_gov_info_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={google_cse_id}&key={google_api_key}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        st.error(f"Error fetching Google results: {e}")
        return []

    sources = []
    if "items" in data:
        for item in data["items"][:3]:
            sources.append({
                "title": item["title"],
                "snippet": item["snippet"],
                "url": item["link"]
            })
    return sources

# --- GPT Function ---
def ask_llm(query, sources, need, location):
    # Prepare sources as Markdown links
    context_text = "\n".join([f"- [{s['title']}]({s['url']})" for s in sources])

    response = client.chat.completions.create(
        model="gpt-4o",  # Or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant trained in Singapore government processes (CPF, ICA, HDB). Always cite official sources as Markdown URLs."},
            {"role": "user", "content": f"User is from: {location}\nUser need: {need}\nQuestion: {query}\n\nOfficial sources:\n{context_text}"}
        ],
        max_tokens=500,
        temperature=0
    )
    return response.choices[0].message.content

# --- User Input ---
user_query = st.text_input("Ask a question about any Singapore Government process:")

if st.button("Get Answer"):
    if user_query:
        with st.spinner("Searching official government sources..."):
            sources = fetch_gov_info_google(user_query)
            if not sources:
                st.warning("No official results found. Please try a different query.")
            else:
                answer = ask_llm(user_query, sources, need, location)
                st.success("Here’s a simplified explanation:")
                st.markdown(answer)  # no need for unsafe_allow_html=True
    else:
        st.warning("Please type your question first.")

# --- Quick Links ---
st.markdown("### 📌 Quick Links")
st.markdown("- [ICA Services](https://www.ica.gov.sg)")
st.markdown("- [CPF Board](https://www.cpf.gov.sg)")
st.markdown("- [HDB Info](https://www.hdb.gov.sg)")
