from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

# Import your model
from model import predict_image

print("Flask app starting...")

app = Flask(__name__)

# -------------------------------
# Upload folder setup
# -------------------------------
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# -------------------------------
# Route to serve uploaded images
# -------------------------------
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# -------------------------------
# Home route
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------------
# Prediction route
# -------------------------------
@app.route('/predict', methods=['POST'])
def predict():

    # Check if file is present
    if 'file' not in request.files:
        return redirect(url_for('home'))

    file = request.files['file']

    # If no file selected
    if file.filename == '':
        return redirect(url_for('home'))

    # Save uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Run prediction
    result, confidence = predict_image(filepath)

    # Send result + image name to frontend
    return render_template(
        'index.html',
        prediction=result,
        confidence=round(confidence * 100, 2),
        image_name=file.filename
    )

# -------------------------------
# Run app
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)