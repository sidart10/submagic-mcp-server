# Submagic MCP Server - Installation Guide for AI Assistants

This guide is optimized for AI coding assistants (like Cline, Claude, etc.) to autonomously install and configure the Submagic MCP server.

## Overview

The Submagic MCP Server provides AI-powered video editing capabilities including automatic captions in 107 languages, magic zooms, B-rolls, and viral clip generation. This server integrates with the Submagic API.

## Prerequisites

- **Python 3.8+** installed on the system
- **pip** (Python package manager)
- **Submagic API Key** from https://app.submagic.co/signup

## Installation Methods

### Method 1: Install from PyPI (Recommended)

```bash
# Install the package globally or in a virtual environment
pip install submagic-mcp-server

# Or with virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install submagic-mcp-server
```

### Method 2: Install from Source (Development)

```bash
# Clone the repository
git clone https://github.com/sidart10/submagic-mcp-server.git
cd submagic-mcp-server

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Configuration

### Step 1: Get API Key

1. Sign up at https://app.submagic.co/signup
2. Navigate to Settings → API Keys
3. Copy your API key (starts with `sk-`)

### Step 2: Configure MCP Client

#### For Claude Desktop

Add to `claude_desktop_config.json` (usually at `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "submagic": {
      "command": "python",
      "args": ["-m", "submagic_mcp"],
      "env": {
        "SUBMAGIC_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

**If installed from source**, use absolute paths:

```json
{
  "mcpServers": {
    "submagic": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["/absolute/path/to/submagic_mcp.py"],
      "env": {
        "SUBMAGIC_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

#### For Cline (VS Code Extension)

Add to MCP settings:

```json
{
  "mcpServers": {
    "submagic": {
      "command": "python",
      "args": ["-m", "submagic_mcp"],
      "env": {
        "SUBMAGIC_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

### Step 3: Restart MCP Client

- **Claude Desktop**: Quit and restart the application
- **Cline**: Reload VS Code window
- **Other clients**: Follow their specific restart instructions

## Verification

After installation, verify the server is working:

```bash
# Test the server directly (if installed from source)
python test_server.py

# Or check in your MCP client by trying:
# "List available Submagic languages"
# "Show me Submagic templates"
```

## Available Tools

Once installed, these tools will be available in your MCP client:

1. **submagic_list_languages** - Get 107+ supported language codes
2. **submagic_list_templates** - View 30+ professional templates
3. **submagic_create_project** - Create video with AI captions
4. **submagic_get_project** - Check status and get download URLs
5. **submagic_update_project** - Fine-tune editing after creation
6. **submagic_export_project** - Export with custom dimensions
7. **submagic_create_magic_clips** - Generate viral clips from YouTube

## Common Use Cases

### Example 1: Add AI Captions to Video

```
Create a Submagic project for my product demo video at https://example.com/demo.mp4
Use English language and Hormozi 2 template
Enable magic zooms and fast silence removal
```

### Example 2: Generate TikTok Clips from YouTube

```
Generate 15-30 second TikTok clips from this YouTube video:
https://youtube.com/watch?v=abc123
Use English language
```

### Example 3: Export for Instagram Reels

```
Export my Submagic project [project-id] 
Dimensions: 1080x1920 (9:16 vertical)
30 FPS
```

## Troubleshooting

### Issue: "SUBMAGIC_API_KEY not found"

**Solution**: Ensure the API key is set in the environment configuration of your MCP client's config file. The key must start with `sk-`.

### Issue: "Server not responding"

**Solutions**:
1. Check Python version (requires 3.8+): `python --version`
2. Verify dependencies are installed: `pip list | grep mcp`
3. Check MCP client logs for connection errors
4. Restart your MCP client completely

### Issue: "Authentication failed"

**Solution**: Verify your API key is valid by testing it at https://api.submagic.co/v1/languages with:
```bash
curl -H "x-api-key: your-key-here" https://api.submagic.co/v1/languages
```

### Issue: "Rate limit exceeded"

**Solution**: Submagic has rate limits:
- Lightweight operations: 1000/hour
- Standard operations: 500/hour
Wait a few minutes and retry. Consider upgrading your Submagic plan.

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `SUBMAGIC_API_KEY` | Yes | Your Submagic API key from app.submagic.co |

## File Locations

- **Config (Claude Desktop macOS)**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Config (Claude Desktop Windows)**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Logs (if debugging)**: Check your MCP client's log directory

## Advanced Configuration

### Custom Python Path

If you need to use a specific Python installation:

```json
{
  "command": "/usr/local/bin/python3.11",
  "args": ["-m", "submagic_mcp"],
  "env": {
    "SUBMAGIC_API_KEY": "sk-your-key"
  }
}
```

### Virtual Environment

If installed in a venv, use the venv's Python:

```json
{
  "command": "/path/to/venv/bin/python",
  "args": ["-m", "submagic_mcp"],
  "env": {
    "SUBMAGIC_API_KEY": "sk-your-key"
  }
}
```

## Resources

- **API Documentation**: https://docs.submagic.co
- **Get API Key**: https://app.submagic.co/signup
- **GitHub Repository**: https://github.com/sidart10/submagic-mcp-server
- **Report Issues**: https://github.com/sidart10/submagic-mcp-server/issues
- **MCP Protocol**: https://modelcontextprotocol.io

## Pricing

Submagic offers several tiers:
- **Free Trial**: 3 videos with watermark
- **Starter**: $14/month - 20 videos
- **Growth**: $40/month - Unlimited
- **Business**: $60/month - Unlimited + advanced features

Visit https://www.submagic.co/pricing for current pricing.

## Notes for AI Assistants

- Always check that the API key is set before attempting operations
- Processing times vary: 2-10 minutes for normal projects, 5-15 minutes for magic clips
- Videos must be publicly accessible URLs (HTTP/HTTPS)
- Supported formats: MP4, MOV (input and output)
- Max file size: 2GB, Max duration: 2 hours
- After any project updates, remember to re-export to apply changes
- Use `submagic_get_project` to poll status every 30-60 seconds

## Success Indicators

Installation is successful when:
1. ✅ MCP client shows Submagic tools in available tools list
2. ✅ `submagic_list_languages` returns 107+ language codes
3. ✅ `submagic_list_templates` returns 30+ template names
4. ✅ No authentication errors when calling tools

