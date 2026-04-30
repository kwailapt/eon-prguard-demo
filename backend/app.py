from flask import Flask, request, jsonify
from models import UserRepository
import os

app = Flask(__name__)
repo = UserRepository()

STRIPE_SECRET = os.environ.get('STRIPE_SECRET')

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    user = repo.find_by_id(int(user_id))
    return jsonify({'user': str(user)})

@app.route('/users')
def list_users():
    users = repo.list_all()
    return jsonify({'users': [str(u) for u in users]})

if __name__ == '__main__':
    app.run(debug=True)
# trigger PR Guard
# PR Guard
# PR Guard
# PR Guard
