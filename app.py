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

# ---------- Load Logs ----------
blocked = 0
sanitized = 0
safe = 0

try:
    with open("logs.json") as f:
        logs = json.load(f)
        df = pd.DataFrame(logs)

        blocked = len(df[df["status"] == "BLOCKED"])
        sanitized = len(df[df["status"] == "SANITIZED"])
        safe = len(df[df["status"] == "ALLOWED"])

except:
    df = pd.DataFrame()

# ---------- Sidebar ----------
st.sidebar.title("🧠 Firewall Monitor")

st.sidebar.success("Firewall Status: ACTIVE")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Security Metrics")

st.sidebar.metric("Blocked Attacks", blocked)
st.sidebar.metric("Sanitized Prompts", sanitized)
st.sidebar.metric("Safe Prompts", safe)

st.sidebar.markdown("---")

st.sidebar.write("Protected Systems:")
st.sidebar.write("✔ AI Agent")
st.sidebar.write("✔ External Prompts")
st.sidebar.write("✔ Tool Access")

st.sidebar.markdown("---")

st.sidebar.subheader("🔥 Firewall Status")

st.sidebar.info("Prompt Inspection Active")

st.sidebar.write("Security Layers:")
st.sidebar.write("✔ Content Inspection")
st.sidebar.write("✔ Attack Detection")
st.sidebar.write("✔ Policy Enforcement")
st.sidebar.write("✔ Prompt Sanitization")
st.sidebar.write("✔ Audit Logging")

# ---------- Chat History ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- AI Chat Interface ----------
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

    st.session_state.messages.append(("User", prompt))
    st.session_state.messages.append(("Agent", response))


# ---------- Conversation ----------
st.markdown("---")
st.subheader("🧾 Conversation")

for role, message in st.session_state.messages:

    if role == "User":
        st.write(f"👤 **User:** {message}")
    else:
        st.write(f"🤖 **Agent:** {message}")


# ---------- Analytics ----------
st.markdown("---")
st.subheader("📊 Attack Analytics Dashboard")

if not df.empty:

    st.subheader("📜 Firewall Logs")
    st.dataframe(df)

    st.subheader("📈 Attack Distribution")

    attack_counts = df["attack_type"].value_counts()

    st.bar_chart(attack_counts)

else:
    st.write("No logs yet.")