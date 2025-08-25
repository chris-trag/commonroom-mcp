#!/usr/bin/env python3
"""
Common Room API Client for MCP Server
Clean implementation based on latest OpenAPI spec
"""

import json
import requests
import os
from typing import List, Dict, Any, Optional

# Load .env file if it exists
def load_env():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, '.env')
    
    try:
        with open(env_path, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    except FileNotFoundError:
        pass

load_env()

class CommonRoomClient:
    def __init__(self):
        self.api_key = os.getenv('COMMONROOM_KEY')
        if not self.api_key:
            raise ValueError("COMMONROOM_KEY environment variable required")
        
        self.base_url = "https://api.commonroom.io/community/v1"
        self.dashboard_base_url = os.getenv('COMMONROOM_BASE_URL')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def get_token_status(self) -> Dict:
        """Get API token status"""
        response = requests.get(f"{self.base_url}/api-token-status", headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_activity_types(self) -> List[Dict]:
        """Get all activity types"""
        response = requests.get(f"{self.base_url}/activityTypes", headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_segments(self) -> List[Dict]:
        """Get all segments"""
        response = requests.get(f"{self.base_url}/segments", headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_segment(self, segment_id: str) -> Dict:
        """Get specific segment"""
        response = requests.get(f"{self.base_url}/segments/{segment_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_tags(self) -> List[Dict]:
        """Get all tags"""
        response = requests.get(f"{self.base_url}/tags", headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_user_by_email(self, email: str) -> Dict:
        """Get user by email"""
        response = requests.get(f"{self.base_url}/user/{email}", headers=self.headers)
        response.raise_for_status()
        user_data = response.json()
        
        # Add dashboard URL if we have the base URL configured and user IDs
        if self.dashboard_base_url and 'ids' in user_data and user_data['ids']:
            user_id = user_data['ids'][0]  # Use first ID
            user_data['dashboard_url'] = self.get_member_url(str(user_id))
        
        return user_data
    
    def add_activity(self, destination_source_id: str, activity_data: Dict) -> Dict:
        """Add activity to destination source"""
        url = f"{self.base_url}/source/{destination_source_id}/activity"
        response = requests.post(url, headers=self.headers, json=activity_data)
        response.raise_for_status()
        return response.json()
    
    def add_user(self, destination_source_id: str, user_data: Dict) -> Dict:
        """Add user to destination source"""
        url = f"{self.base_url}/source/{destination_source_id}/user"
        response = requests.post(url, headers=self.headers, json=user_data)
        response.raise_for_status()
        return response.json()
    
    def get_custom_fields(self) -> List[Dict]:
        """Get custom fields"""
        response = requests.get(f"{self.base_url}/members/customFields", headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_dashboard_urls(self) -> Dict[str, str]:
        """Get dashboard URLs for all sections"""
        if not self.dashboard_base_url:
            raise ValueError("COMMONROOM_BASE_URL not configured. Add it to your .env file (e.g., https://app.commonroom.io/community/your-community-id)")
        
        sections = {
            "home": f"{self.dashboard_base_url}/home",
            "segments": f"{self.dashboard_base_url}/segments", 
            "search": f"{self.dashboard_base_url}/search",
            "contacts": f"{self.dashboard_base_url}/members",
            "organizations": f"{self.dashboard_base_url}/organizations",
            "prospector": f"{self.dashboard_base_url}/prospector",
            "activity": f"{self.dashboard_base_url}/activities",
            "team_alerts": f"{self.dashboard_base_url}/alerts",
            "workflows": f"{self.dashboard_base_url}/workflows",
            "reporting": f"{self.dashboard_base_url}/reports",
            "settings": f"{self.dashboard_base_url}/settings"
        }
        return sections
    
    def get_member_url(self, user_id: str) -> str:
        """Get URL for individual member page"""
        if not self.dashboard_base_url:
            raise ValueError("COMMONROOM_BASE_URL not configured. Add it to your .env file")
        return f"{self.dashboard_base_url}/member/{user_id}"
    
    def get_organization_url(self, org_id: str) -> str:
        """Get URL for individual organization page"""
        if not self.dashboard_base_url:
            raise ValueError("COMMONROOM_BASE_URL not configured. Add it to your .env file")
        return f"{self.dashboard_base_url}/organization/{org_id}"
    
    def get_segment_url(self, segment_id: str) -> str:
        """Get URL for individual segment page"""
        if not self.dashboard_base_url:
            raise ValueError("COMMONROOM_BASE_URL not configured. Add it to your .env file")
        return f"{self.dashboard_base_url}/segment/{segment_id}"
