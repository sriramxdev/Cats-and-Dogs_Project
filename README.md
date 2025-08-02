# 🐱🐶 Cats vs Dogs Classifier

A deep learning web application that classifies images of cats and dogs using a Convolutional Neural Network (CNN) built with TensorFlow and deployed on Streamlit Community Cloud.

## 🚀 Live Demo

[Try the app here!](your-streamlit-app-url) *(Update this URL after deployment)*

## 📖 About

This project uses a trained CNN model to classify uploaded images as either cats or dogs. The model achieves high accuracy and provides confidence scores for its predictions.

### Features
- 📸 Easy image upload interface
- 🤖 Real-time AI predictions
- 📊 Confidence score visualization
- 🎯 User-friendly results display
- 📱 Mobile-responsive design

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: TensorFlow/Keras
- **Image Processing**: PIL (Pillow)
- **Deployment**: Streamlit Community Cloud

## 📁 Project Structure

```
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── cats_dogs_model.h5         # Trained model (H5 format)
├── cats_dogs_savedmodel.keras  # Trained model (Keras format)
├── cats_and_dogs_CNN.ipynb    # Training notebook
└── README.md                   # Project documentation
```

## 🚀 Deployment on Streamlit Community Cloud

### Prerequisites
1. GitHub account
2. Streamlit Community Cloud account (free)

### Steps to Deploy

1. **Fork this repository** to your GitHub account

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Click "New app"**

4. **Connect your GitHub account** if not already connected

5. **Select your repository**: `your-username/Cats-and-Dogs_Project`

6. **Set the main file path**: `app.py`

7. **Click "Deploy"**

The app will automatically deploy and be available at a URL like: `https://your-username-cats-and-dogs-project-app-xxx.streamlit.app/`

### Important Notes for Streamlit Community Cloud

- ✅ **Free tier limitations**: 1GB RAM, shared CPU
- ✅ **Automatic dependency installation** from `requirements.txt`
- ✅ **Model files included** in repository (no upload needed)
- ✅ **Optimized with caching** for better performance
- ✅ **TensorFlow version** compatible with Streamlit Cloud

## 🔧 Local Development

### Setup
```bash
# Clone the repository
git clone https://github.com/your-username/Cats-and-Dogs_Project.git
cd Cats-and-Dogs_Project

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Testing
Upload test images of cats and dogs to verify the model predictions.

## 📊 Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Training Data**: Cats and Dogs dataset
- **Input Size**: 150x150 pixels (RGB)
- **Output**: Binary classification (0 = Cat, 1 = Dog)
- **Framework**: TensorFlow/Keras

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Streamlit Community Cloud](https://streamlit.io/cloud)

---

*Built with ❤️ using Streamlit and TensorFlow*
