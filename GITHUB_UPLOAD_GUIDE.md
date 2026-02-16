# 📤 GitHub Upload Guide

Your code is ready to push to GitHub! Follow these steps:

## Option 1: Create New Repository on GitHub (Recommended)

### Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Fill in the details:
   - **Repository name**: `curling-chatbot` (or your preferred name)
   - **Description**: "Free AI chatbot for Olympic curling questions with web search"
   - **Visibility**: Public or Private (your choice)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

### Step 2: Push Your Code
After creating the repository, GitHub will show you commands. Use these:

```bash
cd curling-chatbot

# Add your GitHub repository as remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push your code
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/johndoe/curling-chatbot.git
git push -u origin main
```

### Step 3: Verify Upload
1. Refresh your GitHub repository page
2. You should see all your files!

---

## Option 2: Using GitHub CLI (gh)

If you have GitHub CLI installed:

```bash
cd curling-chatbot

# Create repository and push in one command
gh repo create curling-chatbot --public --source=. --push

# Or for private repository
gh repo create curling-chatbot --private --source=. --push
```

---

## Option 3: Using GitHub Desktop

1. Open GitHub Desktop
2. Click "Add" → "Add Existing Repository"
3. Select the `curling-chatbot` folder
4. Click "Publish repository"
5. Choose public/private and click "Publish"

---

## Current Git Status

✅ Git repository initialized
✅ All files added and committed
✅ Branch renamed to 'main'
✅ Ready to push!

**Commit message:** "Initial commit: Free curling chatbot with Ollama and DuckDuckGo search"

---

## What's Included in Your Repository

- `app.py` - Streamlit web interface
- `curling_agent.py` - Core chatbot logic
- `requirements.txt` - Python dependencies
- `README.md` - Complete documentation
- `QUICKSTART.md` - 5-minute setup guide
- `PROJECT_PLAN.md` - Architecture details
- `setup.sh` - Linux/macOS setup script
- `setup.bat` - Windows setup script
- `.gitignore` - Git ignore rules

---

## After Pushing to GitHub

### Add Topics (Recommended)
On your GitHub repository page, click "Add topics" and add:
- `chatbot`
- `curling`
- `ollama`
- `langchain`
- `streamlit`
- `ai`
- `free`
- `python`

### Enable GitHub Pages (Optional)
If you want to showcase your project:
1. Go to Settings → Pages
2. Add a description and website link

### Add a License (Optional)
1. Click "Add file" → "Create new file"
2. Name it `LICENSE`
3. Choose a license template (MIT is popular for open source)

---

## Troubleshooting

### "Permission denied (publickey)"
You need to set up SSH keys or use HTTPS with personal access token.

**Quick fix - Use HTTPS:**
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### "Repository not found"
Make sure:
1. Repository exists on GitHub
2. URL is correct
3. You have access to the repository

### "Failed to push"
```bash
# Pull first if repository has changes
git pull origin main --rebase

# Then push
git push -u origin main
```

---

## Need Help?

Run these commands to check your setup:

```bash
cd curling-chatbot

# Check git status
git status

# Check remote
git remote -v

# Check branch
git branch
```

---

## Quick Reference

```bash
# View commit history
git log --oneline

# Add more changes later
git add .
git commit -m "Your commit message"
git push

# Pull latest changes
git pull origin main
```

---

Ready to share your free curling chatbot with the world! 🥌🚀