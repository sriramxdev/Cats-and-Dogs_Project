import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Configure page
st.set_page_config(
    page_title="Cats vs Dogs Classifier",
    page_icon="🐱🐶",
    layout="centered"
)

st.title("🐱🐶 Cats vs Dogs Classifier")
st.markdown("Upload an image and let our AI model predict whether it's a cat or a dog!")

@st.cache_resource
def load_model():
    """Load the pre-trained model with caching for better performance"""
    try:
        # Try to load the .keras model first (recommended format)
        model_path = "cats_dogs_savedmodel.keras"
        if os.path.exists(model_path):
            model = tf.keras.models.load_model(model_path)
            st.success("✅ Model loaded successfully!")
            return model
        else:
            # Fallback to .h5 format
            model_path = "cats_dogs_model.h5"
            if os.path.exists(model_path):
                model = tf.keras.models.load_model(model_path)
                st.success("✅ Model loaded successfully!")
                return model
            else:
                st.error("❌ Model file not found. Please ensure the model file is in the repository.")
                return None
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

# Load model
model = load_model()

# Upload image file
image_file = st.file_uploader(
    "Choose an image...", 
    type=["jpg", "jpeg", "png"],
    help="Upload a clear image of a cat or dog for best results"
)

if model and image_file:
    try:
        # Display the uploaded image
        image = Image.open(image_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Preprocess the image
        input_shape = model.input_shape
        target_size = input_shape[1:3]  # Get height and width
        img_resized = image.resize(target_size)
        img_array = np.array(img_resized) / 255.0  # Normalize to [0,1]
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        with st.spinner("🤔 Analyzing image..."):
            preds = model.predict(img_array, verbose=0)
            
            # Show raw prediction for debugging (optional)
            with st.expander("🔍 View raw model output"):
                st.write("Model Output:", preds)

            # Interpret prediction
            pred_value = float(preds.flatten()[0])
            confidence = pred_value if pred_value > 0.5 else 1 - pred_value
            confidence_pct = confidence * 100

            # Display results with better formatting
            st.markdown("### 🎯 Prediction Results")
            
            if pred_value <= 0.4:
                st.success(f"🐱 **Cat** ({confidence_pct:.1f}% confidence)")
                st.balloons()
            elif pred_value >= 0.6:
                st.success(f"🐶 **Dog** ({confidence_pct:.1f}% confidence)")
                st.balloons()
            else:
                tendency = "Dog 🐶" if pred_value > 0.5 else "Cat 🐱"
                st.warning(f"🤷 Low confidence ({confidence_pct:.1f}%). Leaning towards: {tendency}")
                
            # Add confidence bar
            st.progress(confidence)

    except Exception as e:
        st.error(f"❌ Error processing image: {e}")
        st.info("💡 Try uploading a different image or ensure it's a clear photo of a cat or dog.")

elif model is None:
    st.warning("⚠️ Model not loaded. Please check if the model file exists in the repository.")
    
# Add some helpful information
st.markdown("---")
st.markdown("### ℹ️ About this app")
st.markdown("""
This app uses a Convolutional Neural Network (CNN) trained to classify images of cats and dogs.
- **Best results**: Upload clear, well-lit images with the animal as the main subject
- **Supported formats**: JPG, JPEG, PNG
- **Model confidence**: Higher percentages indicate more confident predictions
""")

st.markdown("### 🚀 How it works")
st.markdown("""
1. Upload an image using the file uploader above
2. The image is preprocessed and resized to match the model's input requirements
3. The trained CNN model analyzes the image features
4. The model outputs a prediction with confidence score
""")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and TensorFlow*")
