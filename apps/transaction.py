from flask import Flask, Blueprint, jsonify, request, render_template
from models import User, Token, Gif
from playhouse.shortcuts import model_to_dict
from hashlib import md5
from flask import send_file

app_transaction = Blueprint('app_transaction', __name__)

@app_transaction.route('/transaction', methods=['POST'])
def login():
    params = request.form # Dict
    sender_id = params['sender_id']
    receiver_id = params['receiver_id']
    gif_sent = params['gif_sent']
    gif = Gif.get(Gif.gif_name == gif_sent)
    gifs = list(Gif.select().dicts())
    users = list(User.select().dicts())

    try:
        sender = User.get(User.id == sender_id)
        try:
            token = Token.get(Token.user_id == sender.id)
            try:
                receiver = User.get(User.id == receiver_id)
                if gif.user_id == sender.id:
                    gif.user_id = receiver.id
                    gif.save()
                    return render_template('index.html', page='user', transaction='ok', gif_sent=gif, user=sender, gifs=gifs, users=users, receiver_gif=receiver), 201
                else:
                    return render_template('index.html', page='user', transaction='not_owner', user=sender, gifs=gifs, users=users), 201
            except:
                return render_template('index.html', page='user', transaction='no_receiver', user=sender, gifs=gifs, users=users), 201
        except:
            return render_template('index.html', page='user', transaction='no_token', user=sender, gifs=gifs, users=users), 201
    except:
        return render_template('index.html', page='user', transaction='no_user', user=sender, gifs=gifs, users=users), 201
