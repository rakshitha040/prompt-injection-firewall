import streamlit as st
from agent import AIAgent

st.title("🛡 Prompt Injection Firewall for AI Agents")

agent = AIAgent()

prompt = st.text_area("Enter your prompt")

if st.button("Send to AI Agent"):
    response = agent.process_prompt(prompt)
    st.write("AI Response:", response)