# ================================================
# PROJECT 2: IMAGE CLASSIFIER - FULL VERSION
# ================================================
# STEP 1: pip install transformers streamlit torch Pillow requests
# STEP 2: streamlit run p2_image.py
# ================================================

import streamlit as st
from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Image Classifier", page_icon="🖼️", layout="centered")

st.title("🖼️ AI Image Classifier")
st.markdown("Image upload cheyandi — AI adi enti undo top 5 predictions tho cheptundi!")
st.divider()

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    return pipeline("image-classification", model="google/vit-base-patch16-224")

with st.spinner("⏳ AI Model loading..."):
    model = load_model()
st.success("✅ Model Ready!")

# ---------- INPUT OPTIONS ----------
st.subheader("📥 Image Select Cheyyadam:")
option = st.radio("Ela select cheyyali?", ["📤 Upload from Computer", "🌐 Paste Image URL"], horizontal=True)

image = None

# Option 1: Upload
if option == "📤 Upload from Computer":
    uploaded = st.file_uploader("Image select cheyandi:", type=["jpg", "jpeg", "png", "webp"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.success("✅ Image loaded!")

# Option 2: URL
elif option == "🌐 Paste Image URL":
    url = st.text_input("Image URL ikkada paste cheyandi:", placeholder="https://example.com/image.jpg")
    if url:
        try:
            response = requests.get(url, timeout=8)
            image = Image.open(BytesIO(response.content)).convert("RGB")
            st.success("✅ Image loaded from URL!")
        except Exception as e:
            st.error(f"❌ URL work avvaledhu: {e}")

# ---------- SHOW IMAGE & CLASSIFY ----------
if image:
    st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("🖼️ Your Image:")
        st.image(image, use_column_width=True)

        # Image info
        st.markdown(f"**Size:** {image.size[0]} x {image.size[1]} px")
        st.markdown(f"**Mode:** {image.mode}")

    with col2:
        st.subheader("🤖 AI Prediction:")

        if st.button("🔍 Classify Now!", use_container_width=True):
            with st.spinner("AI analyzing image..."):
                results = model(image)

            st.markdown("### 🏆 Top 5 Results:")
            medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

            for i, result in enumerate(results[:5]):
                label = result["label"].replace("_", " ").title()
                score = result["score"]
                st.markdown(f"**{medals[i]} {label}**")
                st.progress(score, text=f"{score:.2%}")

            # Best prediction highlight
            best = results[0]
            best_label = best["label"].replace("_", " ").title()
            st.divider()
            st.success(f"🎯 Best Match: **{best_label}** ({best['score']:.2%})")

# ---------- SAMPLE IMAGES ----------
st.divider()
st.subheader("💡 Sample Images Try Cheyandi:")
st.markdown("Below URL copy chesi URL option lo paste cheyandi:")

samples = {
    "🐕 Dog": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/320px-YellowLabradorLooking_new.jpg",
    "🐱 Cat": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg",
    "🚗 Car": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/2019_Honda_Civic_%28FK%29_sedan_%2826418743877%29.jpg/320px-2019_Honda_Civic_%28FK%29_sedan_%2826418743877%29.jpg",
}

cols = st.columns(3)
for i, (name, url) in enumerate(samples.items()):
    with cols[i]:
        st.markdown(f"**{name}**")
        st.code(url, language=None)

# ---------- HOW IT WORKS ----------
st.divider()
with st.expander("🧠 How does this work?"):
    st.markdown("""
    ### Model Used: Google ViT (Vision Transformer)
    - Google trained model — **1000+ categories** recognize cheyagaladu
    - Dogs, cats, cars, flowers, birds anni identify cheyagaladu
    
    ### Steps:
    1. **Image** → 16x16 small patches ga divide avutundi
    2. **Patches** → numbers ga convert avutayi
    3. **Numbers** → AI model lo analyze avutayi
    4. **Output** → Top 5 matching categories + confidence scores
    
    ### Tips:
    - Clear images better results icchunu
    - Blurry or dark images lo accuracy takkuva untundi
    - Single object images better work chesthayi
    """)
# ================================================
# PROJECT 2: IMAGE CLASSIFIER - FULL VERSION
# ================================================
# STEP 1: pip install transformers streamlit torch Pillow requests
# STEP 2: streamlit run p2_image.py
# ================================================

import streamlit as st
from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Image Classifier", page_icon="🖼️", layout="centered")

st.title("🖼️ AI Image Classifier")
st.markdown("Image upload cheyandi — AI adi enti undo top 5 predictions tho cheptundi!")
st.divider()

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    return pipeline("image-classification", model="google/vit-base-patch16-224")

with st.spinner("⏳ AI Model loading..."):
    model = load_model()
st.success("✅ Model Ready!")

# ---------- INPUT OPTIONS ----------
st.subheader("📥 Image Select Cheyyadam:")
option = st.radio("Ela select cheyyali?", ["📤 Upload from Computer", "🌐 Paste Image URL"], horizontal=True)

image = None

# Option 1: Upload
if option == "📤 Upload from Computer":
    uploaded = st.file_uploader("Image select cheyandi:", type=["jpg", "jpeg", "png", "webp"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.success("✅ Image loaded!")

# Option 2: URL
elif option == "🌐 Paste Image URL":
    url = st.text_input("Image URL ikkada paste cheyandi:", placeholder="https://example.com/image.jpg")
    if url:
        try:
            response = requests.get(url, timeout=8)
            image = Image.open(BytesIO(response.content)).convert("RGB")
            st.success("✅ Image loaded from URL!")
        except Exception as e:
            st.error(f"❌ URL work avvaledhu: {e}")

# ---------- SHOW IMAGE & CLASSIFY ----------
if image:
    st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("🖼️ Your Image:")
        st.image(image, use_column_width=True)

        # Image info
        st.markdown(f"**Size:** {image.size[0]} x {image.size[1]} px")
        st.markdown(f"**Mode:** {image.mode}")

    with col2:
        st.subheader("🤖 AI Prediction:")

        if st.button("🔍 Classify Now!", use_container_width=True):
            with st.spinner("AI analyzing image..."):
                results = model(image)

            st.markdown("### 🏆 Top 5 Results:")
            medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

            for i, result in enumerate(results[:5]):
                label = result["label"].replace("_", " ").title()
                score = result["score"]
                st.markdown(f"**{medals[i]} {label}**")
                st.progress(score, text=f"{score:.2%}")

            # Best prediction highlight
            best = results[0]
            best_label = best["label"].replace("_", " ").title()
            st.divider()
            st.success(f"🎯 Best Match: **{best_label}** ({best['score']:.2%})")

# ---------- SAMPLE IMAGES ----------
st.divider()
st.subheader("💡 Sample Images Try Cheyandi:")
st.markdown("Below URL copy chesi URL option lo paste cheyandi:")

samples = {
    "🐕 Dog": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/320px-YellowLabradorLooking_new.jpg",
    "🐱 Cat": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/320px-Cat_November_2010-1a.jpg",
    "🚗 Car": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/2019_Honda_Civic_%28FK%29_sedan_%2826418743877%29.jpg/320px-2019_Honda_Civic_%28FK%29_sedan_%2826418743877%29.jpg",
}

cols = st.columns(3)
for i, (name, url) in enumerate(samples.items()):
    with cols[i]:
        st.markdown(f"**{name}**")
        st.code(url, language=None)

# ---------- HOW IT WORKS ----------
st.divider()
with st.expander("🧠 How does this work?"):
    st.markdown("""
    ### Model Used: Google ViT (Vision Transformer)
    - Google trained model — **1000+ categories** recognize cheyagaladu
    - Dogs, cats, cars, flowers, birds anni identify cheyagaladu
    
    ### Steps:
    1. **Image** → 16x16 small patches ga divide avutundi
    2. **Patches** → numbers ga convert avutayi
    3. **Numbers** → AI model lo analyze avutayi
    4. **Output** → Top 5 matching categories + confidence scores
    
    ### Tips:
    - Clear images better results icchunu
    - Blurry or dark images lo accuracy takkuva untundi
    - Single object images better work chesthayi
    """)
