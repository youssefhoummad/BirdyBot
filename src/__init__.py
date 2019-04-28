from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY'] = 'f2c80b32f536165d6a57ed9cb08a84a4'




from src import routes
