# Cat vs Dog Image Classifier

This project is a simple web app for classifying images as either a cat or a dog using a CNN Keras model. The app is built with Streamlit and allows users to upload their own model and test images through an interactive interface.

## Live Demo

The model is deployed on Hugging Face Spaces and can be tested here: [Cats and Dogs Classifier](https://huggingface.co/spaces/sriramxdev/Cats-and-Dogs-Classifier)

## Features
- Upload an image (`.jpg`, `.jpeg`, `.png`)
- Get instant predictions with confidence scores

## How to Run

1. **Download Files**
   - Download both `app.py` and your model file (e.g., `cats_dogs_savedmodel.keras`) into the same directory.

2. **Install Requirements**
   - Make sure you have Python installed.
   - Install the required packages:
     ```bash
     pip install streamlit tensorflow pillow numpy
     ```

3. **Run the App**
   - In your terminal, navigate to the project directory and run:
     ```bash
     streamlit run app.py
     ```

4. **Use the Interface**
   - In the Streamlit web interface:
     1. Upload your Keras model file (`.keras` or `.h5`).
     2. Upload an image of a cat or dog.
     3. View the prediction and confidence score.

## Notes
- The model should be trained for binary classification (cat vs dog) and accept images as input.
- The app normalizes images to the model's expected input size and scale.

---

**Author:** sriramxdev

