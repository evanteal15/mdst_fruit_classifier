from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import cv2
import ast
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    """
    TODO: Implement a fruit classification endpoint that:
    1. Accepts an image file
    2. Preprocesses the image
    3. Makes a prediction using the model
    4. Returns the predicted fruit with confidence score
    """
    
    # TODO: Check if image is provided in the request
    # Return error if no image is found
    if 'image' not in request.files:
        return jsonify({'error': 'No image found'}), 400
    
    # TODO: Read and decode the image
    # Hint: Use request.files, cv2.imdecode
    image_file = request.files['image']
    image_bytes = np.frombuffer(image_file.read(), np.uint8)
    file = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    
    # TODO: Preprocess the image
    # 1. Resize to 100x100
    # 2. Convert BGR to RGB
    # 3. Normalize pixel values to [0,1]
    file = cv2.resize(file, (100, 100))
    file = cv2.cvtColor(file, cv2.COLOR_BGR2RGB)
    file = file / 255.0
    
    # TODO: Load the model
    # Hint: Use try-except for error handling
    try:
        model = tf.keras.models.load_model('Backend/fruit_classifier.keras')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # TODO: Make prediction
    # Hint: Use model.predict() and handle exceptions
    
    # TODO: Get top 5 predictions
    # Hint: Use np.argsort()
    
    # TODO: Load fruits dictionary from 'Backend/directories.txt'
    # Hint: Use ast.literal_eval()
    
    # TODO: Return prediction
    # Format: {
    #   'fruit': fruit_name,
    #   'confidence': confidence_score,
    #   'class_id': class_id
    # }
    
    pass  # Remove this line when implementing the function

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)


