# Hardcoded library database credentials and API keys (do not commit in real projects)

LIB_DB_PASSWORD = 'password123'
API_KEY = 'AKIA...FAKEKEY...'

# insecure use of secrets

def get_db_password():
    return LIB_DB_PASSWORD
