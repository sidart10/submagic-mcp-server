# Publishing Guide: Submagic MCP Server to Official Marketplaces

This guide walks you through publishing your Submagic MCP server to both the **Official Anthropic MCP Registry** and the **Cline MCP Marketplace**.

## 📋 Pre-Publishing Checklist

Before you begin, ensure you have:

- [x] Python 3.8+ installed
- [x] Git repository on GitHub
- [x] GitHub account (for authentication)
- [x] All code tested and working
- [x] README.md with MCP metadata added
- [x] server.json created
- [x] llms-install.md created (optional but recommended)
- [ ] 400×400 PNG logo created
- [ ] Package published to PyPI

---

## Part 1: Publish to PyPI (Required First Step)

### Step 1.1: Update GitHub URLs in setup.py

**IMPORTANT**: Before publishing, update the placeholder URLs in `setup.py`:

```python
# In setup.py, replace:
url="https://github.com/sid/submagic-mcp-server"

# With your actual GitHub username:
url="https://github.com/YOUR-USERNAME/submagic-mcp-server"
```

Update all three URL fields:
- `url` (main project URL)
- `project_urls.Bug Tracker`
- `project_urls.Source Code`

### Step 1.2: Create PyPI Account

1. Go to https://pypi.org/account/register/
2. Create account and verify email
3. Enable 2FA (recommended)

### Step 1.3: Generate API Token

1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens"
3. Click "Add API token"
4. Name: "submagic-mcp-server"
5. Scope: "Entire account" (or create after first upload)
6. **Copy the token** (starts with `pypi-`)

### Step 1.4: Configure PyPI Credentials

```bash
# Create .pypirc file
nano ~/.pypirc

# Add this content:
[pypi]
  username = __token__
  password = pypi-YOUR-TOKEN-HERE
```

### Step 1.5: Build and Upload Package

```bash
# Install build tools
pip install --upgrade build twine

# Build distribution packages
python -m build

# This creates:
# - dist/submagic_mcp_server-1.0.0-py3-none-any.whl
# - dist/submagic-mcp-server-1.0.0.tar.gz

# Upload to PyPI
python -m twine upload dist/*

# You'll see:
# Uploading distributions to https://upload.pypi.org/legacy/
# Uploading submagic_mcp_server-1.0.0-py3-none-any.whl
# Uploading submagic-mcp-server-1.0.0.tar.gz
```

### Step 1.6: Verify PyPI Upload

1. Visit https://pypi.org/project/submagic-mcp-server/
2. Check that package page loads correctly
3. Verify README displays properly
4. Test installation: `pip install submagic-mcp-server`

---

## Part 2: Publish to Official MCP Registry

### Step 2.1: Install MCP Publisher CLI

**macOS/Linux (Homebrew - Recommended):**
```bash
brew install mcp-publisher
```

**macOS/Linux (Pre-built Binary):**
```bash
curl -L "https://github.com/modelcontextprotocol/registry/releases/download/v1.0.0/mcp-publisher_1.0.0_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher && sudo mv mcp-publisher /usr/local/bin/
```

**Windows (PowerShell):**
```powershell
$arch = if ([System.Runtime.InteropServices.RuntimeInformation]::ProcessArchitecture -eq "Arm64") { "arm64" } else { "amd64" }
Invoke-WebRequest -Uri "https://github.com/modelcontextprotocol/registry/releases/download/v1.0.0/mcp-publisher_1.0.0_windows_$arch.tar.gz" -OutFile "mcp-publisher.tar.gz"
tar xf mcp-publisher.tar.gz mcp-publisher.exe
rm mcp-publisher.tar.gz
# Move mcp-publisher.exe to a directory in your PATH
```

### Step 2.2: Update server.json

**CRITICAL**: Update the GitHub URLs in `server.json`:

```json
{
  "name": "io.github.YOUR-USERNAME/submagic-mcp-server",
  "homepage": "https://github.com/YOUR-USERNAME/submagic-mcp-server",
  "repository": {
    "url": "https://github.com/YOUR-USERNAME/submagic-mcp-server.git"
  },
  "bugs": {
    "url": "https://github.com/YOUR-USERNAME/submagic-mcp-server/issues"
  },
  "author": {
    "name": "Your Name",
    "url": "https://github.com/YOUR-USERNAME"
  }
}
```

### Step 2.3: Authenticate with GitHub

```bash
# Navigate to your project directory
cd /path/to/submagic-mcp-server

# Login with GitHub OAuth
mcp-publisher login github

# This will:
# 1. Open your browser
# 2. Ask you to authorize the MCP Publisher
# 3. Store credentials locally
```

