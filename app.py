import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Rice Leaf Disease Detector", layout="centered")

st.title("🌾 Rice Leaf Disease Detector")
st.markdown("Upload a rice leaf image to detect **Bacterial leaf blight**, **Brown spot**, or **Leaf smut**.")

classes = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut']

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Leaf", use_container_width=True)

    # Simulate prediction (same as your Gradio demo)
    preds = np.random.rand(3)
    preds = preds / preds.sum()
    result = {classes[i]: float(preds[i]) for i in range(3)}

    st.subheader("🔬 Disease Prediction")
    for disease, prob in result.items():
        st.write(f"**{disease}:** {prob:.2%}")

    # Optional: highlight the highest probability
    top_disease = max(result, key=result.get)
    st.success(f"✨ Most likely: **{top_disease}** with {result[top_disease]:.2%} confidence")
else:
    st.info("📤 Please upload a rice leaf image to see the prediction.")

st.markdown("---")
st.caption("👨‍💻 **Project by KalyanaSundar - AI Engineer** | Demo model – replace with your trained classifier")