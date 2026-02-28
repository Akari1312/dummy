# Vulnerable Flask Application

This sample project contains deliberate security vulnerabilities for testing detection tools. Do **not** deploy in production.

## Included Vulnerabilities

- **SQL Injection**: `app.get_user` concatenates user input into SQL queries.
- **Reflected XSS**: `app.search` injects user-supplied terms into HTML without escaping.
- **Command Injection**: `utils.run_ping` builds shell commands with unsanitized input.
- **Hardcoded Secrets**: `secrets.py` stores credentials in source code.
- **Insecure Database Access**: `database.query` and `database.insert_user` use raw string formatting.

## Files

- `app.py` - main Flask application
- `database.py` - database helper with insecure queries
- `utils.py` - utility functions showing command injection
- `secrets.py` - hardcoded credentials

Use this repository to experiment with static analysis, penetration testing, or educational exercises.