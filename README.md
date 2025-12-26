agent % agentcore configure -e ./agent_with_auth.py
Configuring Bedrock AgentCore...
✓ Using file: agent_with_auth.py

🏷️  Inferred agent name: agent_with_auth
Press Enter to use this name, or type a different one (alphanumeric without '-')
Agent name [agent_with_auth]:
✓ Using agent name: agent_with_auth

🔍 Detected dependency file: requirements.txt
Press Enter to use this file, or type a different path (use Tab for autocomplete):
Path or Press Enter to use detected dependency file: requirements.txt
✓ Using requirements file: requirements.txt

🚀 Deployment Configuration
Select deployment type:
  1. Direct Code Deploy (recommended) - Python only, no Docker required
  2. Container - For custom runtimes or complex dependencies
Choice [1]: 1

Select Python runtime version:
  1. PYTHON_3_10
  2. PYTHON_3_11
  3. PYTHON_3_12
  4. PYTHON_3_13
Choice [1]: 1
✓ Deployment type: Direct Code Deploy (python.3.10)

🔐 Execution Role
Press Enter to auto-create execution role, or provide execution role ARN/name to use existing
Execution role ARN/name (or press Enter to auto-create):
✓ Will auto-create execution role

🏗️  S3 Bucket
Press Enter to auto-create S3 bucket, or provide S3 URI/path to use existing
S3 URI/path (or press Enter to auto-create):
✓ Will auto-create S3 bucket

🔐 Authorization Configuration
By default, Bedrock AgentCore uses IAM authorization.
Configure OAuth authorizer instead? (yes/no) [yes]: yes

📋 OAuth Configuration
Enter OAuth discovery URL: <your-oauth-discovery-pool>
Enter allowed OAuth client IDs (comma-separated):
Enter allowed OAuth audience (comma-separated): <your-oauth-audience>
Enter allowed OAuth allowed scopes (comma-separated):
Enter allowed OAuth custom claims as JSON string (comma-separated): 
✓ OAuth authorizer configuration created

🔒 Request Header Allowlist
Configure which request headers are allowed to pass through to your agent.
Common headers: Authorization, X-Amzn-Bedrock-AgentCore-Runtime-Custom-*
Configure request header allowlist? (yes/no) [yes]: no

📋 Request Header Allowlist Configuration
Enter allowed request headers (comma-separated) [Authorization,X-Amzn-Bedrock-AgentCore-Runtime-Custom-*]: Authorization
✓ Request header allowlist configured with 1 headers
Configuring BedrockAgentCore agent: agent_with_auth

Memory Configuration
Tip: Use --disable-memory flag to skip memory entirely

✅ MemoryManager initialized for region: us-east-1
No existing memory resources found in your account

Options:
  • Press Enter to create new memory
  • Type 's' to skip memory setup

Your choice: s
✓ Skipping memory configuration
Memory disabled by user choice
Network mode: PUBLIC
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Configuration Success ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Agent Details                                                                                                                                                                                                                                                                                                       │
│ Agent Name: agent_with_auth                                                                                                                                                                                                                                                                                       │
│ Deployment: direct_code_deploy                                                                                                                                                                                                                                                                                      │
│ Region: us-east-1                                                                                                                                                                                                                                                                                                   │
│ Account: <redacted>                                                                                                                                                                                                                                                                                               │
│ Runtime: python3.10                                                                                                                                                                                                                                                                                                 │
│                                                                                                                                                                                                                                                                                                                     │
│ Configuration                                                                                                                                                                                                                                                                                                       │
│ Execution Role: Auto-create                                                                                                                                                                                                                                                                                         │
│ ECR Repository: N/A                                                                                                                                                                                                                                                                                                 │
│ Network Mode: Public                                                                                                                                                                                                                                                                                                │
│ S3 Bucket: Auto-create                                                                                                                                                                                                                                                                                              │
│ Authorization: OAuth (customJWTAuthorizer)                                                                                                                                                                                                                                                                          │
│                                                                                                                                                                                                                                                                                                                     │
│ Request Headers Allowlist: 1 headers configured                                                                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                                                     │
│ Memory: Disabled                                                                                                                                                                                                                                                                                                    │
│                                                                                                                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                                                     │
│ 📄 Config saved to: <redacted>                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                                                                     │
│ Next Steps:                                                                                                                                                                                                                                                                                                         │
│ agentcore launch                                                                                                                                                                                                                                                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
agent % agentcore launch
🚀 Launching Bedrock AgentCore (cloud mode - RECOMMENDED)...
   • Deploy Python code directly to runtime
   • No Docker required (DEFAULT behavior)
   • Production-ready deployment

💡 Deployment options:
   • agentcore deploy                → Cloud (current)
   • agentcore deploy --local        → Local development

Launching with direct_code_deploy deployment for agent 'agent_with_auth'

╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Deployment Success ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Agent Details:                                                                                                                                                                                                                                                                                                      │
│ Agent Name: agent_with_auth                                                                                                                                                                                                                                                                                        │
│ Agent ARN: <redacted>                                                                                                                                                                                                                   │
│ Deployment Type: Direct Code Deploy                                                                                                                                                                                                                                                                                 │
│                                                                                                                                                                                                                                                                                                                     │
│ 📦 Code package deployed to Bedrock AgentCore                                                                                                                                                                                                                                                                       │
│                                                                                                                                                                                                                                                                                                                     │
│ Next Steps:                                                                                                                                                                                                                                                                                                         │
│    agentcore status                                                                                                                                                                                                                                                                                                 │
│    agentcore invoke '{"prompt": "Hello"}'                                                                                                                                                                                                                                                                           │
│                                                                                                                                                                                                                                                                                                                     │
│ 📋 CloudWatch Logs:                                                                                                                                                                                                                                                                                                 │
│    <redacted> --log-stream-name-prefix "2025/12/26/[runtime-logs"                                                                                                                                                                                          │
│    <redacted> --log-stream-names "otel-rt-logs"                                                                                                                                                                                                            │
│                                                                                                                                                                                                                                                                                                                     │
│ 🔍 GenAI Observability Dashboard:                                                                                                                                                                                                                                                                                   │
│    https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#gen-ai-observability/agent-core                                                                                                                                                                                                                  │
│                                                                                                                                                                                                                                                                                                                     │
│ ⏱️  Note: Observability data may take up to 10 minutes to appear after first launch                                                                                                                                                                                                                                  │
│                                                                                                                                                                                                                                                                                                                     │
│ 💡 Tail logs with:                                                                                                                                                                                                                                                                                                  │
│    aws logs tail <redacted> --log-stream-name-prefix "2025/12/26/[runtime-logs" --follow                                                                                                                                                                   │
│    aws logs tail <redacted> --log-stream-name-prefix "2025/12/26/[runtime-logs" --since 1h                                                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
