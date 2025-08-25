#!/usr/bin/env python3
"""
Test URL generation functions for Common Room MCP
"""

import os
from commonroom_client import CommonRoomClient

def test_url_functions():
    """Test all URL generation functions"""
    
    # Set up test environment
    os.environ['COMMONROOM_KEY'] = 'test_key'
    os.environ['COMMONROOM_BASE_URL'] = 'https://app.commonroom.io/community/8683-amazon-developer'
    
    try:
        client = CommonRoomClient()
        
        # Test member URLs
        member_id = "226882839"
        
        # Test basic member URL
        member_url = client.get_member_url(member_id)
        expected_member = "https://app.commonroom.io/community/8683-amazon-developer/member/226882839"
        assert member_url == expected_member, f"Expected {expected_member}, got {member_url}"
        print(f"✓ Member URL: {member_url}")
        
        # Test member activity URL (via parameter)
        member_activity_url = client.get_member_url(member_id, show_activity=True)
        expected_activity = "https://app.commonroom.io/community/8683-amazon-developer/member/226882839/activity"
        assert member_activity_url == expected_activity, f"Expected {expected_activity}, got {member_activity_url}"
        print(f"✓ Member Activity URL (param): {member_activity_url}")
        
        # Test member activity URL (dedicated function)
        member_activity_url2 = client.get_member_activity_url(member_id)
        assert member_activity_url2 == expected_activity, f"Expected {expected_activity}, got {member_activity_url2}"
        print(f"✓ Member Activity URL (function): {member_activity_url2}")
        
        # Test organization URL
        org_id = "414214-td"
        org_url = client.get_organization_url(org_id)
        expected_org = "https://app.commonroom.io/community/8683-amazon-developer/organization/414214-td"
        assert org_url == expected_org, f"Expected {expected_org}, got {org_url}"
        print(f"✓ Organization URL: {org_url}")
        
        # Test segment URL
        segment_id = "5627821-combo-kepler-developer-outreach-for-unboxing"
        segment_url = client.get_segment_url(segment_id)
        expected_segment = "https://app.commonroom.io/community/8683-amazon-developer/segment/5627821-combo-kepler-developer-outreach-for-unboxing"
        assert segment_url == expected_segment, f"Expected {expected_segment}, got {segment_url}"
        print(f"✓ Segment URL: {segment_url}")
        
        print("\n🎉 All URL tests passed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_url_functions()
