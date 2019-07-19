from flask import render_template, jsonify, request


from src import app
from src.utils import get_photo, get_song, is_arabic, translat


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/answer/", methods=['POST'])
def answer():
    query = request.json['token'].lower()
    if is_arabic(query):
        query = translat(query)

    # parese_token = parese
 
    data = {
        "image": get_photo(query),
        "voice": get_song(query),
        "more_info" : str(query) 
    }
    return jsonify(data)
