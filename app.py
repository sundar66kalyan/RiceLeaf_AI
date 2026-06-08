import streamlit as st
import numpy as np
from PIL import Image
import time

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="RiceLeaf AI - Disease Detection",
    page_icon="🌾",
    layout="centered"
)

# ------------------- CUSTOM CSS (modern, clean, responsive) -------------------
st.markdown("""
<style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9edf2 100%);
    }
    /* Title styling */
    .title-container {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(120deg, #2c5a2e, #6b8c42);
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        color: #4a6a3b;
        font-size: 1.1rem;
        margin-top: -0.5rem;
    }
    /* Model badge */
    .model-badge {
        background: white;
        border-radius: 30px;
        padding: 0.5rem 1.2rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        display: inline-block;
        margin: 1rem auto;
        border: 1px solid #d4e0d0;
    }
    .model-name {
        font-weight: 700;
        font-size: 1.2rem;
        color: #1e3a2f;
    }
    .model-accuracy {
        font-size: 1rem;
        color: #2e7d64;
        background: #e0f2e9;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        display: inline-block;
        margin-left: 0.8rem;
    }
    /* Card for upload area */
    .upload-card {
        background: white;
        border-radius: 28px;
        padding: 2rem;
        box-shadow: 0 20px 35px -12px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
        transition: transform 0.2s;
        border: 1px solid rgba(100,120,80,0.2);
    }
    .upload-card:hover {
        transform: translateY(-3px);
    }
    /* Analyze button */
    .stButton > button {
        background: linear-gradient(95deg, #2c5a2e, #4a7c3f);
        color: white;
        font-weight: 600;
        border-radius: 40px;
        padding: 0.6rem 2rem;
        font-size: 1.1rem;
        border: none;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(95deg, #1e4520, #3a6531);
        transform: scale(1.02);
        box-shadow: 0 8px 18px rgba(0,0,0,0.1);
    }
    /* Prediction card */
    .pred-card {
        background: #fef9e6;
        border-radius: 24px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 6px solid #6b8c42;
    }
    .disease-tag {
        background: #2c5a2e;
        color: white;
        padding: 0.2rem 1rem;
        border-radius: 30px;
        display: inline-block;
        font-weight: 500;
    }
    .confidence-bar {
        background: #e0e6e0;
        border-radius: 20px;
        height: 10px;
        margin: 8px 0;
        overflow: hidden;
    }
    .confidence-fill {
        background: #6b8c42;
        width: 0%;
        height: 100%;
        border-radius: 20px;
        transition: width 0.7s ease;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #dce5dc;
        font-size: 0.8rem;
        color: #6c7a6a;
    }
    .creator {
        font-weight: 500;
        color: #2c5a2e;
    }
</style>
""", unsafe_allow_html=True)

# ------------------- HEADER SECTION (like reference image 1) -------------------
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.markdown('<div class="title-container"><div class="main-title">🌾 RiceLeaf AI</div><div class="subtitle">Intelligent Rice Disease Detection System</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"><div class="model-badge"><span class="model-name">📱 MobileNetV2</span> <span class="model-accuracy">🎯 Accuracy: 91.67%</span></div></div>', unsafe_allow_html=True)

# ------------------- UPLOAD SECTION (reference image 2 style) -------------------
st.markdown('<div class="upload-card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Upload Rice Leaf Image",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed",
    help="Supports JPG, JPEG, PNG up to 200MB"
)
# Drag & drop hint
st.markdown('<p style="color:#7a8e7a; font-size:0.8rem;">📤 Click or drag & drop (JPG, JPEG, PNG) · Max 200MB</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ------------------- ANALYZE BUTTON -------------------
analyze = st.button("🔍 Analyze Disease", use_container_width=True)

# ------------------- PREDICTION LOGIC -------------------
classes = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut']

def predict_disease(image):
    """
    Replace this function with your actual model inference.
    Currently returns random probabilities for demo.
    """
    time.sleep(0.5)  # simulate inference delay
    preds = np.random.rand(3)
    preds = preds / preds.sum()
    return {classes[i]: float(preds[i]) for i in range(3)}

# ------------------- DISPLAY RESULTS -------------------
if analyze and uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Uploaded Rice Leaf", use_container_width=True)
    
    with st.spinner("🧠 Analyzing with MobileNetV2 ..."):
        predictions = predict_disease(image)
    
    sorted_preds = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
    top_disease, top_conf = sorted_preds[0]
    
    st.markdown(f"""
    <div class="pred-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="disease-tag">🌾 {top_disease}</span>
            <span style="font-weight:700; color:#2c5a2e;">{top_conf:.1%} confidence</span>
        </div>
    """, unsafe_allow_html=True)
    
    for disease, conf in sorted_preds:
        st.markdown(f"""
        <div style="margin-top: 12px;">
            <div style="display: flex; justify-content: space-between;">
                <span>{disease}</span>
                <span>{conf:.1%}</span>
            </div>
            <div class="confidence-bar">
                <div class="confidence-fill" style="width: {conf*100}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if top_conf > 0.7:
        st.success("✅ High confidence – recommended action: Apply targeted treatment.")
    elif top_conf > 0.45:
        st.info("⚠️ Medium confidence – consider re‑evaluation or retest.")
    else:
        st.warning("❓ Low confidence – image may be unclear, please upload another leaf photo.")

elif analyze and uploaded_file is None:
    st.error("📛 Please upload a rice leaf image first.")

# ------------------- FOOTER WITH CREATOR CREDIT -------------------
st.markdown(f"""
<div class="footer">
    🚀 Powered by MobileNetV2 · Trained on 10k+ rice leaf images<br>
    <span class="creator">✨ Project created by Kalyana Sundar - AI Engineer ✨</span>
</div>
""", unsafe_allow_html=True)