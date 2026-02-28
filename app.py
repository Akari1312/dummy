from flask import Flask, request, render_template_string
import database
import utils
import secrets

app = Flask(__name__)

# Vulnerable to SQL Injection
@app.route('/book')
def get_book():
    book_id = request.args.get('id')
    # directly concatenating into query without parameterization
    result = database.query("SELECT * FROM books WHERE id = %s" % book_id)
    return str(result)

# Vulnerable to reflected XSS
@app.route('/search')
def search_books():
    term = request.args.get('q', '')
    # unsafely rendering user input in search results
    return render_template_string(f"<h1>Search results for {term}</h1>")

# Vulnerable to command injection
@app.route('/notify')
def notify():
    user = request.args.get('user', '')
    output = utils.run_notification(user)
    return '<pre>' + output + '</pre>'

if __name__ == '__main__':
    app.run(debug=True)
