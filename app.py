import os
import warnings
import sys

# === FORCE CPU-ONLY MODE ===
os.environ['CUDA_VISIBLE_DEVICES'] = '-1' 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  
warnings.filterwarnings('ignore')

import gradio as gr
import numpy as np
import time
import tensorflow as tf
from tensorflow import keras
from PIL import Image

# Force TF into CPU mode explicitly
try:
    tf.config.set_visible_devices([], 'GPU')
except:
    pass

# Load the trained model
model = keras.models.load_model("cats_dogs_savedmodel.keras")

class_names = ["Cat", "Dog"]

def predict(image):
    start_time = time.time()
    
    # Convert PIL Image to numpy array and resize to model input
    img = image.convert("RGB").resize((150, 150))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Silent inference on CPU
    preds = model.predict(img_array, verbose=0)
    
    if preds.shape[-1] == 1:
        # Binary classification (sigmoid)
        pred_class = int(preds[0][0] > 0.5)
        confidence = float(preds[0][0]) if pred_class == 1 else 1 - float(preds[0][0])
    else:
        # Softmax output
        pred_class = np.argmax(preds[0])
        confidence = float(np.max(preds[0]))
    
    # Get raw scores for display
    if preds.shape[-1] == 1:
        dog_score = float(preds[0][0])
        cat_score = 1 - dog_score
    else:
        dog_score = float(preds[0][1])
        cat_score = float(preds[0][0])
    
    elapsed_time = round((time.time() - start_time) * 1000, 2)
    
    # Format prediction text with emoji
    pred_label = class_names[pred_class]
    emoji = "🐱" if pred_label == "Cat" else "🐶"
    
    return {
        "prediction": f"{emoji} {pred_label}",
        "confidence": confidence,
        "cat_score": round(cat_score * 100, 2),
        "dog_score": round(dog_score * 100, 2),
        "time_taken": elapsed_time,
        "raw_prediction": pred_label,
        "raw_confidence": confidence
    }

