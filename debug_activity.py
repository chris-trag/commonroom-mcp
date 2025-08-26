#!/usr/bin/env python3
"""
Debug the MCP server activity addition
"""

import uuid
import time
import json

def test_activity_format():
    """Test the activity format that should work"""
    
    # Create activity data with auto-generated IDs (like the server should do)
    activity_data = {
        "id": f"activity_{int(time.time())}_{str(uuid.uuid4())[:8]}",
        "activityType": "attended_gathering",
        "user": {
            "id": f"user_{int(time.time())}_{str(uuid.uuid4())[:8]}",
            "fullName": "Kourtney Meiss",
            "email": "kmeiss@amazon.com",
            "companyName": "Amazon"
        },
        "activityTitle": {
            "type": "text",
            "value": "AI/TX Meetup - August 2024"
        },
        "content": {
            "type": "text", 
            "value": "Attended AI/TX meetup in Austin focusing on AI developments and networking with local tech community"
        },
        "url": "https://lu.ma/aitx-aug25?tk=UwZ3Bf",
        "timestamp": "2024-08-26T23:00:00Z"
    }
    
    print("Generated activity data:")
    print(json.dumps(activity_data, indent=2))
    
    # Test with the client directly
    from commonroom_client import CommonRoomClient
    
    try:
        client = CommonRoomClient()
        result = client.add_activity(None, activity_data)
        print("Success!")
        print(f"Activity added: {result}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        if hasattr(e, 'response'):
            print(f"Response status: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
        return False

if __name__ == "__main__":
    test_activity_format()
