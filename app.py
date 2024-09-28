from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load BLIP (Bootstrapped Language-Image Pretraining) image captioning model from Hugging Face
try:
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
    print("Model loaded successfully")
except Exception as e:
    print("Error loading model:", e)

# Function to preprocess the image (convert to PIL and prepare for model)
def preprocess_image(image_path):
    try:
        image = Image.open(image_path).convert('RGB')
        return image
    except Exception as e:
        print(f"Error in image preprocessing: {e}")
        return None

# Generate a caption using the BLIP model
def generate_caption(image_path):
    try:
        image = preprocess_image(image_path)
        if image is None:
            return "Error in image preprocessing"

        # Preprocess image for BLIP model
        inputs = processor(images=image, return_tensors="pt")
        pixel_values = inputs["pixel_values"]

        # Generate caption using BLIP model
        generated_ids = model.generate(pixel_values)
        caption = processor.decode(generated_ids[0], skip_special_tokens=True)
        
        if caption:
            return caption
        else:
            return "Unknown"
    
    except Exception as e:
        print(f"Error generating caption: {e}")
        return "Unknown"  # Return "Unknown" in case of error

# Route to display the home page and allow image upload
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part', 400
        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400
        if file and allowed_file(file.filename):
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Generate the caption using the model
            caption = generate_caption(file_path)

            return render_template('result.html', filename=filename, caption=caption)

    return render_template('index.html')

# Route to display the result with the image and its caption
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True)
