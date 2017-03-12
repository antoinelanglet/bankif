from flask import Flask, Blueprint, jsonify, request, render_template
from models import User, Token, Gif
from playhouse.shortcuts import model_to_dict
from hashlib import md5

app_auth = Blueprint('app_auth', __name__)


@app_auth.route('/login', methods=['POST'])
def login():
    params = request.form # Dict
    email = params['email']
    pwd = md5(params['password']).hexdigest()
    try:
        user = User.get(User.email == email)
        if user.password == pwd:
            gifs = list(Gif.select().dicts())
            users = list(User.select().dicts())
            try:
                token = Token.get(Token.user_id == user.id)
                return render_template('index.html', page='user', user=user, gifs=gifs, users=users, token='0'), 201
            except:
                token_created = md5(str(user.id) + user.email).hexdigest()
                query = Token.create(token=token_created, user_id=user.id)
                query.save()
                return render_template('index.html', page='user', user=user, gifs=gifs, users=users, token='1'), 201
        else:
            return render_template('index.html', page='home', login='failed_pwd'), 201
    except:
        return render_template('index.html', page='home', login='failed_user'), 201
