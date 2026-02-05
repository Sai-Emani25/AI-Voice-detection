#!/usr/bin/env python3
"""
Post-Deployment Verification Script

Tests your deployed application to ensure everything is working correctly.
Usage: python scripts/verify-deployment.py <deployment-url>
Example: python scripts/verify-deployment.py https://my-app.vercel.app
"""

import sys
import requests
import json
from typing import Dict, List, Tuple

def test_health_endpoint(base_url: str) -> Tuple[bool, str]:
    """Test the health endpoint"""
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "healthy":
                return True, "✓ Health endpoint working"
            else:
                return False, f"✗ Health endpoint returned unexpected data: {data}"
        else:
            return False, f"✗ Health endpoint returned {response.status_code}"
    except Exception as e:
        return False, f"✗ Health endpoint failed: {str(e)}"

def test_root_endpoint(base_url: str) -> Tuple[bool, str]:
    """Test the root endpoint"""
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            return True, "✓ Root endpoint accessible"
        else:
            return False, f"✗ Root endpoint returned {response.status_code}"
    except Exception as e:
        return False, f"✗ Root endpoint failed: {str(e)}"

def test_docs_endpoint(base_url: str) -> Tuple[bool, str]:
    """Test the API documentation endpoint"""
    try:
        response = requests.get(f"{base_url}/docs", timeout=10)
        if response.status_code == 200:
            return True, "✓ API documentation accessible"
        else:
            return False, f"✗ API docs returned {response.status_code}"
    except Exception as e:
        return False, f"✗ API docs failed: {str(e)}"

def test_openapi_schema(base_url: str) -> Tuple[bool, str]:
    """Test the OpenAPI schema endpoint"""
    try:
        response = requests.get(f"{base_url}/openapi.json", timeout=10)
        if response.status_code == 200:
            schema = response.json()
            if "info" in schema and "paths" in schema:
                return True, f"✓ OpenAPI schema valid (version {schema['info'].get('version', 'unknown')})"
            else:
                return False, "✗ OpenAPI schema incomplete"
        else:
            return False, f"✗ OpenAPI schema returned {response.status_code}"
    except Exception as e:
        return False, f"✗ OpenAPI schema failed: {str(e)}"

def test_app_endpoint(base_url: str) -> Tuple[bool, str]:
    """Test the web app endpoint"""
    try:
        response = requests.get(f"{base_url}/app", timeout=10)
        if response.status_code == 200:
            return True, "✓ Web app accessible"
        else:
            return False, f"✗ Web app returned {response.status_code}"
    except Exception as e:
        return False, f"✗ Web app failed: {str(e)}"

def verify_deployment(base_url: str) -> bool:
    """Run all verification tests"""
    
    # Ensure URL doesn't end with /
    base_url = base_url.rstrip('/')
    
    print(f"\n{'='*60}")
    print(f"Verifying Deployment: {base_url}")
    print(f"{'='*60}\n")
    
    tests = [
        ("Health Check", test_health_endpoint),
        ("Root Endpoint", test_root_endpoint),
        ("API Documentation", test_docs_endpoint),
        ("OpenAPI Schema", test_openapi_schema),
        ("Web Application", test_app_endpoint),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Testing {test_name}...")
        success, message = test_func(base_url)
        results.append(success)
        print(f"  {message}")
    
    print(f"\n{'='*60}")
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    print(f"{'='*60}\n")
    
    if passed == total:
        print("🎉 All tests passed! Your deployment is working correctly.\n")
        print("Next steps:")
        print("  1. Test the /detect endpoint with actual audio")
        print("  2. Monitor logs for any errors")
        print("  3. Update README.md with your deployment URL")
        return True
    else:
        print("⚠️  Some tests failed. Please review the errors above.\n")
        print("Troubleshooting tips:")
        print("  1. Check Vercel deployment logs")
        print("  2. Verify GEMINI_API_KEY is set correctly")
        print("  3. Ensure all dependencies are installed")
        print("  4. Check for any build errors")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/verify-deployment.py <deployment-url>")
        print("Example: python scripts/verify-deployment.py https://my-app.vercel.app")
        sys.exit(1)
    
    deployment_url = sys.argv[1]
    
    # Validate URL format
    if not deployment_url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)
    
    success = verify_deployment(deployment_url)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
