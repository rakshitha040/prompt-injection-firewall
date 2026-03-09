import streamlit as st

st.title("🛡 Prompt Injection Firewall for AI Agents")

prompt = st.text_area("Enter your prompt")

if st.button("Send to AI Agent"):
    st.write("Prompt received:", prompt)