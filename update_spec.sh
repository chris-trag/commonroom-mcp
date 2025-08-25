#!/bin/bash
# Update Common Room OpenAPI Specification

echo "🔄 Updating Common Room OpenAPI spec..."

# Backup current spec
if [ -f "openapi.json" ]; then
    cp openapi.json "openapi.json.backup.$(date +%Y%m%d_%H%M%S)"
    echo "📦 Backed up current spec"
fi

# Extract latest spec from Common Room docs
curl -s "https://api.commonroom.io/docs/community.html" | \
  grep -o '__redoc_state = {.*};' | \
  sed 's/__redoc_state = //' | \
  sed 's/;$//' | \
  jq '.spec.data' > openapi.json.new

# Verify the new spec is valid JSON
if jq empty openapi.json.new 2>/dev/null; then
    mv openapi.json.new openapi.json
    echo "✅ OpenAPI spec updated successfully"
    
    # Show version info
    VERSION=$(jq -r '.info.version // "unknown"' openapi.json)
    TITLE=$(jq -r '.info.title // "unknown"' openapi.json)
    echo "📋 Spec: $TITLE v$VERSION"
else
    rm -f openapi.json.new
    echo "❌ Failed to extract valid OpenAPI spec"
    exit 1
fi
