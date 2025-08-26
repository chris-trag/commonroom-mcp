#!/usr/bin/env python3
"""
Common Room MCP Server
Compatible with Q CLI and Claude Code
"""

import asyncio
import json
import sys
import uuid
import time
from typing import Sequence
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from commonroom_client import CommonRoomClient
from version_checker import background_version_check

app = Server("commonroom")

@app.list_tools()
async def handle_list_tools() -> list[Tool]:
    return [
        Tool(
            name="commonroom_get_activity_types",
            description="Get all available Common Room activity types (article, webinar, presentation, etc.)",
            inputSchema={
                "type": "object", 
                "properties": {},
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_segments", 
            description="Get all Common Room audience segments for targeting and analysis",
            inputSchema={
                "type": "object", 
                "properties": {},
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_tags",
            description="Get all Common Room tags used for categorizing activities and users", 
            inputSchema={
                "type": "object", 
                "properties": {},
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_user",
            description="Get Common Room user profile and activity data by email address",
            inputSchema={
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "Email address of the user to look up"
                    }
                },
                "required": ["email"],
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_add_activity",
            description="Add a new activity record to Common Room (blog post, webinar, conference talk, etc.)",
            inputSchema={
                "type": "object", 
                "properties": {
                    "destination_source_id": {
                        "type": "string",
                        "description": "Common Room destination source ID for the activity"
                    },
                    "activity": {
                        "type": "object",
                        "description": "Activity data including activityType, user info, title, content, url, timestamp",
                        "additionalProperties": True
                    }
                },
                "required": ["activity"],
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_add_user",
            description="Add or update a user profile in Common Room",
            inputSchema={
                "type": "object",
                "properties": {
                    "destination_source_id": {
                        "type": "string",
                        "description": "Common Room destination source ID"
                    },
                    "user": {
                        "type": "object",
                        "description": "User data - provide any combination of email, social handles, name, company, etc.",
                        "properties": {
                            "email": {"type": "string", "description": "User email address"},
                            "fullName": {"type": "string", "description": "User's full name"},
                            "companyName": {"type": "string", "description": "User's company"},
                            "titleAtCompany": {"type": "string", "description": "User's job title"},
                            "twitterUsername": {"type": "string", "description": "Twitter/X username (without @)"},
                            "linkedinUrl": {"type": "string", "description": "LinkedIn profile URL"},
                            "githubUsername": {"type": "string", "description": "GitHub username"},
                            "discordUsername": {"type": "string", "description": "Discord username"},
                            "slackUserId": {"type": "string", "description": "Slack user ID"},
                            "location": {"type": "string", "description": "User location"},
                            "bio": {"type": "string", "description": "User bio/description"}
                        }
                    }
                },
                "required": ["user"],
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_dashboard_urls",
            description="Get URLs for all Common Room dashboard sections (home, segments, search, contacts, etc.). Requires COMMONROOM_BASE_URL in .env file.",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_member_url",
            description="Get URL for individual Common Room member page",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "description": "User ID for the member page"
                    },
                    "show_activity": {
                        "type": "boolean",
                        "description": "If true, returns URL to member's activity page instead of overview",
                        "default": False
                    }
                },
                "required": ["user_id"],
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_member_activity_url",
            description="Get URL for individual Common Room member activity page (more detailed than overview)",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "description": "User ID for the member activity page"
                    }
                },
                "required": ["user_id"],
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_organization_url", 
            description="Get URL for individual Common Room organization page",
            inputSchema={
                "type": "object",
                "properties": {
                    "org_id": {
                        "type": "string",
                        "description": "Organization ID for the organization page"
                    }
                },
                "required": ["org_id"],
                "additionalProperties": False
            }
        ),
        Tool(
            name="commonroom_get_segment_url",
            description="Get URL for individual Common Room segment page", 
            inputSchema={
                "type": "object",
                "properties": {
                    "segment_id": {
                        "type": "string",
                        "description": "Segment ID for the segment page"
                    }
                },
                "required": ["segment_id"],
                "additionalProperties": False
            }
        )
    ]

@app.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> Sequence[TextContent]:
    try:
        client = CommonRoomClient()
        
        if name == "commonroom_get_activity_types":
            result = client.get_activity_types()
        elif name == "commonroom_get_segments":
            result = client.get_segments()
        elif name == "commonroom_get_tags":
            result = client.get_tags()
        elif name == "commonroom_get_user":
            result = client.get_user_by_email(arguments["email"])
        elif name == "commonroom_add_activity":
            print(f"DEBUG: add_activity called with arguments: {arguments}", file=sys.stderr)
            # Auto-generate activity ID and user ID
            activity_data = arguments["activity"].copy()
            activity_data["id"] = f"activity_{int(time.time())}_{str(uuid.uuid4())[:8]}"
            
            # Auto-generate user ID and prepare user data
            user_data = activity_data["user"].copy()
            user_data["id"] = f"user_{int(time.time())}_{str(uuid.uuid4())[:8]}"
            activity_data["user"] = user_data
            
            print(f"DEBUG: Generated activity data: {activity_data}", file=sys.stderr)
            result = client.add_activity(arguments.get("destination_source_id"), activity_data)
        elif name == "commonroom_add_user":
            # Auto-generate user ID
            user_data = arguments["user"].copy()
            user_data["id"] = f"user_{int(time.time())}_{str(uuid.uuid4())[:8]}"
            
            result = client.add_user(arguments.get("destination_source_id"), user_data)
        elif name == "commonroom_get_dashboard_urls":
            result = client.get_dashboard_urls()
        elif name == "commonroom_get_member_url":
            show_activity = arguments.get("show_activity", False)
            result = {"url": client.get_member_url(arguments["user_id"], show_activity)}
        elif name == "commonroom_get_member_activity_url":
            result = {"url": client.get_member_activity_url(arguments["user_id"])}
        elif name == "commonroom_get_organization_url":
            result = {"url": client.get_organization_url(arguments["org_id"])}
        elif name == "commonroom_get_segment_url":
            result = {"url": client.get_segment_url(arguments["segment_id"])}
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    except Exception as e:
        error_msg = f"Common Room API Error: {str(e)}"
        return [TextContent(type="text", text=error_msg)]

async def main():
    # Handle both stdio and potential other transports
    try:
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, app.create_initialization_options())
    except Exception as e:
        import traceback
        print(f"Server error: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
