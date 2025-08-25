# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2025-08-25

### Added
- Dashboard URL generation feature
- `commonroom_get_dashboard_urls` tool for getting links to all dashboard sections
- Optional `COMMONROOM_BASE_URL` environment variable support
- Automatic .env file loading in client
- Enhanced error messaging when base URL not configured
- `dashboard_url` field automatically included in `get_user_by_email` responses

### Fixed
- Member URLs now use correct `/member/` path instead of `/members/`
- User lookup now properly handles API response structure with `ids` array

### Updated
- Documentation updated with dashboard URL setup instructions
- Examples include dashboard URL queries
- Installation guide covers new environment variable

## [1.0.0] - 2025-08-25

### Added
- Initial MCP server implementation
- Support for 6 Common Room API endpoints
- Claude Code and Amazon Q CLI compatibility
- Automatic OpenAPI spec version checking
- Comprehensive documentation (README, INSTALL, SPEC)
- Background version checking with update notifications
- Update script for OpenAPI spec maintenance

### Features
- `commonroom_get_activity_types` - List activity types
- `commonroom_get_segments` - List audience segments
- `commonroom_get_tags` - List tags
- `commonroom_get_user` - Get user by email
- `commonroom_add_activity` - Add activity record
- `commonroom_add_user` - Add/update user record

### Technical
- MCP 1.0 protocol compliance
- Environment-based API key management
- Comprehensive error handling
- JSON Schema validation
- Cross-platform compatibility
