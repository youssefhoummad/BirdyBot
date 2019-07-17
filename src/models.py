from src import db


class Category(db.Model):
    # الطائفة = الطيور
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def __str__(self):
        return f"<Category {self.name}>"


class Rank(db.Model):
    # الرتبة = الدجاجيات، لقلاقيات، زقزاقيات...
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('ranks', lazy=True))

    def __str__(self):
        return f"<Rank {self.name}>"


class Family(db.Model):
    # الرتبة = الدجاجيات، لقلاقيات، زقزاقيات...
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'), nullable=False)
    rank = db.relationship('Rank', backref=db.backref('families', lazy=True))

    def __str__(self):
        return f"<Family {self.name}>"


class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'), nullable=False)
    family = db.relationship('Family', backref=db.backref('birds', lazy=True))

    name = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(120))
    voice = db.Column(db.String(120))
    more_info = db.Column(db.String(120))

    def __str__(self):
        return f"<Bird {self.name}>"
