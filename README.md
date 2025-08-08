# 🍃 Leaf Counter AI - Retro Edition

A whimsical AI/ML application that counts leaves from tree images with variable accuracy based on the AI's "mood". Features a beautiful retro-style interface with sage green accents.

## 🌟 Features

- **AI-Powered Leaf Counting**: Uses computer vision techniques to detect and count leaves in tree images
- **Mood-Based Accuracy**: AI accuracy varies from 5% to 90% based on its current mood
- **Retro UI Design**: Inspired by classic operating systems with modern sage green accents
- **Real-time Processing**: Live progress indicators and status updates
- **Drag & Drop Support**: Easy image upload with drag and drop functionality
- **Responsive Design**: Works on desktop and mobile devices

## 🎭 AI Moods & Accuracy

| Mood | Accuracy Range | Emoji |
|------|----------------|-------|
| Excellent | 85-95% | 😊 |
| Good | 70-85% | 🙂 |
| Neutral | 50-70% | 😐 |
| Bad | 25-50% | 😕 |
| Terrible | 5-25% | 😫 |

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone or Download

Download all files to your local directory.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

### Step 4: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
useless3/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main UI template
└── uploads/              # Uploaded images (created automatically)
```

## 🎮 How to Use

1. **Upload an Image**: Click "📂 Choose Image File" or drag and drop a tree image
2. **Set AI Mood**: Choose the AI's mood using the mood selector buttons
3. **Analyze**: Click "🔍 Analyze Leaves" to start the counting process
4. **View Results**: See the leaf count, confidence level, and processing details

## 🔧 Technical Details

### Backend (Flask)
- **Image Processing**: Uses OpenCV for computer vision operations
- **Leaf Detection**: Combines edge detection, color segmentation, and contour analysis
- **Mood System**: Random mood changes affect processing accuracy
- **File Handling**: Secure file upload with timestamp-based naming

### Frontend (HTML/CSS/JavaScript)
- **Retro Design**: Classic window-style interface with drop shadows and gradients
- **Sage Green Theme**: Custom color palette with #556B2F, #90EE90, and related shades
- **Interactive Elements**: Hover effects, progress bars, and animated loading
- **Responsive Layout**: Adapts to different screen sizes

### AI/ML Components
- **Computer Vision**: OpenCV-based image analysis
- **Color Segmentation**: HSV color space for green leaf detection
- **Contour Analysis**: Shape-based leaf identification
- **Accuracy Simulation**: Mood-based accuracy variation system

## 🎨 UI Design Features

- **Retro Window Style**: Classic title bars, close buttons, and drop shadows
- **Sage Green Accents**: Primary color scheme using various shades of sage green
- **Gradient Backgrounds**: Subtle gradients for depth and visual appeal
- **Monospace Font**: Courier New for that authentic retro feel
- **Interactive Buttons**: Hover effects and active states
- **Progress Indicators**: Animated loading spinners and progress bars

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Change port in app.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Missing Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Image Upload Issues**
   - Ensure image is in supported format (PNG, JPG, JPEG, GIF, BMP)
   - Check file size (max 16MB)
   - Verify image contains visible tree/leaf content

### Supported Image Formats
- PNG
- JPG/JPEG
- GIF
- BMP

## 🎯 Future Enhancements

- [ ] Machine Learning model training for better accuracy
- [ ] Batch processing for multiple images
- [ ] Export results to CSV/PDF
- [ ] Advanced mood algorithms
- [ ] Mobile app version
- [ ] Cloud deployment options

## 📝 License

This project is created for educational and entertainment purposes. Feel free to modify and use as needed.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application!

---

**Note**: This is a demonstration application. The leaf counting accuracy is simulated and varies based on the AI's "mood" for entertainment purposes. For production use, consider implementing more sophisticated computer vision or machine learning models.
