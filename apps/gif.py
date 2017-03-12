from flask import Flask, Blueprint, jsonify, request, render_template
from models import User, Token, Gif
from playhouse.shortcuts import model_to_dict
from hashlib import md5

app_gif = Blueprint('app_gif', __name__)

@app_gif.route('/gifs', methods=['GET'])
def gifs():
    return jsonify({'data': list(Gif.select().dicts()) }), 201

@app_gif.route('/gif/<id>', methods=['GET'])
def gif(id):
    gif = Gif.get(Gif.id == id)
    return jsonify({'data': model_to_dict(gif) }), 201

@app_gif.route('/gifs', methods=['POST'])
def gif_new():
    params = request.get_json() # Dict
    query = Gif.create(gif_url=params['gif_url'], gif_name=params['gif_name'], user_id=params['user_id'])
    query.save()
    return jsonify({'data': model_to_dict(query) }), 201

@app_gif.route('/gifs/<id>', methods=['PUT'])
def gif_update(id):
    params = request.get_json() # Dict
    gif = Gif.get(Gif.id == id)
    gif.gif_url = params['gif_url']
    gif.gif_name = params['gif_name']
    gif.user_id = params['user_id']
    # query = Gif.update(email=params['email'], password=params['password'].where(Gif.id < id))
    gif.save()
    return jsonify({'data': model_to_dict(gif) }), 201

@app_gif.route('/gifs/<id>', methods=['DELETE'])
def gif_delete(id):
    params = request.get_json() # Dict
    gif = Gif.get(Gif.id == id)
    gif.delete_instance()
    return jsonify({'data': model_to_dict(gif) }), 201
