# Common Room MCP Server Specification

## Overview
Unofficial MCP server that exposes Common Room API functionality as tools for AI assistants (Q CLI, Claude Code). Features auto-generated IDs and flexible user data handling for seamless integration.

## Core Requirements

### Authentication
- Requires `COMMONROOM_KEY` environment variable
- Uses Bearer token authentication with Common Room API
- API base URL: `https://api.commonroom.io/community/v1`

### MCP Protocol Compliance
- Implements MCP 1.0 specification
- Uses stdio transport for communication
- Supports both Q CLI and Claude Code clients
- JSON Schema validation with `additionalProperties: false`

### Error Handling
- Graceful API error handling with descriptive messages
- Server startup error handling with stderr logging
- HTTP status code propagation from Common Room API

## Core Features

### Tool Set (10 tools)
1. **commonroom_get_activity_types** - List all activity types
2. **commonroom_get_segments** - List audience segments  
3. **commonroom_get_tags** - List categorization tags
4. **commonroom_get_user** - Get user by email (includes dashboard_url)
5. **commonroom_add_activity** - Create activity record (auto-generates IDs)
6. **commonroom_add_user** - Create/update user record (auto-generates IDs)
7. **commonroom_get_dashboard_urls** - Get URLs for all dashboard sections
8. **commonroom_get_member_url** - Get individual member page URL
9. **commonroom_get_organization_url** - Get individual organization page URL
10. **commonroom_get_segment_url** - Get individual segment page URL

### Auto-Generated IDs
- **Activity IDs**: Format `activity_{timestamp}_{uuid8}` (e.g., `activity_1703123456_a1b2c3d4`)
- **User IDs**: Format `user_{timestamp}_{uuid8}` (e.g., `user_1703123456_e5f6g7h8`)
- Ensures uniqueness while remaining human-readable
- Common Room handles deduplication via email/social handles

### Flexible User Data
Accepts any combination of user fields:
- `email` - Email address (recommended for deduplication)
- `fullName` - Full name
- `companyName` - Company name  
- `titleAtCompany` - Job title
- `twitterUsername` - Twitter/X handle (without @)
- `linkedinUrl` - LinkedIn profile URL
- `githubUsername` - GitHub username
- `discordUsername` - Discord username
- `slackUserId` - Slack user ID
- `location` - Geographic location
- `bio` - User bio/description

### Data Operations
- **Read Operations**: Activity types, segments, tags, user lookup (with dashboard URLs)
- **Write Operations**: Add activities, add/update users (with auto-generated IDs)
- **URL Generation**: Dashboard URLs for members, organizations, segments
- **Bulk Operations**: Not implemented (use existing bulk_activities.py)

### API Endpoints Used
- `GET /activityTypes`
- `GET /segments` 
- `GET /tags`
- `GET /user/{email}` (enhanced with dashboard_url)
- `POST /source/{destinationSourceId}/activity`
- `POST /source/{destinationSourceId}/user`

### Dashboard URL Generation
- Member pages: `/member/{user_id}` (not `/members/`)
- Organization pages: `/organization/{org_id}`
- Segment pages: `/segment/{segment_id}`

## Technical Architecture

### Components
- `server.py` - MCP server implementation with ID generation
- `commonroom_client.py` - Common Room API client
- `openapi.json` - API specification reference

### Dependencies
- `mcp` - Model Context Protocol library
- `requests` - HTTP client for API calls
- `uuid` - ID generation
- `time` - Timestamp generation

### Configuration
- Environment-based API key management
- JSON configuration for MCP clients
- Cross-platform compatibility (macOS focus)

## User Experience Improvements

### Simplified Activity Creation
Users can now say:
```
Add blog post by chris@trag.dev with title "Fire TV Guide"
Add webinar by Sarah (sarah@company.com, Twitter: @sarahj) with title "Smart TV Development"
```

Instead of providing complex user objects with IDs.

### Automatic Deduplication
- Server generates unique IDs for each request
- Common Room merges users based on email/social handles
- No need to track or manage user IDs manually

## Limitations

### Not Implemented
- Bulk operations (use separate bulk tools)
- Real-time data streaming
- Webhook support
- Advanced query filtering
- Custom field management beyond basic read

### API Constraints
- Rate limiting handled by Common Room API
- Requires destination source ID for write operations
- Email-based user lookup only (no other identifiers)

## Version Compatibility
- Common Room API: v1 (community endpoints)
- MCP Protocol: 1.0
- Python: 3.8+
- Q CLI: Latest
- Claude Code: Latest
