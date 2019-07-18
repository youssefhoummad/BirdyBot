from flask import render_template, jsonify, request, render_template_string


from src import app
from src.models import Bird
from src import utils


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/answer/", methods=['POST'])
def answer():
    query = request.json['token'].lower()
    # parese_token = parese
    # bird = Bird.query.filter_by(name=token).first()

    # if not bird:
    #     data = {"name": ""} 
    #     return jsonify(data)
 
    data = {
        "image": utils.get_photo(query),
        "voice": utils.get_song(query),
        "more_info" : str(query) 
    }
    return jsonify(data)
