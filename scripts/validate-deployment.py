#!/usr/bin/env python3
"""Validate deployment configuration"""
import sys
import os
from pathlib import Path

def check_env_vars():
    required = ['GEMINI_API_KEY']
    missing = [var for var in required if not os.getenv(var)]
    if missing:
        print(f"Missing environment variables: {missing}")
        return False
    return True

def check_dependencies():
    try:
        import librosa
        import google.generativeai
        print("✓ All critical dependencies imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

if __name__ == "__main__":
    checks = [
        ("Environment Variables", check_env_vars),
        ("Dependencies", check_dependencies),
    ]
    
    all_passed = True
    for name, check in checks:
        print(f"\nChecking {name}...")
        if not check():
            all_passed = False
    
    sys.exit(0 if all_passed else 1)
