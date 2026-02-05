# Quick Setup Guide for Gemini API

## 🚀 Getting Started

Follow these steps to set up your AI Voice Detection system with Gemini AI:

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the API key (it looks like: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)

### 2. Set Up Locally

#### Option A: Using .env file (Recommended)

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in your text editor and add your API key:
   ```
   GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```

#### Option B: Using Environment Variable

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

The application will start at: **http://localhost:8000**

### 5. Test It Out

Open your browser and go to:
- **Main UI**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Interactive Test**: http://localhost:8000/app

## 🔧 For Vercel Deployment

When deploying to Vercel, you need to add the API key as an **Environment Variable**:

1. Go to your project in Vercel Dashboard
2. Settings → Environment Variables
3. Add new variable:
   - **Name**: `GEMINI_API_KEY`
   - **Value**: Your Gemini API key
   - **Environment**: Production, Preview, Development (select all)
4. Redeploy your application

## ⚠️ Important Security Notes

- **NEVER** commit your `.env` file to Git (it's already in `.gitignore`)
- **NEVER** share your API key publicly
- **NEVER** hardcode your API key in the source code
- For production, always use environment variables

## 🆘 Troubleshooting

### Error: "Gemini API key is required"
**Solution**: Make sure you've set the `GEMINI_API_KEY` environment variable or created a `.env` file

### Error: "Module not found: google.generativeai"
**Solution**: Run `pip install -r requirements.txt` again

### API key not working
**Solution**: 
- Check if the API key is correct (no extra spaces)
- Make sure you've enabled the Gemini API in Google Cloud Console
- Verify your Google account has API access

## 📚 Additional Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Full Deployment Guide](DEPLOYMENT.md)
- [Project README](README.md)

---

**Happy coding! 🎉**
