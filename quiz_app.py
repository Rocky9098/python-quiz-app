import streamlit as st

st.set_page_config(page_title="Python Quiz", layout="centered")

st.title("🧠 Python Quiz: Exceptions & Command Line Arguments")
st.markdown("Test your knowledge on exception handling and command-line arguments!")

# Quiz data
quiz = [
    {
        "question": "What does a ZeroDivisionError indicate?",
        "options": ["Invalid syntax", "Division by zero", "Missing argument", "Wrong data type"],
        "answer": 1
    },
    {
        "question": "Which block always executes?",
        "options": ["try", "except", "finally", "raise"],
        "answer": 2
    },
    {
        "question": "What does sys.argv[0] represent?",
        "options": ["First argument", "Script name", "Last argument", "Argument count"],
        "answer": 1
    },
    {
        "question": "Which module provides structured parsing?",
        "options": ["sys", "os", "argparse", "math"],
        "answer": 2
    },
    {
        "question": "What does the raise keyword do?",
        "options": ["Catch an error", "Ignore an error", "Trigger an exception", "Log an error"],
        "answer": 2
    }
]

# Store user answers
score = 0
user_answers = []

with st.form("quiz_form"):
    for i, q in enumerate(quiz):
        st.subheader(f"Q{i+1}: {q['question']}")
        user_choice = st.radio("", q["options"], key=f"q{i}")
        user_answers.append(user_choice)
    submitted = st.form_submit_button("Submit Quiz")

if submitted:
    for i, q in enumerate(quiz):
        correct_option = q["options"][q["answer"]]
        if user_answers[i] == correct_option:
            score += 1
    st.success(f"🎉 You scored {score} out of {len(quiz)}!")
