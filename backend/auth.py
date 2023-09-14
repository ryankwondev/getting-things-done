from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from .models import User

def create_token(user_id):
    access_token = create_access_token(identity=user_id)
    return access_token

def verify_token(token):
    try:
        user_id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['identity']
    except jwt.ExpiredSignatureError:
        return None
    return user_id

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_token(user.id)
    return jsonify(access_token=access_token), 200
