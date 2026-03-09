import streamlit as st
from agent import AIAgent
from firewall import PromptFirewall

st.title("🛡 Prompt Injection Firewall for AI Agents")

agent = AIAgent()
firewall = PromptFirewall()

prompt = st.text_area("Enter your prompt")

if st.button("Send to AI Agent"):

    result = firewall.inspect_prompt(prompt)

    if result["status"] == "blocked":
        st.error(f"⚠ Attack Detected: {result['attack_type']}")
        st.warning(result["message"])

    else:
        response = agent.process_prompt(prompt)
        st.success(response)