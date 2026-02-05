# AI-Generated Voice Detection System

[![CI/CD Pipeline](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/ci-cd.yml)
[![Deploy to Vercel](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/deploy.yml/badge.svg)](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/deploy.yml)
[![PR Tests](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/test.yml/badge.svg)](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/test.yml)
[![Docker Build](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/docker-build.yml/badge.svg)](https://github.com/Sai-Emani25/AI-Voice-detection/actions/workflows/docker-build.yml)

This project is an API-based system designed to detect whether a voice sample is AI-generated or Human-generated using **Google Gemini AI**. It supports multiple languages (Tamil, English, Hindi, Malayalam, Telugu, Kannada) and accepts Base64-encoded MP3 audio inputs.

## 🚀 Live Demo

- **GitHub Repository**: https://github.com/Sai-Emani25/AI-Voice-detection
- **Deployment Guide**: See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions

## Features

- **API Endpoint**: RESTful API built with FastAPI.
- **Live Audio Monitoring**: Real-time voice detection using WebSocket
- **Interactive UI**: Modern web interface with file upload and live monitoring
- **Input Format**: JSON payload with Base64-encoded audio and language tag.
- **Output Format**: Structured JSON with classification, confidence score, and explanation.
- **Extensible Architecture**: Modular design allowing easy integration of trained ML models (PyTorch, TensorFlow, etc.).
- **Comprehensive CI/CD**: Automated testing, security scanning, and deployment workflows

## Project Structure

- `main.py`: The entry point for the FastAPI application.
- `model.py`: Contains the `VoiceClassifier` class that uses **Google Gemini AI** for voice classification.
- `preprocessing.py`: Handles audio decoding and feature extraction.
- `requirements.txt`: List of dependencies with pinned versions.
- `test_api.py`: A script to test the API with dummy audio.
- `api/index.py`: Vercel serverless function entry point.
- `.github/workflows/`: CI/CD workflows for automated testing and deployment.
- `scripts/validate-deployment.py`: Deployment validation script.

## Setup and Run

1. **Get Gemini API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in and create an API key
   - Copy your API key

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variable**:
   ```bash
   # Windows PowerShell
   $env:GEMINI_API_KEY="your_api_key_here"
   
   # Linux/Mac
   export GEMINI_API_KEY="your_api_key_here"
   
   # Or create a .env file (recommended)
   cp .env.example .env
   # Then edit .env and add your API key
   ```

4. **Run the Server**:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

5. **Test the API**:
   You can use the provided test script:
   ```bash
   python test_api.py
   ```
   Or use `curl` / Postman:
   ```bash
   curl -X POST "http://localhost:8000/detect" \
        -H "Content-Type: application/json" \
        -d '{"audio_base64": "<BASE64_STRING>", "language": "English"}'
   ```

## Gemini AI Integration

This application uses **Google Gemini AI** for intelligent voice classification:

- **How it works**: Audio features are extracted and analyzed by Gemini AI
- **Features analyzed**: Spectral centroid, rolloff, zero-crossing rate, MFCC, and more
- **AI-powered detection**: Gemini identifies patterns consistent with AI-generated or human voices
- **No local model required**: All inference happens through the Gemini API

## API Specification

### POST `/detect`

**Request Body**:
```json
{
  "audio_base64": "SUQzBAAAAA...",
  "language": "English"
}
```

**Response**:
```json
{
  "classification": "AI-Generated",
  "confidence_score": 0.95,
  "explanation": "High confidence based on spectral artifacts...",
  "metadata": { ... }
}
```

## 🚀 Quick Deploy

### Option 1: One-Click Deploy to Vercel (Fastest - 2 Minutes)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Sai-Emani25/AI-Voice-detection&env=GEMINI_API_KEY&envDescription=Get%20your%20Gemini%20API%20key%20from%20Google%20AI%20Studio&envLink=https://makersuite.google.com/app/apikey)

**Steps:**
1. Click the button above
2. Sign in to Vercel with GitHub
3. Add your `GEMINI_API_KEY` (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
4. Click "Deploy"
5. Your app is live in 2 minutes! 🎉

### Option 2: Deploy via Vercel CLI (3 Minutes)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd AI-Voice-detection
vercel --prod

# Add environment variable
vercel env add GEMINI_API_KEY
```

### Option 3: Automated Deployment Script

```bash
# Run the deployment script
./scripts/deploy.sh
```

### 📖 Detailed Deployment Guides

- **[QUICK_DEPLOY.md](QUICK_DEPLOY.md)** - Step-by-step deployment guide (5 min read)
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Comprehensive deployment documentation
- **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Deployment verification checklist

### Verify Your Deployment

After deployment, test your app:

```bash
python scripts/verify-deployment.py https://your-app.vercel.app
```

---

## Deployment

### Deploy to Vercel (Recommended)

1. **Push to GitHub** (already done ✅)
2. **Deploy to Vercel**:
   - Visit [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Add `GEMINI_API_KEY` environment variable
   - Click "Deploy"

For detailed deployment instructions including GitHub Actions automation, see **[DEPLOYMENT.md](DEPLOYMENT.md)**.

### Other Platforms

The application can also be deployed to:
- **Railway**: Full WebSocket support
- **Render**: Easy Python app deployment
- **Heroku**: Traditional PaaS deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for platform-specific instructions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
