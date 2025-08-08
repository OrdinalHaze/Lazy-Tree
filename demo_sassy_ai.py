#!/usr/bin/env python3
"""
Demo script to showcase the sassy AI features
"""

from app import LeafCounterAI
import random

def demo_sassy_ai():
    """Demonstrate the sassy AI features"""
    
    print("🍃 Leaf Counter AI - Sassy Demo")
    print("=" * 50)
    
    # Initialize the AI
    ai = LeafCounterAI()
    
    # Demo different moods
    moods = ["excellent", "good", "neutral", "bad", "terrible"]
    
    print("🤖 Let's see how sassy our AI can be in different moods!\n")
    
    for mood in moods:
        print(f"🎭 Testing {mood.upper()} mood:")
        print("-" * 30)
        
        # Set the mood
        ai.set_mood(mood)
        
        # Get a sassy comment
        comment = ai.get_sassy_comment()
        print(f"AI says: {comment}")
        
        # Show accuracy range
        accuracy_range = ai.mood_accuracy_map[mood]
        print(f"Accuracy range: {accuracy_range[0]}% - {accuracy_range[1]}%")
        
        print()
    
    print("🎉 Demo complete! The AI is ready to be sassy with your tree images!")
    print("\nTo try it yourself:")
    print("1. Run: python app.py")
    print("2. Open: http://localhost:5000")
    print("3. Upload a tree image and watch the AI's mood change!")

if __name__ == "__main__":
    demo_sassy_ai()
