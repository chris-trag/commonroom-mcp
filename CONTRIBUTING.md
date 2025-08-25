# Contributing

This is a personal project for Common Room MCP integration. 

## Issues & Support

For Common Room platform issues, visit:
- [Common Room Documentation](https://docs.commonroom.io/)
- [Uncommon Community](https://www.commonroom.io/uncommon)
- [Common Room Contact](https://www.commonroom.io/contact/)

## Development

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Test with both Claude Code and Q CLI
5. Submit a pull request

## Testing

```bash
# Test API client
python -c "from commonroom_client import CommonRoomClient; print(CommonRoomClient().get_token_status())"

# Test version checker
python version_checker.py

# Test MCP server
python server.py
```
