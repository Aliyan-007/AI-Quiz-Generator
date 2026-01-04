import streamlit as st
import openai
import wikipedia
import os

# 🔐 Load your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

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

# 🤖 Generate Quiz with GPT
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
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating quiz: {e}"

# 🚀 Trigger Quiz Generation
if topic:
    with st.spinner("Fetching summary and generating quiz..."):
        summary = get_wiki_summary(topic)
        st.subheader("📘 Wikipedia Summary")
        st.write(summary)

        quiz = generate_quiz(summary)
        st.subheader("📝 Generated Quiz")
        st.markdown(quiz)