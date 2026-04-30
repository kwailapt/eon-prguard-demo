from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

STRIPE_SECRET = "sk_live_abc123def456ghi789jkl"
STRIPE_PUBLISHABLE = "pk_test_xyz789"

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM users WHERE id = ?"
    result = conn.execute(query, (user_id,)).fetchone()
    return jsonify({'user': result})

@app.route('/users')
def list_users():
    conn = sqlite3.connect('users.db')
    result = conn.execute("SELECT * FROM users").fetchall()
    return jsonify({'users': result})

if __name__ == '__main__':
    app.run(debug=True)
