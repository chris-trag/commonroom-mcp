# Common Room MCP Setup Guide

Complete guide to setting up the Common Room MCP server with all required credentials.

## Step 1: Get Your API Token

1. **Navigate to API Tokens**:
   - Go to: `https://app.commonroom.io/community/YOUR-COMMUNITY-ID/settings/api-tokens`
   - Replace `YOUR-COMMUNITY-ID` with your actual community ID

2. **Create New Token**:
   - Click "Create API Token"
   - Give it a descriptive name (e.g., "MCP Server", "Q CLI Integration")
   - Copy the token immediately - you won't see it again!

3. **Documentation**: [Common Room API Token Guide](https://www.commonroom.io/docs/set-preferences/api-tokens/)

## Step 2: Find Your Community ID

Your Community ID is in your Common Room URL:
- URL: `https://app.commonroom.io/community/8683-amazon-developer`
- Community ID: `8683-amazon-developer`

## Step 3: Get Your Destination ID

For adding activities and users via API, you need a Destination ID:

1. **Go to Sources Settings**:
   - Navigate to: `https://app.commonroom.io/community/YOUR-COMMUNITY-ID/settings/sources`

2. **Find API Source**:
   - Click on "API" source
   - Or go directly to: `https://app.commonroom.io/community/YOUR-COMMUNITY-ID/settings/sources/api`

3. **Copy Destination ID**:
   - Look for the Destination ID number (e.g., `138683`)
   - This is what you'll use for `COMMONROOM_DESTINATION_ID`

## Step 4: Signal ID (Optional)

Signal IDs help categorize activities. You can:
- Use an existing signal from your Common Room settings
- Create a new signal for your MCP activities
- Leave blank to use default signal handling

## Step 5: Configure Environment

Create your `.env` file:

```bash
cp .env.example .env
```

Edit `.env` with your values:

```bash
# Required: Your API token from Step 1
COMMONROOM_KEY=your_actual_api_token_here

# Required: Your community URL from Step 2  
COMMONROOM_BASE_URL=https://app.commonroom.io/community/your-community-id

# Required for adding activities/users: Destination ID from Step 3
COMMONROOM_DESTINATION_ID=your_destination_id_here

# Optional: Signal ID for categorizing activities
COMMONROOM_SIGNAL_ID=your_signal_id_here
```

## Step 6: Test Your Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Test the server
python server.py

# Test with a simple query (in another terminal with Q CLI)
q chat --mcp-config mcp-config.json
# Then ask: "Get all Common Room activity types"
```

## Troubleshooting

**"COMMONROOM_KEY not found"**:
- Check your `.env` file exists and has the correct token
- Restart your terminal/application after setting environment variables

**"destination_source_id required"**:
- Make sure `COMMONROOM_DESTINATION_ID` is set in your `.env` file
- Verify the Destination ID is correct from your API source settings

**"Unauthorized" errors**:
- Verify your API token is correct and hasn't expired
- Check that the token has the necessary permissions

## API Reference

- [Common Room API Documentation](https://api.commonroom.io/docs/community.html)
- [Authentication Guide](https://api.commonroom.io/docs/community.html#section/Authentication)
- [API Token Management](https://www.commonroom.io/docs/set-preferences/api-tokens/)
