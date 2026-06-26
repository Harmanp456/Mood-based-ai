import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


# ---------------- MODEL ----------------
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)


# ---------------- PAGE ----------------
st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon=":speech_balloon:",
    layout="centered"
)

st.markdown(
    """
    <style>
        :root {
            --panel: #ffffff;
            --panel-soft: #fff7ed;
            --ink: #111827;
            --muted: #526179;
            --line: #e2e8f0;
            --accent: #7c3aed;
            --accent-strong: #5b21b6;
            --cyan: #0891b2;
            --green: #16a34a;
            --warm: #f97316;
            --rose: #f43f5e;
        }

        .stApp {
            background:
                radial-gradient(circle at 8% 18%, rgba(244, 63, 94, 0.28), transparent 18rem),
                radial-gradient(circle at 86% 20%, rgba(8, 145, 178, 0.24), transparent 20rem),
                radial-gradient(circle at 52% 94%, rgba(249, 115, 22, 0.22), transparent 18rem),
                linear-gradient(135deg, #fff1f2 0%, #eef2ff 38%, #ecfeff 68%, #fff7ed 100%);
            color: var(--ink);
        }

        .block-container {
            max-width: 900px;
            padding-top: 2.5rem;
            padding-bottom: 8.5rem;
        }

        .hero {
            padding: 1.6rem 1.7rem;
            border: 1px solid rgba(124, 58, 237, 0.22);
            border-radius: 8px;
            background:
                linear-gradient(#ffffff, #ffffff) padding-box,
                linear-gradient(135deg, #f43f5e, #7c3aed, #0891b2, #f97316) border-box;
            box-shadow: 0 22px 55px rgba(124, 58, 237, 0.14);
            backdrop-filter: blur(18px);
            margin-bottom: 1.15rem;
        }

        .eyebrow {
            margin: 0 0 0.35rem 0;
            color: var(--rose);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0;
            text-transform: uppercase;
        }

        .hero h1 {
            margin: 0;
            color: transparent;
            background: linear-gradient(90deg, #f43f5e 0%, #7c3aed 42%, #0891b2 72%, #f97316 100%);
            -webkit-background-clip: text;
            background-clip: text;
            font-size: clamp(2.1rem, 7vw, 4.1rem);
            line-height: 1;
            letter-spacing: 0;
        }

        .hero p:last-child {
            max-width: 620px;
            margin: 0.75rem 0 0 0;
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.55;
        }

        div[role="radiogroup"] {
            gap: 0.75rem;
        }

        div[role="radiogroup"] label {
            min-height: 3rem;
            padding: 0.75rem 0.95rem;
            border: 1px solid rgba(124, 58, 237, 0.18);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.86);
            box-shadow: 0 10px 28px rgba(124, 58, 237, 0.08);
        }

        div[role="radiogroup"] label:hover {
            border-color: rgba(124, 58, 237, 0.5);
            background: #ffffff;
            transform: translateY(-1px);
        }

        div[role="radiogroup"] label:nth-child(1) {
            background: linear-gradient(135deg, rgba(255, 241, 242, 0.95), rgba(255, 255, 255, 0.86));
        }

        div[role="radiogroup"] label:nth-child(2) {
            background: linear-gradient(135deg, rgba(255, 247, 237, 0.95), rgba(255, 255, 255, 0.86));
        }

        div[role="radiogroup"] label:nth-child(3) {
            background: linear-gradient(135deg, rgba(236, 254, 255, 0.95), rgba(255, 255, 255, 0.86));
        }

        [data-testid="stChatMessage"] {
            border: 1px solid rgba(124, 58, 237, 0.14);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.92);
            box-shadow: 0 14px 34px rgba(124, 58, 237, 0.08);
            margin-bottom: 0.75rem;
        }

        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
            background: linear-gradient(135deg, rgba(236, 254, 255, 0.95), rgba(255, 255, 255, 0.9));
            border-color: rgba(8, 145, 178, 0.24);
        }

        .empty-chat {
            padding: 1rem 1.1rem;
            border: 1px dashed rgba(124, 58, 237, 0.42);
            border-radius: 8px;
            background:
                linear-gradient(135deg, rgba(255, 255, 255, 0.72), rgba(236, 254, 255, 0.58));
            color: var(--muted);
            margin: 1rem 0;
        }

        .stChatInputContainer {
            background: transparent;
        }

        [data-testid="stChatFloatingInputContainer"] {
            bottom: 0.35rem;
            padding-bottom: 0.35rem;
            background: linear-gradient(180deg, transparent 0%, rgba(255, 255, 255, 0.86) 38%, rgba(255, 255, 255, 0.96) 100%);
        }

        [data-testid="stChatInput"] {
            border: 1px solid rgba(124, 58, 237, 0.2);
            border-radius: 8px;
            box-shadow: 0 16px 36px rgba(124, 58, 237, 0.16);
        }

        .stButton > button {
            border-radius: 8px;
            border: 1px solid rgba(124, 58, 237, 0.22);
            background: linear-gradient(90deg, rgba(244, 63, 94, 0.08), rgba(124, 58, 237, 0.08), rgba(8, 145, 178, 0.08));
            color: var(--accent-strong);
            font-weight: 700;
            min-height: 2.8rem;
        }

        .stButton > button:hover {
            border-color: var(--accent);
            color: var(--accent);
            box-shadow: 0 10px 26px rgba(124, 58, 237, 0.15);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <section class="hero">
        <p class="eyebrow">Mood powered chat</p>
        <h1>AI Mood Chatbot</h1>
        <p>Choose a personality and keep the conversation flowing in the style you picked.</p>
    </section>
    """,
    unsafe_allow_html=True
)


# ---------------- MODE SELECTION ----------------
mode_choice = st.radio(
    "Choose your AI Mode:",
    ["Angry", "Funny", "Sad"],
    horizontal=True
)


# Map mode
if mode_choice == "Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_choice == "Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."


# ---------------- SESSION MEMORY ----------------
if "messages" not in st.session_state or st.session_state.get("current_mode") != mode:
    st.session_state.current_mode = mode
    st.session_state.messages = [SystemMessage(content=mode)]


# ---------------- DISPLAY CHAT ----------------
if len(st.session_state.messages) == 1:
    st.markdown(
        '<div class="empty-chat">Your conversation will appear here.</div>',
        unsafe_allow_html=True
    )

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)


# ---------------- USER INPUT ----------------
user_input = st.chat_input("Say something...")

if user_input:

    if user_input == "0":
        st.warning("Conversation ended. Refresh page to start again.")
        st.stop()

    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    response = model.invoke(st.session_state.messages)

    # Add AI message
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)


# ---------------- CLEAR BUTTON ----------------
st.divider()
if st.button("Reset Chat", use_container_width=True):
    st.session_state.messages = [SystemMessage(content=mode)]
    st.rerun()
