# Example Prompts

Test your Common Room MCP server with these sample queries:

## Basic Data Retrieval
```
Get all Common Room activity types
Show me Common Room segments
List all Common Room tags
What activity types are available in Common Room?
Get Common Room dashboard URLs
Show me links to all Common Room dashboard sections
```

## User Lookup
```
Get Common Room user data for chris@trag.dev
Look up laquigi@amazon.com in Common Room
Find user @giolaq on Common Room
```

## Analysis Queries
```
What Common Room segments exist for my team?
Show me all the tags available in Common Room
Which activity types would be good for developer evangelism?
```

## Adding Activities

**Simple blog post:**
```
Add a blog post activity to Common Room by chris@trag.dev with title "Fire TV Development Guide"
```

**Conference talk with social handles:**
```
Add a conference talk activity by john@company.com (Twitter: @johndev, GitHub: johnsmith) with title "React Native on Fire TV"
```

**Webinar with full user details:**
```
Add webinar activity by Sarah Johnson (sarah@startup.com, LinkedIn: linkedin.com/in/sarahjohnson, Company: TechStartup, Title: CTO) with title "Building Apps for Smart TVs"
```

**Article with minimal info:**
```
Add article activity by developer@example.com with title "Getting Started with Alexa Skills"
```

## Adding Users

**Basic user:**
```
Add user chris@trag.dev to Common Room
```

**User with social profiles:**
```
Add user john@company.com with Twitter @johndev and GitHub johnsmith to Common Room
```

**Complete user profile:**
```
Add user Sarah Johnson (sarah@startup.com, LinkedIn: linkedin.com/in/sarahjohnson, Company: TechStartup, Title: CTO, Location: Austin TX) to Common Room
```

## URL Generation
```
Get Common Room member URL for user ID 226882839
Show me the activity page for Common Room member 123456
Get organization URL for org ID 789
What's the URL for Common Room segment 456?
```

## Troubleshooting
```
Check if Common Room API is working
Test my Common Room connection
What tools are available for Common Room?
```

## Getting Started

Start with the **Basic Data Retrieval** queries first - they don't require any parameters and will quickly show if the MCP is working properly!

## User Data Fields Supported

When adding activities or users, you can provide any combination of:
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

The MCP will auto-generate unique IDs for both users and activities, while Common Room handles deduplication based on email and social handles.
