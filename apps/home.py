from flask import Flask, Blueprint, jsonify, request, render_template
from models import User, Token, Gif

app_home = Blueprint('app_home', __name__)

@app_home.route('/', methods=['GET'])
def home():
    return render_template('index.html', page='home'), 201
