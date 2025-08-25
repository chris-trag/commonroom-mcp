#!/usr/bin/env python3
"""
Common Room API Version Checker
Checks for updates to the OpenAPI spec after server startup
"""

import asyncio
import json
import re
import requests
import hashlib
from datetime import datetime
from typing import Optional

class VersionChecker:
    def __init__(self, current_spec_path: str = "openapi.json"):
        self.current_spec_path = current_spec_path
        self.docs_url = "https://api.commonroom.io/docs/community.html"
    
    def get_current_spec_hash(self) -> Optional[str]:
        """Get hash of current OpenAPI spec"""
        try:
            with open(self.current_spec_path, 'r') as f:
                content = f.read()
                return hashlib.md5(content.encode()).hexdigest()
        except FileNotFoundError:
            return None
    
    def fetch_latest_spec(self) -> Optional[dict]:
        """Extract latest OpenAPI spec from Common Room docs"""
        try:
            response = requests.get(self.docs_url, timeout=10)
            response.raise_for_status()
            
            # Extract __redoc_state from HTML
            match = re.search(r'__redoc_state = ({.*?});', response.text, re.DOTALL)
            if not match:
                return None
            
            state = json.loads(match.group(1))
            return state.get('spec', {}).get('data')
        
        except Exception:
            return None
    
    def check_for_updates(self) -> dict:
        """Check if there's a newer version available"""
        current_hash = self.get_current_spec_hash()
        latest_spec = self.fetch_latest_spec()
        
        if not latest_spec:
            return {"status": "error", "message": "Could not fetch latest spec"}
        
        latest_hash = hashlib.md5(json.dumps(latest_spec, sort_keys=True).encode()).hexdigest()
        
        if current_hash != latest_hash:
            return {
                "status": "update_available",
                "message": "New Common Room API spec available",
                "current_hash": current_hash,
                "latest_hash": latest_hash,
                "update_command": "curl -s 'https://api.commonroom.io/docs/community.html' | grep -o '__redoc_state = {.*};' | sed 's/__redoc_state = //' | sed 's/;$//' | jq '.spec.data' > openapi.json"
            }
        
        return {"status": "up_to_date", "message": "OpenAPI spec is current"}

async def background_version_check():
    """Background task to check for updates periodically"""
    await asyncio.sleep(30)  # Wait 30s after server start
    
    checker = VersionChecker()
    result = checker.check_for_updates()
    
    if result["status"] == "update_available":
        print(f"🔄 UPDATE AVAILABLE: {result['message']}")
        print(f"   Current: {result['current_hash'][:8]}...")
        print(f"   Latest:  {result['latest_hash'][:8]}...")
        print(f"   Update:  {result['update_command']}")
    elif result["status"] == "up_to_date":
        print(f"✅ OpenAPI spec is up to date")
    else:
        print(f"⚠️  Could not check for updates: {result['message']}")

if __name__ == "__main__":
    # Test the checker
    checker = VersionChecker()
    result = checker.check_for_updates()
    print(json.dumps(result, indent=2))
