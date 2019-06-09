from src import db



class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(120))
    voice = db.Column(db.String(120))
    more_info = db.Column(db.String(120))

    def __repr__(self):
        return '<Bird %r>' %self.name
