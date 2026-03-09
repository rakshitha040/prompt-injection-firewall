import streamlit as st
from agent import AIAgent
from detector import PromptDetector

# Page title
st.title("🛡 Prompt Injection Firewall for AI Agents")

# Initialize components
agent = AIAgent()
detector = PromptDetector()

# User input
prompt = st.text_area("Enter your prompt")

# Button action
if st.button("Send to AI Agent"):

    # Check for attacks
    attack = detector.detect_attack(prompt)

    if attack:
        st.error(f"⚠ Attack Detected: {attack}")
        st.warning("Prompt blocked by firewall.")

    else:
        response = agent.process_prompt(prompt)
        st.success(response)