# Optimized layout configuration for Full-Screen Width & Horizontal Stability
CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Quicksand:wght@500;700&display=swap');
body, .gradio-container {
    background-color: #0e0e0e !important;
    font-family: "Inter", sans-serif !important;
}
/* Fix 2: Stretches the interface to utilize the whole available screen size */
.gradio-container {
    max-width: 96% !important;
    width: 96% !important;
    margin: 0 auto !important;
    padding: 30px 0 !important;
}
.header {
    text-align: center !important;
    margin-bottom: 35px !important;
}
.header h1 {
    font-family: "Quicksand", sans-serif !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    font-size: 3rem !important;
    letter-spacing: -0.5px !important;
    margin-bottom: 10px !important;
}
.header p {
    color: rgba(255, 255, 255, 0.5) !important;
    font-size: 1.1rem !important;
    font-weight: 300 !important;
    max-width: 600px !important;
    margin: 0 auto !important;
    line-height: 1.6 !important;
}
/* Fix 1: Enforces a strict, unshakeable horizontal split structure */
.app-layout {
    display: flex !important;
    flex-direction: row !important;
    gap: 30px !important;
    width: 100% !important;
    align-items: stretch !important;
}
.upload-panel {
    flex: 1 !important;
    min-width: 45% !important;
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 24px !important;
    padding: 30px !important;
}
.results-panel {
    flex: 1 !important;
    min-width: 45% !important;
    background: linear-gradient(145deg, #131324, #0d1326) !important;
    border-radius: 24px !important;
    padding: 30px !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6) !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    min-height: 460px !important; /* Locks layout height to match upload area precisely */
}
.btn-predict {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 14px !important;
    border-radius: 14px !important;
    font-size: 1.05rem !important;
    transition: all 0.25s ease !important;
    margin-top: 20px !important;
}
.btn-predict:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.35) !important;
}
.btn-clear {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: rgba(255, 255, 255, 0.6) !important;
    font-weight: 500 !important;
    padding: 14px !important;
    border-radius: 14px !important;
    transition: all 0.25s ease !important;
    margin-top: 10px !important;
}
.btn-clear:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #ffffff !important;
}
.ring-container {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
}
.ring-wrapper {
    position: relative !important;
    width: 200px !important;
    height: 200px !important;
}
.ring-svg {
    transform: rotate(-90deg) !important;
    width: 200px !important;
    height: 200px !important;
}
.ring-bg {
    fill: none !important;
    stroke: rgba(255, 255, 255, 0.04) !important;
    stroke-width: 12 !important;
}
.ring-progress {
    fill: none !important;
    stroke: url(#gradient) !important;
    stroke-width: 12 !important;
    stroke-linecap: round !important;
    transition: stroke-dashoffset 0.8s ease-out !important;
}
.ring-center-text {
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    text-align: center !important;
}
.ring-percentage {
    font-size: 2.8rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    line-height: 1.1 !important;
}
.ring-label {
    font-size: 0.8rem !important;
    color: rgba(255, 255, 255, 0.4) !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
.prediction-label {
    font-family: "Quicksand", sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    text-align: center !important;
    margin: 20px 0 !important;
    color: #ffffff !important;
}
.stats-grid {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 14px !important;
    width: 100% !important;
}
.stat-item {
    background: rgba(255, 255, 255, 0.03) !important;
    border-radius: 14px !important;
    padding: 14px !important;
    text-align: center !important;
    border: 1px solid rgba(255, 255, 255, 0.04) !important;
}
.stat-value {
    font-size: 1.15rem !important;
    font-weight: 600 !important;
    color: #ffffff !important;
}
.stat-label {
    font-size: 0.7rem !important;
    color: rgba(255, 255, 255, 0.4) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    margin-top: 5px !important;
}
.placeholder-wrapper {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    height: 100% !important;
    width: 100% !important;
}
/* High-Visibility Custom Colored Footer */
.footer {
    text-align: center !important;
    color: rgba(255, 255, 255, 0.75) !important; 
    font-size: 0.95rem !important;              
    margin-top: 60px !important;
    padding: 20px !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
}
.footer a {
    color: #8a9eff !important; /* Bright colored accent link */
    font-weight: 600 !important;
    text-decoration: none !important;
}
.footer a:hover {
    color: #a3b4ff !important;
    text-decoration: underline !important;
}
/* Clean collapsing rules strictly reserved for smaller mobile displays */
@media (max-width: 900px) {
    .app-layout {
        flex-direction: column !important;
    }
    .stats-grid {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
    }
}
"""

def format_output(pred_data):
    if pred_data is None:
        return '''
        <div class="placeholder-wrapper">
            <span style="font-size:4.5rem; opacity:0.3; display:block; margin-bottom:15px;">📸</span>
            <span style="color:rgba(255,255,255,0.35); font-size:1.1rem; font-weight:400; text-align:center;">
                Upload an image to see results
            </span>
        </div>
        '''
    
    confidence = pred_data.get("confidence", 0)
    cat_score = pred_data.get("cat_score", 0)
    dog_score = pred_data.get("dog_score", 0)
    time_taken = pred_data.get("time_taken", 0)
    raw_class = pred_data.get("raw_prediction", "Cat")
    
    circumference = 565.48
    offset = circumference - (confidence * circumference)
    confidence_pct = confidence * 100
    
    emoji = "🐱" if raw_class == "Cat" else "🐶"
    
    return f'''
    <div class="ring-container">
        <div class="ring-wrapper">
            <svg class="ring-svg" viewBox="0 0 200 200">
                <defs>
                    <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
                    </linearGradient>
                </defs>
                <circle class="ring-bg" cx="100" cy="100" r="90" />
                <circle class="ring-progress" cx="100" cy="100" r="90" 
                        stroke-dashoffset="{offset}" 
                        style="stroke-dasharray: 565.48;" />
                </svg>
            <div class="ring-center-text">
                <div class="ring-percentage">{confidence_pct:.1f}%</div>
                <div class="ring-label">Confidence</div>
            </div>
        </div>
    </div>
    
    <div class="prediction-label">
        {emoji} {raw_class}
    </div>
    
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-value">🐱 {cat_score:.1f}%</div>
            <div class="stat-label">Cat Score</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">🐶 {dog_score:.1f}%</div>
            <div class="stat-label">Dog Score</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">{time_taken} ms</div>
            <div class="stat-label">Speed</div>
        </div>
    </div>
    '''

with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo"), 
               title="Cats vs Dogs Classifier",
               css=CUSTOM_CSS) as demo:
    
    gr.HTML("""
    <div class="header">
        <h1>🐱 vs 🐶 CNN Classifier</h1>
        <p>Upload an image of a cat or dog and the model will predict which it is.<br>
        Built from scratch with 4-layer CNN achieving <strong>89% accuracy</strong></p>
    </div>
    """)
    
    # Grid Row utilizing unshakeable inline-flex parameters
    with gr.Row(elem_classes="app-layout"):
        with gr.Column(elem_classes="upload-panel"):
            input_image = gr.Image(type="pil", label="Upload Image")
            submit_btn = gr.Button("🔍 Predict", variant="primary", elem_classes="btn-predict")
            clear_btn = gr.Button("🗑️ Clear", variant="secondary", elem_classes="btn-clear")
        
        with gr.Column(elem_classes="results-panel"):
            output_html = gr.HTML(value=format_output(None))
    
    submit_btn.click(
        fn=lambda img: format_output(predict(img)) if img is not None else format_output(None),
        inputs=input_image,
        outputs=output_html
    )
    
    clear_btn.click(
        fn=lambda: (None, format_output(None)),
        inputs=None,
        outputs=[input_image, output_html]
    )
    
    gr.HTML("""
    <div class="footer">
        Created by Sri Ram Sharma (<a href="https://sriramxdev.me" target="_blank">sriramxdev.me</a>).
    </div>
    """)

if __name__ == "__main__":
    demo.launch(ssr_mode=False)
