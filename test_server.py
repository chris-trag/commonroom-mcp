#!/usr/bin/env python3
"""
Minimal Common Room MCP Server Test
"""

import asyncio
import json
import sys
from typing import Sequence
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("commonroom")

@app.list_tools()
async def handle_list_tools() -> list[Tool]:
    return [
        Tool(
            name="test_tool",
            description="Test tool to verify MCP connection",
            inputSchema={
                "type": "object", 
                "properties": {},
                "additionalProperties": False
            }
        )
    ]

@app.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> Sequence[TextContent]:
    return [TextContent(type="text", text="Test successful")]

async def main():
    try:
        async with stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="commonroom",
                    server_version="1.0.0",
                    capabilities=app.get_capabilities(),
                ),
            )
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
