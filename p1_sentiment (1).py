# ================================================
# PROJECT 1: SENTIMENT ANALYSIS - FULL VERSION
# ================================================
# STEP 1: pip install transformers streamlit torch
# STEP 2: streamlit run p1_sentiment.py
# ================================================

import streamlit as st
from transformers import pipeline

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Sentiment Analysis", page_icon="😊", layout="centered")

st.title("😊 Sentiment Analysis App")
st.markdown("Text enter cheyandi — AI meeru feeling detect chestundi!")
st.divider()

# ---------- LOAD AI MODEL ----------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

with st.spinner("⏳ AI Model loading..."):
    model = load_model()
st.success("✅ Model Ready!")

# ---------- USER INPUT ----------
text = st.text_area("✍️ Meeru text ikkada type cheyandi:", placeholder="Example: I love AI projects!", height=150)

col1, col2 = st.columns(2)
with col1:
    analyze_btn = st.button("🔍 Analyze", use_container_width=True)
with col2:
    clear_btn = st.button("🗑️ Clear", use_container_width=True)

if clear_btn:
    st.rerun()

# ---------- ANALYZE SINGLE TEXT ----------
if analyze_btn:
    if not text.strip():
        st.warning("⚠️ Please text type cheyandi!")
    else:
        with st.spinner("Analyzing..."):
            result = model(text)[0]

        label = result["label"]
        score = result["score"]

        st.divider()
        st.subheader("📊 Result:")

        if label == "POSITIVE":
            st.success("😊 POSITIVE Sentiment")
        else:
            st.error("😢 NEGATIVE Sentiment")

        st.metric("Confidence Score", f"{score:.2%}")
        st.progress(score)

        st.divider()
        st.subheader("📈 Score Breakdown:")
        col1, col2 = st.columns(2)
        with col1:
            pos_score = score if label == "POSITIVE" else 1 - score
            st.metric("✅ Positive", f"{pos_score:.2%}")
        with col2:
            neg_score = score if label == "NEGATIVE" else 1 - score
            st.metric("❌ Negative", f"{neg_score:.2%}")

# ---------- EXAMPLE SENTENCES ----------
st.divider()
st.subheader("💡 Try These Examples:")

examples = [
    "I love this AI project!",
    "This is the worst day ever.",
    "Amazing work, keep it up!",
    "I hate waiting in long lines.",
    "Today is a beautiful day!"
]

for ex in examples:
    if st.button(ex, use_container_width=True, key=ex):
        res = model(ex)[0]
        if res["label"] == "POSITIVE":
            st.success(f"😊 POSITIVE — {res['score']:.2%}")
        else:
            st.error(f"😢 NEGATIVE — {res['score']:.2%}")

# ---------- BATCH ANALYSIS ----------
st.divider()
st.subheader("📋 Batch Analysis — Multiple Sentences:")
batch_text = st.text_area(
    "Multiple lines enter cheyandi (each line = one sentence):",
    placeholder="I love Python!\nThis is boring.\nAI is amazing!",
    height=120,
    key="batch"
)

if st.button("🔍 Analyze All Lines", use_container_width=True):
    lines = [l.strip() for l in batch_text.strip().split("\n") if l.strip()]
    if lines:
        with st.spinner("All lines analyzing..."):
            results = model(lines)
        st.subheader("Results:")
        for line, res in zip(lines, results):
            if res["label"] == "POSITIVE":
                st.success(f"😊 '{line}' → POSITIVE ({res['score']:.2%})")
            else:
                st.error(f"😢 '{line}' → NEGATIVE ({res['score']:.2%})")
    else:
        st.warning("Please text enter cheyandi!")

# ---------- HOW IT WORKS ----------
st.divider()
with st.expander("🧠 How does this work?"):
    st.markdown("""
    ### Model Used: DistilBERT
    - Google **BERT** model lightweight version
    - Thousands of reviews tho trained
    
    ### Steps:
    1. **Text** → words split into tokens
    2. **Tokens** → numbers ga convert
    3. **Numbers** → AI model analyze chestundi
    4. **Output** → POSITIVE or NEGATIVE + confidence score
    
    ### Score Meaning:
    - **90%+** → AI chala confident
    - **70-90%** → AI confident
    - **50-70%** → AI not very sure
    """)