### Step 2.4: Publish to Registry

```bash
# Make sure you're in the project directory
cd /path/to/submagic-mcp-server

# Publish!
mcp-publisher publish

# You should see:
# ✓ Successfully published
```

### Step 2.5: Verify Registry Publication

```bash
# Search for your server in the registry
curl "https://registry.modelcontextprotocol.io/v0/servers?search=io.github.YOUR-USERNAME/submagic-mcp-server"

# Or visit the registry API docs:
# https://registry.modelcontextprotocol.io
```

---

## Part 3: Submit to Cline MCP Marketplace

### Step 3.1: Create 400×400 PNG Logo

**Requirements:**
- Dimensions: Exactly 400×400 pixels
- Format: PNG
- Size: < 1MB recommended
- Style: Clear, professional, recognizable at small sizes

**Design Tips:**
- Use high contrast colors
- Avoid small text (won't be readable when scaled)
- Simple, bold designs work best
- Consider using Submagic brand colors or video editing theme
- Test how it looks at 64×64 pixels

**Tools to Create Logo:**
- **Canva**: https://www.canva.com (use 400×400 custom size)
- **Figma**: https://www.figma.com
- **GIMP**: Free, open-source
- **Adobe Photoshop/Illustrator**: Professional tools
- **AI Tools**: DALL-E, Midjourney, Stable Diffusion

**Quick Option**: Use a screenshot of Submagic interface or a video icon with text overlay.

### Step 3.2: Push Code to GitHub (If Not Already Done)

```bash
# Initialize git (if not already)
git init

# Add all files except ignored ones
git add .

# Commit
git commit -m "Initial release v1.0.0 - AI-powered video editing MCP server"

# Create GitHub repository at https://github.com/new

# Add remote
git remote add origin https://github.com/YOUR-USERNAME/submagic-mcp-server.git

# Push
git branch -M main
git push -u origin main
```

### Step 3.3: Upload Logo to GitHub

```bash
# Create assets directory
mkdir -p assets

# Move your logo there
mv logo.png assets/logo.png

# Commit and push
git add assets/logo.png
git commit -m "Add logo for marketplace submission"
git push
```

### Step 3.4: Create Marketplace Submission

1. **Go to**: https://github.com/cline/mcp-marketplace/issues/new?template=mcp-server-submission.yml

2. **Fill out the form**:

   **Server Name**: `Submagic MCP Server`
   
   **GitHub Repository URL**: 
   ```
   https://github.com/YOUR-USERNAME/submagic-mcp-server
   ```
   
   **Logo URL**:
   ```
   https://raw.githubusercontent.com/YOUR-USERNAME/submagic-mcp-server/main/assets/logo.png
   ```
   
   **Short Description**:
   ```
   AI-powered video editing with automatic captions in 107 languages, magic zooms, B-rolls, and viral clip generation
   ```
   
   **Why Should This Be Added?**:
   ```
   Submagic MCP Server brings professional video editing capabilities to AI assistants:
   
   ✨ Key Benefits:
   - Automatic AI captions in 107 languages with 98%+ accuracy
   - Magic zooms and B-rolls for engaging content
   - Viral clip generation from YouTube videos
   - 30+ professional templates (Hormozi, Beast, Sara)
   - Platform-optimized exports (TikTok, Reels, Shorts)
   
   🎯 Use Cases:
   - Content creators making social media videos
   - Marketers creating ad campaigns
   - Educators adding captions to courses
   - Podcasters repurposing episodes into clips
   
   📊 Quality Indicators:
   - Production-ready with 100% API coverage
   - Comprehensive documentation and examples
   - Well-tested with error handling
   - Active maintenance
   
   This server enables users to automate video editing workflows that would normally require expensive software and hours of manual work.
   ```
   
   **Installation Testing Confirmation**:
   ```
   ✅ Yes, I have tested giving Cline my README.md and watched successful setup
   ```

3. **Submit the issue**

### Step 3.5: Wait for Review

- **Timeline**: Usually 2-3 days
- **What They Check**:
  - Community adoption (GitHub stars help!)
  - Developer credibility
  - Code quality and documentation
  - Security (especially for sensitive domains)

### Step 3.6: Address Feedback (If Any)

- Reviewers may ask questions or request changes
- Respond promptly to feedback
- Update your submission as needed

---

## Part 4: Post-Publication

### Step 4.1: Announce Your Server

**On GitHub**:
- Add topics: `mcp`, `model-context-protocol`, `video-editing`, `submagic`
- Create a release: v1.0.0 with release notes
- Add badges to README:
  ```markdown
  [![PyPI](https://img.shields.io/pypi/v/submagic-mcp-server)](https://pypi.org/project/submagic-mcp-server/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  ```

**On Social Media**:
- Share on Twitter/X with #MCP hashtag
- Post in relevant Reddit communities (r/LocalLLaMA, etc.)
- Share in MCP Discord: https://discord.gg/cline

### Step 4.2: Monitor for Issues

- Check GitHub issues regularly
- Respond to user questions
- Fix bugs promptly
- Consider feature requests

### Step 4.3: Plan for Updates

When you have updates:

**For PyPI**:
```bash
# Update version in setup.py
# Build and upload new version
python -m build
python -m twine upload dist/*
```

**For MCP Registry**:
```bash
# Update version in server.json
# Publish new version
mcp-publisher publish
```

---

## Troubleshooting

### PyPI Upload Fails

**Error**: "File already exists"
- **Solution**: Increment version number in `setup.py`

**Error**: "Invalid authentication"
- **Solution**: Check `.pypirc` credentials, regenerate token

### MCP Registry Publication Fails

**Error**: "Package validation failed"
- **Solution**: Ensure README contains `mcp-name: io.github.YOUR-USERNAME/submagic-mcp-server`

**Error**: "Authentication failed"
- **Solution**: Run `mcp-publisher login github` again

### Cline Marketplace Rejection

**Reason**: "Not enough community adoption"
- **Solution**: Get more GitHub stars, share on social media, build user base first

**Reason**: "Installation difficulties"
- **Solution**: Improve documentation, test installation process thoroughly

---

## Checklists

### ✅ Pre-Publishing Checklist

- [ ] Code is tested and working
- [ ] README.md contains MCP metadata
- [ ] server.json created with correct info
- [ ] llms-install.md created
- [ ] setup.py URLs updated with your GitHub username
- [ ] server.json URLs updated with your GitHub username
- [ ] Logo created (400×400 PNG)
- [ ] Code pushed to GitHub
- [ ] GitHub repository is public

### ✅ Publishing Checklist

- [ ] Published to PyPI successfully
- [ ] Package installable: `pip install submagic-mcp-server`
- [ ] Published to Official MCP Registry
- [ ] Verified in registry search
- [ ] Submitted to Cline Marketplace
- [ ] Logo uploaded and accessible

### ✅ Post-Publishing Checklist

- [ ] Added repository topics on GitHub
- [ ] Created v1.0.0 release on GitHub
- [ ] Announced on social media
- [ ] Monitoring for issues and feedback
- [ ] Planned update strategy

---

## Important Notes

1. **GitHub Username**: Replace `YOUR-USERNAME` everywhere with your actual GitHub username
2. **API Keys**: Never commit API keys to git
3. **Testing**: Always test installation before publishing
4. **Versioning**: Use semantic versioning (1.0.0, 1.0.1, 1.1.0, etc.)
5. **Documentation**: Keep docs updated with each release

---

## Resources

### Official Documentation
- **MCP Registry Publishing**: https://modelcontextprotocol.info/tools/registry/publishing/
- **MCP Registry FAQ**: https://modelcontextprotocol.info/tools/registry/faq/
- **Cline Marketplace**: https://github.com/cline/mcp-marketplace
- **PyPI Publishing**: https://packaging.python.org/tutorials/packaging-projects/

### Tools
- **MCP Publisher CLI**: https://github.com/modelcontextprotocol/registry
- **PyPI**: https://pypi.org
- **GitHub**: https://github.com

### Community
- **MCP Discord**: https://discord.gg/cline
- **MCP Discussions**: https://github.com/modelcontextprotocol/registry/discussions
- **Cline Discord**: https://discord.gg/cline

---

## Quick Reference Commands

```bash
# PyPI
python -m build
python -m twine upload dist/*

# MCP Registry
mcp-publisher login github
mcp-publisher publish

# Git
git add .
git commit -m "Release v1.0.0"
git tag v1.0.0
git push origin main --tags

# Verify
pip install submagic-mcp-server
curl "https://registry.modelcontextprotocol.io/v0/servers?search=submagic"
```

---

## Need Help?

- **Registry Issues**: https://github.com/modelcontextprotocol/registry/discussions
- **Marketplace Issues**: https://github.com/cline/mcp-marketplace/issues
- **PyPI Issues**: https://pypi.org/help/

Good luck with your publication! 🚀

