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

    if result["status"] == "blocked":

        log_event(prompt, result["attack_type"], "BLOCKED")

        st.error(f"⚠ Attack Detected: {result['attack_type']}")
        st.warning("Prompt blocked by firewall")

    else:

        response = agent.process_prompt(prompt)

        log_event(prompt, "None", "ALLOWED")

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