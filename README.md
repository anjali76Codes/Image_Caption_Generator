# Image Captioning Web Application

This project is a Flask web application that generates captions for uploaded images using the BLIP (Bootstrapped Language-Image Pretraining) model. It serves as a practical demonstration of concepts in data warehousing and data mining.

## Table of Contents

- [Project Description](#project-description)
- [Concepts in Data Warehousing and Data Mining](#concepts-in-data-warehousing-and-data-mining)
- [Installation](#installation)
- [Usage](#installation)


## Project Description

Users can upload images, and the application processes them to generate descriptive captions using a pre-trained machine learning model. The application utilizes Flask for the web interface, PIL for image handling, and Hugging Face's Transformers library for model inference.

## Concepts in Data Warehousing and Data Mining

This project integrates several key concepts:

- **Data Storage**: Uploaded images are stored systematically, simulating a data warehouse where structured data is crucial for analysis.

- **Data Processing**: Image preprocessing resembles data cleaning techniques, ensuring that raw data is transformed into a usable format.

- **Machine Learning**: The BLIP model applies supervised learning principles, utilizing labeled training data to generate captions based on input images.

- **Feature Extraction**: The model identifies and extracts features from images, similar to feature engineering in data mining.

- **User Interaction**: The application allows real-time interaction, enabling users to input data and receive insights, which is essential in data warehousing applications.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-captioning-flask.git
   cd image-captioning-flask


# Usage
Run the application:
python app.py

main installation :
pip install Flask Pillow torch torchvision transformers



# Installation :
1. python3 -m venv env
2. Get-ExecutionPolicy
3. Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

4. .\env\Scripts\Activate.ps1



# Run on this Url
# URL : http://127.0.0.1:5000/


Main installation :
# Step 1: Create a virtual environment
python -m venv env

# Step 2: Activate the environment (Windows)
env\Scripts\activate


# Step 3: Install all dependencies
pip install -r requirements.txt

# Step 4: Run the app
python app.py




for optimization installation
pip install celery redis

