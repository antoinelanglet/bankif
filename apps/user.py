from flask import Flask, Blueprint, jsonify, request, render_template
from models import User, Token, Gif
from playhouse.shortcuts import model_to_dict
from hashlib import md5

app_user = Blueprint('app_user', __name__)

@app_user.route('/tokens', methods=['GET'])
def tokens():
    return jsonify({'data': list(Token.select().dicts())}), 201

@app_user.route('/users', methods=['GET'])
def users():
    return jsonify({'data': list(User.select().dicts()) }), 201

@app_user.route('/user/<id>', methods=['GET'])
def user(id):
    user = User.get(User.id == id)
    return jsonify({'data': model_to_dict(user) }), 201

@app_user.route('/signup', methods=['GET'])
def home_signup():
    return render_template('index.html', page='signup'), 201

@app_user.route('/new_user', methods=['POST'])
def user_new():
    params = request.form # Dict
    query = User.create(surname=params['surname'], lastname=params['lastname'], email=params['email'], password=md5(params['password']).hexdigest())
    query.save()
    return render_template('index.html', page='home', signup='success'), 201

@app_user.route('/users/<id>', methods=['PUT'])
def user_update(id):
    params = request.get_json() # Dict
    user = User.get(User.id == id)
    user.surname = params['surname']
    user.lastname = params['lastname']
    user.email = params['email']
    user.password = md5(params['password']).hexdigest()
    # query = User.update(email=params['email'], password=params['password'].where(User.id < id))
    user.save()
    return jsonify({'data': model_to_dict(user) }), 201

@app_user.route('/users/<id>', methods=['DELETE'])
def user_delete(id):
    params = request.get_json() # Dict
    user = User.get(User.id == id)
    user.delete_instance()
    return jsonify({'data': model_to_dict(user) }), 201
