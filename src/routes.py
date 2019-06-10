from flask import render_template, jsonify

from src import app
from src.models import Bird


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/result/<query>", methods=['GET', 'POST'])
def result(query):
    # TODO
    bird = Bird.query.filter_by(name=query).first()
    data = {
        "name": bird.name,
        "image": bird.image,
        "voice": bird.voice,
        "more": bird.more_info
    }
    return jsonify(data)
