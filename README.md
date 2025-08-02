# 🐱🐶 Cats vs Dogs Classifier

A comprehensive deep learning project that demonstrates image classification using Convolutional Neural Networks (CNN). This project includes a complete machine learning pipeline from data preprocessing to model deployment, featuring a trained CNN model that accurately classifies images of cats and dogs.

## 🚀 Live Demo

[Try the app here!](your-streamlit-app-url) *(Update this URL after deployment)*

## 📖 About

This project showcases the complete workflow of building an image classification system:

- **Data Processing**: Downloads and organizes the Microsoft Cats and Dogs dataset (25,000 images)
- **Model Architecture**: Custom CNN with convolutional layers, pooling, and dropout for regularization
- **Training Pipeline**: Includes data augmentation, early stopping, and learning rate scheduling
- **Model Evaluation**: Comprehensive evaluation with confusion matrix and classification reports
- **Web Deployment**: Interactive Streamlit web application for real-time predictions

The trained model achieves high accuracy in distinguishing between cats and dogs and provides confidence scores for predictions.

### Features
- 📸 Easy image upload interface
- 🤖 Real-time AI predictions with confidence scores
- 📊 Confidence score visualization with progress bars
- 🎯 Clean, user-friendly results display
- 📱 Mobile-responsive design
- 👨‍💻 Author attribution and GitHub integration

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: TensorFlow/Keras
- **Image Processing**: PIL (Pillow), OpenCV
- **Data Analysis**: NumPy, Pandas, Matplotlib, Seaborn
- **Deployment**: Streamlit Community Cloud

## 📁 Project Structure

```
├── app.py                      # Streamlit web application
├── requirements.txt            # Python dependencies
├── cats_dogs_savedmodel.keras  # Trained CNN model
├── cats_and_dogs_CNN.ipynb    # Complete training pipeline notebook
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
- **Dataset**: Microsoft Cats and Dogs dataset (25,000 images)
- **Input Size**: 150x150 pixels (RGB)
- **Output**: Binary classification (0 = Cat, 1 = Dog)
- **Framework**: TensorFlow/Keras
- **Training Features**: Data augmentation, early stopping, learning rate scheduling

## 📓 Jupyter Notebook

The `cats_and_dogs_CNN.ipynb` notebook contains the complete machine learning pipeline:

1. **Data Download & Preparation**: Automated dataset download and organization
2. **Data Visualization**: Sample images and dataset statistics
3. **Data Preprocessing**: Image augmentation and generator setup
4. **Model Architecture**: Custom CNN design with multiple layers
5. **Model Training**: Training with callbacks and monitoring
6. **Model Evaluation**: Performance metrics and confusion matrix
7. **Prediction Visualization**: Test predictions with confidence scores
8. **Model Saving**: Export trained model in multiple formats

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
