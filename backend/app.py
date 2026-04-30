from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# VULNERABILITY: SQL injection (will be fixed in PR #1)
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM users WHERE id = " + user_id
    result = conn.execute(query).fetchone()
    return jsonify({'user': result})

# VULNERABILITY: missing error handling
@app.route('/users')
def list_users():
    conn = sqlite3.connect('users.db')
    result = conn.execute("SELECT * FROM users").fetchall()
    return jsonify({'users': result})

if __name__ == '__main__':
    app.run(debug=True)
