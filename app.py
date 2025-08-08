import os
import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import random
import time
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class LeafCounterAI:
    def __init__(self):
        self.mood = "neutral"
        self.mood_accuracy_map = {
            "excellent": (85, 95),
            "good": (70, 85),
            "neutral": (50, 70),
            "bad": (25, 50),
            "terrible": (5, 25)
        }
    
    def set_mood(self, mood):
        """Set the AI's mood which affects accuracy"""
        self.mood = mood
    
    def get_random_mood(self):
        """Randomly change the AI's mood"""
        moods = list(self.mood_accuracy_map.keys())
        self.mood = random.choice(moods)
        return self.mood
    
    def count_leaves(self, image_path):
        """Count leaves in an image with variable accuracy based on mood"""
        try:
            # Load image
            image = cv2.imread(image_path)
            if image is None:
                return {"error": "Could not load image"}
            
            # Convert to different color spaces for analysis
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            
            # Get image dimensions
            height, width = gray.shape
            total_pixels = height * width
            
            # Simulate leaf detection with computer vision techniques
            # This is a simplified approach - in a real application, you'd use more sophisticated ML models
            
            # 1. Edge detection
            edges = cv2.Canny(gray, 50, 150)
            
            # 2. Color-based segmentation for green areas (leaves)
            lower_green = np.array([35, 50, 50])
            upper_green = np.array([85, 255, 255])
            green_mask = cv2.inRange(hsv, lower_green, upper_green)
            
            # 3. Contour detection
            contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Filter contours by area to identify potential leaves
            min_contour_area = 100
            max_contour_area = 5000
            leaf_contours = [cnt for cnt in contours if min_contour_area < cv2.contourArea(cnt) < max_contour_area]
            
            # Base leaf count from contours
            base_leaf_count = len(leaf_contours)
            
            # Apply mood-based accuracy variation
            accuracy_range = self.mood_accuracy_map[self.mood]
            accuracy_factor = random.uniform(accuracy_range[0], accuracy_range[1]) / 100
            
            # Add some randomness to make it more realistic
            noise_factor = random.uniform(0.8, 1.2)
            
            # Calculate final leaf count with mood-based accuracy
            final_leaf_count = int(base_leaf_count * accuracy_factor * noise_factor)
            
            # Ensure we don't return negative counts
            final_leaf_count = max(0, final_leaf_count)
            
            # Generate confidence score based on mood
            confidence = random.uniform(accuracy_range[0], accuracy_range[1])
            
            return {
                "leaf_count": final_leaf_count,
                "confidence": round(confidence, 1),
                "mood": self.mood,
                "base_count": base_leaf_count,
                "image_size": f"{width}x{height}",
                "processing_time": round(random.uniform(0.5, 3.0), 2)
            }
            
        except Exception as e:
            return {"error": f"Error processing image: {str(e)}"}

# Initialize the AI
ai_model = LeafCounterAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Randomly change AI mood for each request
        current_mood = ai_model.get_random_mood()
        
        # Process the image
        result = ai_model.count_leaves(filepath)
        
        if 'error' not in result:
            result['filename'] = filename
            result['upload_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return jsonify(result)
    
    return jsonify({'error': 'Invalid file type'})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/mood', methods=['POST'])
def set_mood():
    data = request.get_json()
    mood = data.get('mood', 'neutral')
    ai_model.set_mood(mood)
    return jsonify({'mood': mood, 'message': f'AI mood set to {mood}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
