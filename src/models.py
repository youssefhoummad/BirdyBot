from src import db



class Class(db.Model):
    # الطائفة = الطيور
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def __str__(self):
        return f"<Class {self.name}>"


class Order(db.Model):
    # الرتبة = الدجاجيات، لقلاقيات، زقزاقيات...
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def __str__(self):
        return f"<Class {self.name}>"


class Family(db.Model):
    # الرتبة = الدجاجيات، لقلاقيات، زقزاقيات...
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def __str__(self):
        return f"<Class {self.name}>"


class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(120))
    voice = db.Column(db.String(120))
    more_info = db.Column(db.String(120))

    def __str__(self):
        return f"<Bird {self.name}>"
