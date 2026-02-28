# Vulnerable Library Booking System

This sample project simulates a rudimentary library booking web application. It is intentionally riddled with security flaws so that you can experiment with static analysis, penetration testing, or educational exercises. **Do not** use this code in any real deployment.

## System Description

The application allows visitors to look up book records, perform text searches, and trigger reminders for borrowers. Books are stored in a SQLite database and external utilities are invoked for notification messages. The implementation is simplistic and insecure—all vulnerabilities are deliberate and serve as teaching points.

## Included Vulnerabilities

- **SQL Injection**: `app.get_book` directly concatenates user-supplied book IDs into SQL queries.
- **Reflected XSS**: `app.search_books` renders unescaped search terms into HTML responses.
- **Command Injection**: `utils.run_notification` constructs shell commands from user input.
- **Hardcoded Secrets**: `secrets.py` contains plaintext database passwords and API keys.
- **Insecure Database Access**: `database.query` and `database.insert_book` use raw string formatting instead of parameterized statements.

## Files

- `app.py` - main Flask application with vulnerable endpoints
- `database.py` - database helper with insecure functions for book records
- `utils.py` - utility functions demonstrating command injection
- `secrets.py` - hardcoded credentials

Use this repository responsibly for testing and learning; never deploy it publicly.

Use this repository to experiment with static analysis, penetration testing, or educational exercises.