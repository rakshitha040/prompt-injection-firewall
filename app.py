import streamlit as st
import json
import pandas as pd

from agent import AIAgent
from firewall import PromptFirewall
from logger import log_event

# Page configuration
st.set_page_config(page_title="AI Prompt Injection Firewall", layout="wide")

# Title
st.title("🛡 AI Prompt Injection Firewall Dashboard")

# Initialize components
agent = AIAgent()
firewall = PromptFirewall()

# Sidebar firewall monitor
st.sidebar.title("🧠 Firewall Monitor")
st.sidebar.success("Firewall Status: ACTIVE")

st.sidebar.markdown("---")
st.sidebar.write("Protected Systems:")
st.sidebar.write("✔ AI Agent")
st.sidebar.write("✔ External Prompts")
st.sidebar.write("✔ Tool Access")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Layout columns
col1, col2 = st.columns([2,1])

# LEFT PANEL - AI Chat Interface
with col1:

    st.subheader("💬 AI Agent Interface")

    prompt = st.text_area("Enter your prompt")

    send = st.button("Send Prompt")

    if send and prompt:

        result = firewall.inspect_prompt(prompt)

        if result["status"] == "sanitized":

            st.warning(f"⚠ Attack Detected: {result['attack_type']}")
            st.info("Prompt sanitized by firewall")

            response = agent.process_prompt(result["sanitized_prompt"])

            log_event(prompt, result["attack_type"], "SANITIZED")

        elif result["status"] == "safe":

            response = agent.process_prompt(prompt)

            log_event(prompt, "None", "ALLOWED")

        # Save conversation
        st.session_state.messages.append(("User", prompt))
        st.session_state.messages.append(("Agent", response))


# RIGHT PANEL - Firewall Status
with col2:

    st.subheader("🔥 Firewall Status")

    st.info("Prompt Inspection Active")

    st.write("Security Layers:")
    st.write("✔ Content Inspection")
    st.write("✔ Attack Detection")
    st.write("✔ Policy Enforcement")
    st.write("✔ Prompt Sanitization")
    st.write("✔ Audit Logging")


# Conversation display
st.markdown("---")
st.subheader("🧾 Conversation")

for role, message in st.session_state.messages:

    if role == "User":
        st.write(f"👤 **User:** {message}")

    else:
        st.write(f"🤖 **Agent:** {message}")


# Logs + Analytics
st.markdown("---")
st.subheader("📊 Attack Analytics Dashboard")

try:

    with open("logs.json") as f:

        logs = json.load(f)

        df = pd.DataFrame(logs)

        if not df.empty:

            st.subheader("📜 Firewall Logs")

            st.dataframe(df)

            st.subheader("📈 Attack Distribution")

            attack_counts = df["attack_type"].value_counts()

            st.bar_chart(attack_counts)

except:
    st.write("No logs yet.")