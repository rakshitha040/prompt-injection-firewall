import streamlit as st
from agent import AIAgent
from firewall import PromptFirewall
from logger import log_event

st.title("🛡 Prompt Injection Firewall for AI Agents")

agent = AIAgent()
firewall = PromptFirewall()

prompt = st.text_area("Enter your prompt")

if st.button("Send to AI Agent"):

    result = firewall.inspect_prompt(prompt)

    if result["status"] == "sanitized":

        st.warning(f"⚠ Attack Detected: {result['attack_type']}")
        st.info("Prompt sanitized by firewall")

        response = agent.process_prompt(result["sanitized_prompt"])
        st.success(response)

    elif result["status"] == "safe":

        response = agent.process_prompt(prompt)
        st.success(response)

import json

st.subheader("🔍 Firewall Logs")

try:
    with open("logs.json") as f:
        logs = json.load(f)

        for log in logs[::-1]:
            st.write(log)

except:
    st.write("No logs yet")