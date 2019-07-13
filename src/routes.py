from flask import render_template, jsonify, request, render_template_string


from src import app
from src.models import Bird


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/answer", methods=['POST'])
def answer():
    # TODO
    token = request.json['token']

    # bird = Bird.query.filter_by(name=query).first()

    answer = render_template('_answer.html', content="after token")
    answer = render_template_string(answer)

    data = {
        "answer":answer,
    }
    return jsonify(data)
