from flask import render_template

from src import app
from src import forms


@app.route("/", methods=['GET', 'POST'])
def index():
    form = forms.SearchForm()
    return render_template('home.html', form=form, addresse=None)
