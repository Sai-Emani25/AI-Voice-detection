# Deployment Checklist ✅

Use this checklist to ensure your deployment is successful.

## Pre-Deployment Checklist

### 1. Repository Setup
- [ ] All code changes committed and pushed to GitHub
- [ ] Branch is up to date with latest changes
- [ ] No merge conflicts
- [ ] `.gitignore` excludes unnecessary files (node_modules, .env, etc.)

### 2. Dependencies
- [ ] `requirements.txt` exists with all dependencies
- [ ] All dependencies have pinned versions
- [ ] No known security vulnerabilities
- [ ] Dependencies tested locally

### 3. Environment Configuration
- [ ] `.env.example` file exists
- [ ] All required environment variables documented
- [ ] `GEMINI_API_KEY` obtained from Google AI Studio
- [ ] No secrets committed to repository

### 4. Application Files
- [ ] `main.py` - Main FastAPI application
- [ ] `model.py` - Voice classifier
- [ ] `preprocessing.py` - Audio processing
- [ ] `api/index.py` - Vercel serverless entry point
- [ ] `vercel.json` - Vercel configuration
- [ ] All files syntax-validated (no Python errors)

### 5. Testing
- [ ] Application runs locally: `uvicorn main:app --reload`
- [ ] Health endpoint works: `http://localhost:8000/health`
- [ ] API documentation accessible: `http://localhost:8000/docs`
- [ ] Test script runs: `python test_api.py`
- [ ] All imports work correctly

---

## Deployment Checklist

### Vercel Deployment

#### Via Dashboard
- [ ] Logged into Vercel account
- [ ] Repository imported to Vercel
- [ ] `GEMINI_API_KEY` added as environment variable
- [ ] Deployment triggered
- [ ] Deployment completed successfully
- [ ] Live URL received

#### Via CLI
- [ ] Vercel CLI installed: `npm install -g vercel`
- [ ] Logged in: `vercel login`
- [ ] Project linked: `vercel link`
- [ ] Environment variable set: `vercel env add GEMINI_API_KEY`
- [ ] Deployed to production: `vercel --prod`

#### Via GitHub Actions
- [ ] `VERCEL_TOKEN` secret added to GitHub
- [ ] `VERCEL_ORG_ID` secret added to GitHub
- [ ] `VERCEL_PROJECT_ID` secret added to GitHub
- [ ] `GEMINI_API_KEY` secret added to GitHub
- [ ] Workflow files exist in `.github/workflows/`
- [ ] Changes merged to `main` branch
- [ ] GitHub Actions workflow triggered
- [ ] Workflow completed successfully

---

## Post-Deployment Checklist

### 1. Verification
- [ ] Health endpoint responds: `https://your-app.vercel.app/health`
- [ ] API docs accessible: `https://your-app.vercel.app/docs`
- [ ] Main page loads: `https://your-app.vercel.app/`
- [ ] No 500 errors in Vercel logs
- [ ] Environment variables loaded correctly

### 2. Functionality Testing
- [ ] Test audio upload via web interface
- [ ] Test `/detect` API endpoint with sample audio
- [ ] Test response time (should be < 10 seconds)
- [ ] Test different audio formats (WAV, MP3)
- [ ] Test different languages (Tamil, English, Hindi, etc.)
- [ ] WebSocket connection works (if applicable)

### 3. Performance
- [ ] Response times acceptable
- [ ] No memory errors
- [ ] No timeout errors
- [ ] Concurrent requests handled properly

### 4. Monitoring
- [ ] Vercel dashboard shows successful deployment
- [ ] Error logs checked (no critical errors)
- [ ] Usage/analytics reviewed
- [ ] Alerts configured (optional)

---

## Troubleshooting Guide

If deployment fails, check these in order:

### 1. Build Errors
- [ ] Review Vercel build logs
- [ ] Check for missing dependencies in `requirements.txt`
- [ ] Verify Python version compatibility (3.10+)
- [ ] Check for syntax errors in Python files

### 2. Runtime Errors
- [ ] Verify `GEMINI_API_KEY` is set correctly
- [ ] Check Vercel function logs for error messages
- [ ] Verify all imports resolve correctly
- [ ] Check for file permission issues

### 3. API Errors
- [ ] Test Gemini API key directly
- [ ] Check API rate limits
- [ ] Verify network connectivity to Google APIs
- [ ] Review error messages in response

### 4. Performance Issues
- [ ] Check Vercel function execution time limits
- [ ] Review audio file size limits
- [ ] Optimize heavy computations
- [ ] Consider upgrading Vercel plan if needed

---

## Deployment Validation Script

Run this script to validate your deployment:

```bash
# Test health endpoint
curl https://your-app.vercel.app/health

# Test API documentation
curl https://your-app.vercel.app/docs

# Test root endpoint
curl https://your-app.vercel.app/
```

Or use the provided Python script:
```bash
python scripts/validate-deployment.py
```

---

## Rollback Plan

If deployment fails and you need to rollback:

### Vercel Dashboard
1. Go to Vercel dashboard
2. Click on your project
3. Go to "Deployments"
4. Find the last working deployment
5. Click "..." menu → "Promote to Production"

### GitHub Actions
1. Revert the commit that caused issues:
   ```bash
   git revert <commit-hash>
   git push origin main
   ```
2. GitHub Actions will auto-deploy the reverted version

---

## Success Criteria

Your deployment is successful when:

✅ All pre-deployment checks pass
✅ Deployment completes without errors
✅ Health endpoint returns 200 OK
✅ API documentation is accessible
✅ Test detection request succeeds
✅ No errors in production logs
✅ Response times are acceptable

---

## Post-Deployment Tasks

After successful deployment:

1. [ ] Update README.md with live deployment URL
2. [ ] Test all API endpoints thoroughly
3. [ ] Share deployment URL with team/users
4. [ ] Set up monitoring/alerting (optional)
5. [ ] Configure custom domain (optional)
6. [ ] Document any deployment-specific configuration
7. [ ] Create backup/disaster recovery plan
8. [ ] Schedule regular dependency updates

---

## Maintenance Checklist (Weekly/Monthly)

- [ ] Review error logs
- [ ] Check dependency updates
- [ ] Monitor API usage
- [ ] Review security alerts
- [ ] Test critical functionality
- [ ] Update documentation if needed

---

**Congratulations on your deployment!** 🎉

For questions or issues, refer to:
- [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for step-by-step instructions
- [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment guide
- Vercel documentation at [vercel.com/docs](https://vercel.com/docs)
