import boto3
from flask import request, jsonify
from .models import User
from . import db

ses = boto3.client('ses')

def send_email(to, subject, body):
    ses.send_email(
        Source='no-reply@gettingthingsdone.com',
        Destination={
            'ToAddresses': [to]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    send_email(email, 'Welcome to Getting Things Done!', 'Please confirm your email address to complete the signup process.')
    return jsonify({'message': 'A confirmation email has been sent to your email address.'}), 201

@app.route('/change_password', methods=['POST'])
def change_password():
    data = request.get_json()
    email = data['email']
    new_password = data['new_password']
    user = User.query.filter_by(email=email).first()
    if user:
        user.password = new_password
        db.session.commit()
        send_email(email, 'Your password has been changed', 'You have successfully changed your password.')
        return jsonify({'message': 'Your password has been changed.'}), 200
    else:
        return jsonify({'message': 'User not found.'}), 404
