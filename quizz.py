import streamlit as st
import requests
import wikipedia
import os

# 🔑 Load Hugging Face API key from environment variable
HF_API_KEY = os.getenv("HF_API_KEY")

# 🎯 App Title
st.set_page_config(page_title="AI Quiz Generator", layout="centered")
st.title("🎬 KON BANEGA CRORE PATTI")
st.markdown("Generate multiple-choice quizzes from Wikipedia summaries of historical topics.")

# 📥 User Input
topic = st.text_input("Enter a historical topic (e.g., Cold War, Partition of India):")

# 📚 Fetch Wikipedia Summary
def get_wiki_summary(topic):
    try:
        summary = wikipedia.summary(topic, sentences=10)
        return summary
    except Exception as e:
        return f"Error fetching summary: {e}"

# 🤖 Generate Quiz with Hugging Face
def generate_quiz(summary):
    prompt = f"""
    Based on the following historical summary, generate 5 multiple-choice questions.
    Each question should have:
    - A clear question
    - Four answer options (A, B, C, D)
    - The correct answer indicated
    - A brief explanation

    Summary:
    {summary}
    """

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct",
        headers=headers,
        json={"inputs": prompt}
    )

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return str(result)
    else:
        return f"Error generating quiz: {response.text}"

# 🚀 Trigger Quiz Generation
if topic:
    with st.spinner("Fetching summary and generating quiz..."):
        summary = get_wiki_summary(topic)
        st.subheader("📘 Wikipedia Summary")
        st.write(summary)

        quiz = generate_quiz(summary)
        st.subheader("📝 Generated Quiz")
        st.markdown(quiz)