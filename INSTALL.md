# Installation Guide

## Prerequisites

1. **Python 3.8+** installed
2. **Common Room API token** - Get from [Common Room Settings → API tokens](https://app.commonroom.io/)
3. **MCP-compatible client** (Claude Code or Amazon Q CLI)

## Setup

### 1. Clone/Download Repository

```bash
git clone <repository-url>
cd commonroom-mcp
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env file with your credentials:
# COMMONROOM_KEY=your_api_token_here
# COMMONROOM_BASE_URL=https://app.commonroom.io/community/your-community-id
```

### 4. Test Server

```bash
python server.py
# Should start without errors (Ctrl+C to stop)
```

## Claude Code Installation

### Step 1: Locate Config File
Claude Code config is at: `~/Library/Application Support/Claude/claude_desktop_config.json`

### Step 2: Add MCP Server
Edit the config file and add (replace `/path/to/commonroom-mcp` with your actual path):

```json
{
  "mcpServers": {
    "commonroom": {
      "command": "python",
      "args": ["/path/to/commonroom-mcp/server.py"],
      "env": {
        "COMMONROOM_KEY": "your_api_token_here",
        "COMMONROOM_BASE_URL": "https://app.commonroom.io/community/your-community-id"
      }
    }
  }
}
```

**Using environment variable:**
```json
{
  "mcpServers": {
    "commonroom": {
      "command": "python",
      "args": ["/path/to/commonroom-mcp/server.py"],
      "env": {
        "COMMONROOM_KEY": "${COMMONROOM_KEY}",
        "COMMONROOM_BASE_URL": "${COMMONROOM_BASE_URL}"
      }
    }
  }
}
```

### Step 3: Restart Claude Code
Quit and restart Claude Code to load the MCP server.

### Step 4: Verify Installation
In Claude Code, try: "Get all Common Room activity types"

## Amazon Q CLI Installation

### Step 1: Install Q CLI
```bash
# If not already installed
pip install amazon-q-developer-cli
```

### Step 2: Configure MCP
Create or edit your Q CLI MCP configuration file:

```bash
# Create config directory if needed
mkdir -p ~/.config/amazon-q

# Edit MCP config
nano ~/.config/amazon-q/mcp-config.json
```

Add the Common Room server (replace `/path/to/commonroom-mcp` with your actual path):
```json
{
  "mcpServers": {
    "commonroom": {
      "command": "python",
      "args": ["/path/to/commonroom-mcp/server.py"],
      "env": {
        "COMMONROOM_KEY": "${COMMONROOM_KEY}",
        "COMMONROOM_BASE_URL": "${COMMONROOM_BASE_URL}"
      }
    }
  }
}
```

### Step 3: Start Q CLI with MCP
```bash
q chat --mcp-config ~/.config/amazon-q/mcp-config.json
```

### Step 4: Verify Installation
In Q CLI, try: "Show me Common Room activity types"

## Alternative: Global MCP Configuration

### For Claude Code
If you have multiple MCP servers, merge configurations:

```json
{
  "mcpServers": {
    "commonroom": {
      "command": "python",
      "args": ["/path/to/commonroom-mcp/server.py"],
      "env": {
        "COMMONROOM_KEY": "${COMMONROOM_KEY}"
      }
    },
    "other-server": {
      "command": "other-command",
      "args": ["other-args"]
    }
  }
}
```

### For Q CLI
Use the `--mcp-config` flag to specify your configuration file location.

## Troubleshooting

### Common Issues

**"Module not found" error:**
```bash
pip install mcp requests
```

**"COMMONROOM_KEY not found" error:**
- Verify environment variable is set: `echo $COMMONROOM_KEY`
- Check `.env` file exists and has correct format
- Restart terminal/application after setting environment variables

**"Server not responding" error:**
- Test server manually: `python server.py`
- Check file paths in configuration are absolute
- Verify Python is in PATH: `which python`

**Claude Code not showing tools:**
- Restart Claude Code completely
- Check config file syntax with JSON validator
- Verify config file location: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Q CLI not finding MCP config:**
- Use absolute path: `q chat --mcp-config /full/path/to/mcp-config.json`
- Check file permissions: `ls -la ~/.config/amazon-q/mcp-config.json`

### Debug Mode

Test the server directly:
```bash
cd /path/to/commonroom-mcp
python -c "from commonroom_client import CommonRoomClient; print(CommonRoomClient().get_token_status())"
```

Should return your API token status if working correctly.

## Next Steps

Once installed, you can:
- Ask for Common Room activity types
- Look up team members by email
- Add new activities and users
- Analyze segments and tags
- Get URLs for members, organizations, and segments

See [README.md](README.md) for usage examples.
