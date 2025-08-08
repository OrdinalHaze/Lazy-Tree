#!/usr/bin/env python3
"""
Test script to verify Leaf Counter AI setup
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'flask',
        'cv2',
        'numpy',
        'PIL',
        'skimage',
        'matplotlib',
        'werkzeug'
    ]
    
    print("🔍 Testing package imports...")
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Please run: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_flask_app():
    """Test if Flask app can be created"""
    try:
        from app import app
        print("✅ Flask app created successfully!")
        return True
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def test_ai_model():
    """Test if AI model can be initialized"""
    try:
        from app import LeafCounterAI
        ai = LeafCounterAI()
        print("✅ AI model initialized successfully!")
        
        # Test mood setting
        ai.set_mood("excellent")
        print(f"✅ Mood setting works: {ai.mood}")
        
        return True
    except Exception as e:
        print(f"❌ AI model initialization failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🍃 Leaf Counter AI - Setup Test")
    print("=" * 40)
    
    # Test Python version
    print(f"🐍 Python version: {sys.version}")
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test Flask app
        flask_ok = test_flask_app()
        
        # Test AI model
        ai_ok = test_ai_model()
        
        if flask_ok and ai_ok:
            print("\n🎉 All tests passed! You can now run the application.")
            print("Run: python app.py")
            print("Then open: http://localhost:5000")
        else:
            print("\n❌ Some tests failed. Please check the errors above.")
    else:
        print("\n❌ Import tests failed. Please install dependencies first.")

if __name__ == "__main__":
    main()
