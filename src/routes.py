from flask import render_template, request, url_for, redirect
import wikipedia

from src import app
from src import forms



wikipedia.set_lang("ar")



@app.route("/", defaults={'addresse': None})
@app.route("/<string:addresse>")
def index(addresse):
    form = forms.SearchForm()
    summary = wikipedia.summary(addresse, sentences=1)
    # if form.validate_on_submit():
    #     addresse=form.search.data
    #     return redirect(url_for('index', addresse=addresse,  =))
    return render_template('home.html', form=form, addresse=addresse, summary=summary)
