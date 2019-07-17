from flask import render_template, jsonify, request, render_template_string


from src import app
from src.models import Bird


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/answer/", methods=['POST'])
def answer():
    # TODO
    token = request.json['token']
    bird = Bird.query.filter_by(name=token).first()

    if not bird:
        data = {"name": ""} 
        return jsonify(data)

    data = {
        "category": bird.category.name,
        "rank": bird.rank.name,
        "family": bird.family.name,
        "name": bird.name,
        
        "image": bird.image,
        "voice": bird.voice,
        "more_info": bird.more_info,
    }
    return jsonify(data)
