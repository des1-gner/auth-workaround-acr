import boto3
import hmac
import hashlib
import base64

USER_POOL_ID = '<your-user-pool>'
CLIENT_ID = '<your-client-id>'
USERNAME = '<your-username>'
PASSWORD = '<your-password>'

# Get the client secret from Cognito
cognito = boto3.client('cognito-idp', region_name='us-east-1')

client_details = cognito.describe_user_pool_client(
    UserPoolId=USER_POOL_ID,
    ClientId=CLIENT_ID
)

CLIENT_SECRET = client_details['UserPoolClient'].get('ClientSecret')

if not CLIENT_SECRET:
    print("ERROR: Client doesn't have a secret")
    exit(1)

# Calculate SECRET_HASH
def get_secret_hash(username):
    message = bytes(username + CLIENT_ID, 'utf-8')
    secret = bytes(CLIENT_SECRET, 'utf-8')
    dig = hmac.new(secret, msg=message, digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()

# Authenticate
try:
    response = cognito.initiate_auth(
        ClientId=CLIENT_ID,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': USERNAME,
            'PASSWORD': PASSWORD,
            'SECRET_HASH': get_secret_hash(USERNAME)
        }
    )
    
    token = response['AuthenticationResult']['IdToken']
    print(f"Token: {token}")
    print(f"\nUse this token to invoke the agent")
    
except Exception as e:
    print(f"Error: {e}")
