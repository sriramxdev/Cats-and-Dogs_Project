import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Suppress TensorFlow warnings

import streamlit as st

# Try to import TensorFlow with error handling
try:
    import tensorflow as tf
    # Disable GPU if available to avoid memory issues on Streamlit Cloud
    tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('GPU')[0], True) if tf.config.list_physical_devices('GPU') else None
    TF_AVAILABLE = True
except ImportError as e:
    st.error(f"TensorFlow import failed: {e}")
    TF_AVAILABLE = False
except Exception as e:
    st.warning(f"TensorFlow setup warning: {e}")
    TF_AVAILABLE = True

from PIL import Image
import numpy as np

# Only proceed if TensorFlow is available
if not TF_AVAILABLE:
    st.error("❌ TensorFlow is not available. Please check the deployment configuration.")
    st.stop()

# Configure page
st.set_page_config(
    page_title="Cats vs Dogs Classifier",
    page_icon="🐱🐶",
    layout="centered"
)

# Custom CSS for Material Design theme
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Custom card styling */
    .info-card {
        background-color: #F5F5F5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Upload area styling */
    .uploadedFile {
        border: 2px dashed #2196F3;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        background-color: #FAFAFA;
    }
    
    /* Success/Error message styling */
    .stSuccess, .stError, .stWarning {
        border-radius: 10px;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background-color: #2196F3;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 20px;
        border: none;
        background-color: #2196F3;
        color: white;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1976D2;
        box-shadow: 0 4px 8px rgba(33, 150, 243, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.title("🐱🐶 Cats vs Dogs Classifier")
st.markdown("Upload an image and let our AI model predict whether it's a cat or a dog!")

# Author information
st.markdown("""
<div style="text-align: center; padding: 10px; margin: 20px 0; background-color: #F5F5F5; border-radius: 10px; border-left: 4px solid #2196F3;">
    <p style="margin: 0; color: #666; font-size: 0.9em;">
        🚀 <strong>Created by:</strong> <a href="https://github.com/sriramxdev" target="_blank" style="color: #2196F3; text-decoration: none;">Sriram</a> | 
        <em>Deep Learning Enthusiast</em>
    </p>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the pre-trained model with caching for better performance"""
    try:
        # Load the .keras model (recommended format)
        model_path = "cats_dogs_savedmodel.keras"
        if os.path.exists(model_path):
            with st.spinner("Loading AI model..."):
                # Load with additional error handling for TensorFlow compatibility
                model = tf.keras.models.load_model(
                    model_path,
                    compile=False  # Skip compilation to avoid potential issues
                )
                # Recompile with basic settings
                model.compile(
                    optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy']
                )
            st.success("✅ Model loaded successfully!")
            return model
        else:
            st.error("❌ Model file not found. Please ensure the model file is in the repository.")
            return None
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.info("💡 This might be due to TensorFlow version compatibility. Try refreshing the page.")
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

# About section with material design card
st.markdown("""
<div class="info-card">
    <h3 style="color: #2196F3; margin-top: 0;">ℹ️ About this app</h3>
    <p>This app uses a Convolutional Neural Network (CNN) trained to classify images of cats and dogs.</p>
    <ul style="margin-bottom: 0;">
        <li><strong>Best results:</strong> Upload clear, well-lit images with the animal as the main subject</li>
        <li><strong>Supported formats:</strong> JPG, JPEG, PNG</li>
        <li><strong>Model confidence:</strong> Higher percentages indicate more confident predictions</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# How it works section with material design card
st.markdown("""
<div class="info-card">
    <h3 style="color: #2196F3; margin-top: 0;">🚀 How it works</h3>
    <ol style="margin-bottom: 0;">
        <li>Upload an image using the file uploader above</li>
        <li>The image is preprocessed and resized to match the model's input requirements</li>
        <li>The trained CNN model analyzes the image features</li>
        <li>The model outputs a prediction with confidence score</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 15px; margin-top: 30px; background-color: #F5F5F5; border-radius: 10px;">
    <p style="margin: 0; color: #666; font-size: 0.9em;">
        💻 <strong>Built with</strong> <span style="color: #2196F3;">Streamlit</span> & <span style="color: #2196F3;">TensorFlow</span> | 
        ⭐ <a href="https://github.com/sriramxdev/Cats-and-Dogs_Project" target="_blank" style="color: #2196F3; text-decoration: none;">Star on GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)
