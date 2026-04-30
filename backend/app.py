from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
@app.route('/search')
def search_user():
    name = request.args.get('name')
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE name = '{name}'"
    result = conn.execute(query).fetchone()
    return jsonify({'user': result})
if __name__ == '__main__':
    app.run(debug=True)
