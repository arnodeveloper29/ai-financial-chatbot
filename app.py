import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("💰 AI Financial Advisor")

user_input = st.text_input("Ask your financial question:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful financial advisor."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    st.write(answer)

st.warning("This is AI-generated advice. Not professional financial advice.")
