from flask import Flask, request, render_template_string
import database
import utils
import secrets

app = Flask(__name__)

# Vulnerable to SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    # directly concatenating into query
    result = database.query("SELECT * FROM users WHERE id = %s" % user_id)
    return str(result)

# Vulnerable to reflected XSS
@app.route('/search')
def search():
    term = request.args.get('q', '')
    # unsafely rendering user input
    return render_template_string(f"<h1>Results for {term}</h1>")

# Vulnerable to command injection
@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    output = utils.run_ping(host)
    return '<pre>' + output + '</pre>'

if __name__ == '__main__':
    app.run(debug=True)
