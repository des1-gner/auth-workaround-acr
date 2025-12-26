import requests
import json
import uuid

TOKEN = "<your-token-from-the-other-script>"

RUNTIME_ID = '<your-ac-runtime-id>'
ACCOUNT_ID = '<your-account-id>'
REGION = 'us-east-1'

url = f'https://bedrock-agentcore.{REGION}.amazonaws.com/runtimes/{RUNTIME_ID}/invocations'

session_id = str(uuid.uuid4())

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

payload = json.dumps({"prompt": "Test with OAuth token"})

params = {
    'runtimeSessionId': session_id,
    'qualifier': 'DEFAULT',
    'accountId': ACCOUNT_ID
}

try:
    response = requests.post(url, headers=headers, data=payload, params=params)
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:1000]}")
    
    if response.status_code == 200:
        try:
            result = response.json()
            print("\nParsed:")
            print(json.dumps(result, indent=2))
        except:
            pass
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
