import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import tempfile

st.title("Keras Model Image Tester")

# Upload model file
model_file = st.file_uploader("Upload your Keras model (.h5 or .keras)", type=["h5", "keras"])
# Upload image file
image_file = st.file_uploader("Upload an image to test", type=["jpg", "jpeg", "png"])

if model_file and image_file:
    try:
        # Determine correct suffix for temp file
        if model_file.name.endswith(".keras"):
            suffix = ".keras"
        else:
            suffix = ".h5"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(model_file.read())
            tmp_path = tmp.name
        with st.spinner("Loading model..."):
            model = tf.keras.models.load_model(tmp_path)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

    try:
        image = Image.open(image_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        input_shape = model.input_shape
        target_size = input_shape[1:3]
        img_resized = image.resize(target_size)
        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        with st.spinner("Running prediction..."):
            preds = model.predict(img_array)
            st.write("Model Output:", preds)

            # Interpret prediction
            pred_value = float(preds.flatten()[0])
            confidence = pred_value if pred_value > 0.5 else 1 - pred_value
            confidence_pct = confidence * 100

            if pred_value <= 0.4:
                label = "Cat"
                st.success(f"Prediction: Cat ({confidence_pct:.2f}% confidence)")
            elif pred_value >= 0.6:
                label = "Dog"
                st.success(f"Prediction: Dog ({confidence_pct:.2f}% confidence)")
            else:
                tendency = "Dog" if pred_value > 0.5 else "Cat"
                st.warning(f"Low confidence ({confidence_pct:.2f}%). Tending towards: {tendency}")

    except Exception as e:
        st.error(f"Error processing image or running prediction: {e}")