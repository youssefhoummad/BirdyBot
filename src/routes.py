from flask import render_template, jsonify

from src import app


@app.route("/")
def index():
    return render_template('home.html')


# @app.route("/result/<query>", methods=['GET', 'POST'])
# def result(query):
#     # TODO
#     data = somefunc(query)
#     data = {
#         "data": [{
#             "city": "elkelaa",
#             "lat": 32.0481,
#             "lng": -7.4081
#         }]
#     }
#     return jsonify(data)
