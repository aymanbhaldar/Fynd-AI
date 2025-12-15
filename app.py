import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
from openai import OpenAI

# 1. Page Config
st.set_page_config(page_title="Fynd AI Feedback System", layout="wide")

# 2. Secure API Key Handling
# Tries to get key from secrets file first, then environment variables
if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
else:
    api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("🚨 No API Key found! Please check your secrets.toml file.")
    st.stop()

client = OpenAI(api_key=api_key)
DATA_FILE = "reviews.json"

# 3. Helper Functions
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_review(data):
    reviews = load_data()
    reviews.append(data)
    with open(DATA_FILE, "w") as f:
        json.dump(reviews, f, indent=4)

def analyze_review(rating, text):
    """Sends request to LLM for analysis"""
    prompt = f"""
    Analyze this review. Rating: {rating}/5. Review: "{text}".
    Return a JSON object with exactly these keys:
    - 'reply': A polite, empathetic response to the customer.
    - 'summary': A concise 5-10 word summary.
    - 'action': A concrete recommended business action.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"reply": "Error generating response", "summary": "Error", "action": f"System Error: {e}"}

# 4. Navigation Layout
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["User Dashboard", "Admin Dashboard"])

# --- PAGE 1: USER DASHBOARD ---
if page == "User Dashboard":
    st.title("🌟 Leave a Review")
    st.write("Share your experience with us!")
    
    with st.form("review_form"):
        stars = st.slider("Rating", 1, 5, 5)
        text = st.text_area("Your Review")
        submit_btn = st.form_submit_button("Submit Feedback")
        
        if submit_btn and text:
            with st.spinner("AI is analyzing your feedback..."):
                analysis = analyze_review(stars, text)
                
                record = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "rating": stars,
                    "review": text,
                    "ai_summary": analysis['summary'],
                    "ai_action": analysis['action']
                }
                save_review(record)
                
            st.success("✅ Feedback Received!")
            st.info(f"**Company Reply:** {analysis['reply']}")

# --- PAGE 2: ADMIN DASHBOARD ---
elif page == "Admin Dashboard":
    st.title("📊 Admin Insights")
    
    data = load_data()
    if not data:
        st.info("No reviews yet. Go to the User Dashboard to add one!")
    else:
        df = pd.DataFrame(data)
        
        # Metrics
        col1, col2 = st.columns(2)
        col1.metric("Total Reviews", len(df))
        col1.metric("Average Rating", f"{df['rating'].mean():.1f} ⭐")
        
        # Data Display
        st.divider()
        st.subheader("Live Feed")
        st.dataframe(df[['timestamp', 'rating', 'ai_summary', 'ai_action']], use_container_width=True)