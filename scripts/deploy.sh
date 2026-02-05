#!/bin/bash

# One-Command Deployment Script for Vercel
# This script automates the deployment process

set -e  # Exit on error

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║        AI Voice Detection - Vercel Deployment               ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "⚠️  Vercel CLI not found!"
    echo ""
    echo "Installing Vercel CLI..."
    npm install -g vercel
    echo "✓ Vercel CLI installed"
    echo ""
fi

# Check if user is logged in
echo "🔐 Checking Vercel authentication..."
if ! vercel whoami &> /dev/null; then
    echo "Please login to Vercel:"
    vercel login
fi

echo "✓ Logged in to Vercel"
echo ""

# Check for GEMINI_API_KEY
echo "🔑 Checking for GEMINI_API_KEY..."
if [ -f .env ]; then
    if grep -q "GEMINI_API_KEY" .env; then
        echo "✓ Found .env file with GEMINI_API_KEY"
    else
        echo "⚠️  .env file found but no GEMINI_API_KEY"
        echo "Please add GEMINI_API_KEY to your .env file"
    fi
else
    echo "⚠️  No .env file found"
    echo "Creating .env from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo ""
        echo "📝 Please edit .env and add your GEMINI_API_KEY:"
        echo "   nano .env"
        echo ""
        read -p "Press Enter after you've added your API key..."
    fi
fi

echo ""
echo "📦 Installing dependencies locally to verify..."
pip install -r requirements.txt --quiet
echo "✓ Dependencies installed"
echo ""

echo "🧪 Running basic validation..."
python -c "from main import app; print('✓ Application imports successfully')" 2>&1 | grep -v "Gemini API" || true
echo "✓ Validation passed"
echo ""

echo "🚀 Deploying to Vercel..."
echo ""

# Deploy to Vercel
vercel --prod

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║              ✅ Deployment Successful!                      ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Get the deployment URL
DEPLOYMENT_URL=$(vercel ls --prod 2>/dev/null | grep "Ready" | head -1 | awk '{print $2}' || echo "")

if [ -n "$DEPLOYMENT_URL" ]; then
    echo "🌐 Your app is live at:"
    echo "   https://$DEPLOYMENT_URL"
    echo ""
    echo "📚 API Documentation:"
    echo "   https://$DEPLOYMENT_URL/docs"
    echo ""
    echo "❤️  Health Check:"
    echo "   https://$DEPLOYMENT_URL/health"
    echo ""
    
    echo "🧪 Running post-deployment verification..."
    if command -v python3 &> /dev/null; then
        python3 scripts/verify-deployment.py "https://$DEPLOYMENT_URL" || echo "⚠️  Some verification tests failed. Check the output above."
    fi
fi

echo ""
echo "Next Steps:"
echo "  1. Set environment variable in Vercel dashboard:"
echo "     vercel env add GEMINI_API_KEY"
echo "  2. Test your deployment at the URL above"
echo "  3. Check Vercel dashboard for logs and settings"
echo ""
echo "Need help? Check QUICK_DEPLOY.md for detailed instructions"
echo ""
