from flask import render_template, jsonify, request


from src import app
from src import utils


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/answer/", methods=['POST'])
def answer():
    query = request.json['token'].lower()
    # parese_token = parese
 
    data = {
        "image": utils.get_photo(query),
        "voice": utils.get_song(query),
        "more_info" : str(query) 
    }
    return jsonify(data)
