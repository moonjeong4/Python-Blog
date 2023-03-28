from flask import jsonify, session
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from database import db


class User:
    def __init__(self, user_dict):

        self.name = user_dict.get('name')
        self.email = user_dict.get('email')
        self.password = user_dict.get('password')

    def start_session(self, user):

        session['logged_in'] = True
        session['user'] = user
        # convert to json
        # session['user'] = json.dumps(user, default=str)
        return jsonify(user), 200

    def signup(self):

        if db.users.find_one({"name": self.name}):
            return jsonify({"error": "User name already in use"}), 400

        user = {'name': self.name, 'email': self.email, 'password': self.password}

        result = db.users.insert_one(user)

        if result:
            user_id = result.inserted_id
            # this is dictionary format
            user = db.users.find_one({'_id': user_id})
            user['_id'] = str(user['_id'])
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def login(self):
        user = db.users.find_one({'name': self.name})
        if user and pbkdf2_sha256.verify(self.password, user['password']):
            user['_id'] = str(user['_id'])
            return self.start_session(user)
        return jsonify({'error': "Invalid login"}), 401
