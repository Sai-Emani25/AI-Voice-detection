# Quick Deployment Guide 🚀

This guide will help you deploy your AI Voice Detection system to production quickly.

## Prerequisites

Before deploying, ensure you have:

1. ✅ A GitHub account with this repository
2. ✅ A Vercel account (free tier works)
3. ✅ A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

---

## Option 1: Deploy to Vercel (Recommended) - 5 Minutes

### Step 1: Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. **Copy the API key** (you'll need it in Step 3)

### Step 2: Deploy to Vercel via Dashboard

1. **Go to Vercel**: Visit [vercel.com](https://vercel.com)
2. **Sign in** with your GitHub account
3. **Import Project**:
   - Click "Add New..." → "Project"
   - Select the repository: `Sai-Emani25/AI-Voice-detection`
   - Click "Import"

4. **Configure Project**:
   - Framework Preset: **Other**
   - Root Directory: `./` (default)
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

5. **Add Environment Variable** (CRITICAL):
   - Click "Environment Variables"
   - Add variable:
     - Name: `GEMINI_API_KEY`
     - Value: `[paste your API key from Step 1]`
   - Click "Add"

6. **Deploy**:
   - Click "Deploy"
   - Wait 2-3 minutes for deployment to complete
   - Your app will be live at: `https://your-project-name.vercel.app`

### Step 3: Test Your Deployment

Once deployed, visit these URLs to verify:

- **Main App**: `https://your-project-name.vercel.app/`
- **API Docs**: `https://your-project-name.vercel.app/docs`
- **Health Check**: `https://your-project-name.vercel.app/health`

---

## Option 2: Deploy via Vercel CLI - 3 Minutes

### Prerequisites
- Node.js installed on your computer
- Terminal/Command Prompt access

### Steps

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Login to Vercel
vercel login

# 3. Navigate to your project
cd /path/to/AI-Voice-detection

# 4. Deploy
vercel

# 5. Follow the prompts:
#    - Set up and deploy? Y
#    - Which scope? [select your account]
#    - Link to existing project? N
#    - Project name? [press Enter for default]
#    - Directory? ./ [press Enter]

# 6. Deploy to production
vercel --prod

# 7. Set environment variable
vercel env add GEMINI_API_KEY
# Paste your Gemini API key when prompted
# Select "Production" environment
```

Your app is now live! 🎉

---

## Option 3: Enable GitHub Actions Auto-Deploy

This enables automatic deployment whenever you push to the `main` branch.

### Step 1: Get Vercel Credentials

```bash
# Install Vercel CLI if not already installed
npm install -g vercel

# Login
vercel login

# Link to your project
cd /path/to/AI-Voice-detection
vercel link
```

After running `vercel link`, check the `.vercel/project.json` file for:
- `projectId`
- `orgId`

### Step 2: Get Vercel Token

1. Visit [Vercel Settings → Tokens](https://vercel.com/account/tokens)
2. Click "Create Token"
3. Name it: "GitHub Actions"
4. Click "Create"
5. **Copy the token** (you'll only see it once!)

### Step 3: Add GitHub Secrets

1. Go to your GitHub repository: `https://github.com/Sai-Emani25/AI-Voice-detection`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"** and add each of these:

   | Name | Value |
   |------|-------|
   | `VERCEL_TOKEN` | [Your Vercel token from Step 2] |
   | `VERCEL_ORG_ID` | [orgId from .vercel/project.json] |
   | `VERCEL_PROJECT_ID` | [projectId from .vercel/project.json] |
   | `GEMINI_API_KEY` | [Your Gemini API key] |

### Step 4: Merge Your Branch

```bash
# Checkout main branch
git checkout main

# Merge your changes
git merge copilot/update-requirements-and-cicd

# Push to GitHub
git push origin main
```

**GitHub Actions will automatically deploy to Vercel!** 🚀

Check deployment status at: `https://github.com/Sai-Emani25/AI-Voice-detection/actions`

---

## Option 4: Deploy to Railway (Alternative)

Railway supports WebSockets and is great for real-time features.

### Steps

1. **Sign up**: Visit [railway.app](https://railway.app)
2. **New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `AI-Voice-detection`
3. **Add Environment Variable**:
   - Go to Variables
   - Add: `GEMINI_API_KEY` = [your API key]
4. **Deploy**: Railway will automatically deploy!

---

## Troubleshooting

### Issue: "Module not found" errors
**Solution**: Make sure `requirements.txt` is in the root directory with all dependencies

### Issue: API returns 500 errors
**Solution**: Check that `GEMINI_API_KEY` is set correctly in environment variables

### Issue: WebSocket not working on Vercel
**Solution**: Vercel Serverless has WebSocket limitations. Use Railway or Render for full WebSocket support

### Issue: Deployment takes too long
**Solution**: This is normal for first deployment (installing Python dependencies). Subsequent deploys are faster.

---

## Verify Your Deployment

Once deployed, test the following:

1. **Health Check**: `GET /health`
   ```bash
   curl https://your-app.vercel.app/health
   ```
   Expected: `{"status": "healthy"}`

2. **API Documentation**: Visit `/docs`
   Should show interactive Swagger UI

3. **Test Detection**: Use the web interface at `/app`
   Upload an audio file and test the detection

---

## Next Steps

After successful deployment:

1. ✅ Update your README.md with the live URL
2. ✅ Test all features thoroughly
3. ✅ Monitor logs for any errors
4. ✅ Set up custom domain (optional)
5. ✅ Configure monitoring/analytics (optional)

---

## Need Help?

- **Vercel Docs**: [vercel.com/docs](https://vercel.com/docs)
- **GitHub Actions**: Check `.github/workflows/` for workflow files
- **API Issues**: Check Vercel logs in dashboard

**Your AI Voice Detection system is ready to deploy!** 🎉
