# Deployment Guide

## Important: Gemini API Setup

This application uses **Google Gemini AI** for voice classification. Before deploying, you need:

1. **Get a Gemini API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy your API key

2. **Set up locally** (for testing):
   - Create a `.env` file in your project root:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

3. **For production deployment**:
   - You'll add this as an environment variable in Vercel (see Step 2 below)

---

## Deploying to GitHub and Vercel

This guide explains how to deploy your AI Voice Detection system to GitHub and Vercel.

### Prerequisites

1. **GitHub Account**: [Sign up at GitHub](https://github.com)
2. **Vercel Account**: [Sign up at Vercel](https://vercel.com)
3. **Git installed** on your local machine

---

## Step 1: Push to GitHub ✅

Your code is already pushed to GitHub at: `https://github.com/Sai-Emani25/AI-Voice-detection`

---

## Step 2: Deploy to Vercel

### Option A: Using Vercel Dashboard (Recommended for first deployment)

1. **Go to Vercel**: Visit [vercel.com](https://vercel.com)
2. **Sign in** with your GitHub account
3. **Import Project**:
   - Click "Add New..." → "Project"
   - Select your GitHub repository: `AI-Voice-detection`
   - Click "Import"
4. **Configure Project**:
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`
5. **Environment Variables** (REQUIRED):
   - Click "Environment Variables"
   - Add: `GEMINI_API_KEY` = `your_gemini_api_key_here`
   - Get your API key from: [Google AI Studio](https://makersuite.google.com/app/apikey)
6. **Deploy**: Click "Deploy"

Your app will be live at: `https://your-project-name.vercel.app`

---

### Option B: Using Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy from project directory**:
   ```bash
   cd "d:\My stuff\Passion work\Websites I made\AI Voice Detection"
   vercel
   ```

4. **Follow the prompts**:
   - Set up and deploy? **Y**
   - Which scope? (select your account)
   - Link to existing project? **N**
   - Project name? (press Enter for default)
   - Directory? `./` (press Enter)

5. **Deploy to production**:
   ```bash
   vercel --prod
   ```

---

## Step 3: Set Up Automatic Deployments and CI/CD

### GitHub Actions Workflows

The repository includes comprehensive GitHub Actions workflows for CI/CD:

#### 1. **CI/CD Pipeline** (`.github/workflows/ci-cd.yml`)

Comprehensive workflow with 6 jobs that runs on every push and PR:

**Jobs:**
- **Code Quality & Validation**: Linting with flake8, formatting with black, syntax validation
- **Testing**: Unit tests, API tests, import validation, coverage reports
- **Security Scan**: Dependency vulnerability checks, secret scanning, environment variable validation
- **Build Validation**: Application startup verification, health checks, API documentation validation
- **Deploy to Vercel**: Automatic production deployment on main branch (requires secrets)
- **Deploy to Railway**: Optional staging deployment on develop branch (requires secrets)

**Secrets Required for Deployment:**
- `VERCEL_TOKEN`: Your Vercel authentication token
- `VERCEL_ORG_ID`: Your Vercel organization ID
- `VERCEL_PROJECT_ID`: Your Vercel project ID
- `GEMINI_API_KEY`: Your Google Gemini API key (for tests)
- `RAILWAY_TOKEN`: (Optional) Your Railway authentication token

#### 2. **Pull Request Tests** (`.github/workflows/test.yml`)

Runs on all pull requests to validate:
- No merge conflicts
- Requirements.txt is up-to-date with all critical dependencies
- Code quality standards
- All imports work correctly
- Generates PR validation summary

#### 3. **Enhanced Deploy Workflow** (`.github/workflows/deploy.yml`)

Enhanced version of the original deployment workflow with:
- Pre-deployment validation
- Environment variable checks
- Conditional deployment (only if secrets are configured)
- Deployment status notifications
- Dependency caching for faster builds

#### 4. **Docker Build** (`.github/workflows/docker-build.yml`)

Optional workflow for Docker-based deployments:
- Builds Docker images for the application
- Pushes to GitHub Container Registry
- Supports deployment to Railway, Render, or any Docker-compatible platform
- Includes health checks and proper configuration

### Setting Up GitHub Actions

**To enable automatic deployments:**

1. **Get Vercel Tokens**:
   ```bash
   # Install Vercel CLI if not already installed
   npm install -g vercel
   
   # Login and get tokens
   vercel login
   cd /path/to/AI-Voice-detection
   vercel link
   ```

2. **Copy these values**:
   - Vercel Token: Get from [Vercel Settings → Tokens](https://vercel.com/account/tokens)
   - Project ID: Found in `.vercel/project.json` (after running `vercel link`)
   - Org ID: Found in `.vercel/project.json`

3. **Add GitHub Secrets**:
   - Go to your GitHub repository
   - Settings → Secrets and variables → Actions
   - Click "New repository secret" and add:
     - `VERCEL_TOKEN`: Your Vercel token
     - `VERCEL_ORG_ID`: Your organization ID
     - `VERCEL_PROJECT_ID`: Your project ID
     - `GEMINI_API_KEY`: Your Gemini API key (for testing)

4. **Push changes**:
   ```bash
   git add .
   git commit -m "Enable GitHub Actions workflows"
   git push origin main
   ```

Now, every push to `main` branch will:
- ✅ Run code quality checks
- ✅ Execute all tests
- ✅ Scan for security vulnerabilities
- ✅ Validate the build
- ✅ Automatically deploy to Vercel (if secrets are configured)

### Workflow Status

You can check the status of your workflows at:
- `https://github.com/your-username/AI-Voice-detection/actions`

### Deployment Validation

Run the validation script to check your deployment configuration:

```bash
python scripts/validate-deployment.py
```

This will verify:
- ✓ Environment variables are set correctly
- ✓ All critical dependencies are installed
- ✓ Application can start successfully

---

## Fixing the Infinite Loop Issue ✅

The merge conflicts that were causing the infinite loop have been resolved. The WebSocket connection now properly handles:
- Connection lifecycle (open, message, error, close)
- Proper error handling
- Clean disconnection when stopping monitoring

---

## Testing Your Deployment

### Local Testing
```bash
uvicorn main:app --reload
# Visit: http://localhost:8000
```

### Production Testing
After deploying to Vercel, test your endpoints:
- `https://your-app.vercel.app/` - Main UI
- `https://your-app.vercel.app/docs` - API Documentation
- `https://your-app.vercel.app/health` - Health Check

---

## Troubleshooting

### Issue: "Module not found" errors
**Solution**: Ensure all dependencies are in `requirements.txt`

### Issue: WebSocket not working on Vercel
**Solution**: Vercel Serverless Functions have limitations with WebSockets. For production WebSocket support, consider:
- Using Vercel Edge Functions
- Deploying to a platform that supports persistent connections (Railway, Render, Heroku)

### Issue: File size limits
**Solution**: Vercel has a 4.5MB limit for serverless functions. Large audio files should use streaming or external storage.

---

## Alternative Deployment Platforms

If Vercel doesn't meet your needs, consider:

### **Railway** (Supports WebSockets)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### **Render**
1. Go to [render.com](https://render.com)
2. New → Web Service
3. Connect GitHub repository
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### **Heroku**
```bash
# Create Procfile
echo "web: uvicorn main:app --host 0.0.0.0 --port $PORT" > Procfile

# Deploy
heroku login
heroku create your-app-name
git push heroku main
```

---

## Repository Links

- **GitHub**: https://github.com/Sai-Emani25/AI-Voice-detection
- **Vercel** (after deployment): https://your-project.vercel.app

---

## Need Help?

- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
