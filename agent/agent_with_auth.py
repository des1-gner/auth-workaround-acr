from bedrock_agentcore import BedrockAgentCoreApp, RequestContext
import jwt
import json

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke_agent(payload, context: RequestContext):
    """
    Entry point that validates Authorization header and cognito:groups
    """
    try:
        user_input = payload.get("prompt", "Hello!")
        
        # Log all headers we receive
        app.logger.info(f"Request headers: {json.dumps(context.request_headers)}")
        
        # Get Authorization header
        auth_header = context.request_headers.get('Authorization', '')
        
        if not auth_header:
            app.logger.warning("No Authorization header found")
            return {
                "result": "❌ No Authorization header received",
                "headers_received": list(context.request_headers.keys()),
                "context_type": str(type(context))
            }
        
        if not auth_header.startswith('Bearer '):
            return {"result": "❌ Invalid Authorization header format"}
        
        # Extract and decode JWT token
        token = auth_header[7:]  # Remove 'Bearer ' prefix
        
        try:
            # Decode without verification (for demo - you should verify in production)
            decoded = jwt.decode(token, options={"verify_signature": False})
            app.logger.info(f"Decoded token claims: {json.dumps(decoded)}")
            
            # Check cognito:groups claim
            groups = decoded.get('cognito:groups', [])
            app.logger.info(f"User groups: {groups}")
            
            # Validate group membership
            required_group = 'DeveloperGroup'
            if required_group not in groups:
                return {
                    "result": f"❌ Access denied. User not in required group: {required_group}",
                    "user_groups": groups,
                    "user_sub": decoded.get('sub', 'unknown')
                }
            
            # User is authorized - process the request
            return {
                "result": f"✅ Authorized! Processed: {user_input}",
                "user_sub": decoded.get('sub'),
                "user_groups": groups,
                "token_issuer": decoded.get('iss'),
                "token_audience": decoded.get('aud')
            }
            
        except jwt.DecodeError as e:
            app.logger.error(f"JWT decode error: {e}")
            return {"result": f"❌ Invalid JWT token: {str(e)}"}
            
    except Exception as e:
        app.logger.error(f"Error in invoke_agent: {str(e)}")
        import traceback
        app.logger.error(traceback.format_exc())
        return {"result": f"❌ Error: {str(e)}"}

if __name__ == "__main__":
    app.run()
