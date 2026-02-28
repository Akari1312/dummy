# Hardcoded credentials and API keys (do not commit in real projects)

DB_PASSWORD = 'password123'
API_KEY = 'AKIA...FAKEKEY...'

# insecure use of secrets

def get_db_password():
    return DB_PASSWORD
