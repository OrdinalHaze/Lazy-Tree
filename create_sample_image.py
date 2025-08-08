#!/usr/bin/env python3
"""
Create a sample tree image for testing the Leaf Counter AI
"""

import numpy as np
from PIL import Image, ImageDraw
import os

def create_sample_tree_image():
    """Create a simple tree image with green leaves for testing"""
    
    # Create a blank image with sky blue background
    width, height = 400, 500
    image = Image.new('RGB', (width, height), (135, 206, 235))  # Sky blue
    
    draw = ImageDraw.Draw(image)
    
    # Draw ground
    draw.rectangle([0, 400, width, height], fill=(34, 139, 34))  # Forest green
    
    # Draw tree trunk
    trunk_color = (139, 69, 19)  # Saddle brown
    trunk_width = 40
    trunk_x = width // 2 - trunk_width // 2
    draw.rectangle([trunk_x, 300, trunk_x + trunk_width, 400], fill=trunk_color)
    
    # Draw tree leaves (multiple green circles)
    leaf_colors = [
        (34, 139, 34),   # Forest green
        (50, 205, 50),   # Lime green
        (0, 128, 0),     # Green
        (85, 107, 47),   # Dark olive green
        (107, 142, 35),  # Olive drab
    ]
    
    # Create multiple leaf clusters
    leaf_positions = [
        (200, 200, 60),   # Main cluster
        (150, 180, 40),   # Left cluster
        (250, 180, 40),   # Right cluster
        (180, 150, 35),   # Top left
        (220, 150, 35),   # Top right
        (200, 120, 30),   # Top center
        (130, 220, 25),   # Lower left
        (270, 220, 25),   # Lower right
    ]
    
    for x, y, size in leaf_positions:
        color = leaf_colors[np.random.randint(0, len(leaf_colors))]
        # Draw multiple smaller circles to simulate individual leaves
        for i in range(8):
            offset_x = np.random.randint(-size//2, size//2)
            offset_y = np.random.randint(-size//2, size//2)
            leaf_size = np.random.randint(8, 15)
            draw.ellipse([
                x + offset_x - leaf_size//2,
                y + offset_y - leaf_size//2,
                x + offset_x + leaf_size//2,
                y + offset_y + leaf_size//2
            ], fill=color)
    
    # Add some texture to the trunk
    for i in range(10):
        x = trunk_x + np.random.randint(0, trunk_width)
        y = 300 + np.random.randint(0, 100)
        draw.line([x, y, x, y + 2], fill=(101, 67, 33), width=1)
    
    # Save the image
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    filename = 'uploads/sample_tree.png'
    image.save(filename)
    print(f"✅ Sample tree image created: {filename}")
    print(f"📏 Image size: {width}x{height} pixels")
    print("🌳 This image contains multiple green leaf clusters for testing")
    
    return filename

if __name__ == "__main__":
    create_sample_tree_image()
