from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    favorites = db.relationship('Favorite', backref='user')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "favorites": self.favorites,

            # do not serialize the password, its a security breach
        }
    

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    favorites = db.relationship('Favorite', backref='planet')

    def __repr__(self):
        return '<Planets %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hair_color= db.Column(db.String(250), nullable=True)
    gender= db.Column(db.String(250), nullable=True)
    birth_year= db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(50), unique=False, nullable=False)
    favorites = db.relationship('Favorite', backref='person')

    def __repr__(self):
        return '<People %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
        }


class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(50), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(50), unique=False, nullable=False)
    favorites = db.relationship('Favorite', backref='starship')

    def __repr__(self):
        return '<Starship %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "cargo_capacity": self.cargo_capacity,
        }

    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    favoriteStarshipId = db.Column(db.Integer, db.ForeignKey('starship.id'), nullable=True)
    favoritePersonId = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    favoritePlanetId = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    
    def __repr__(self):
            return '<Favorites %r>' % self.id
    def serialize(self):
        return {
            "id_favorito": self.id,
            "user_id": self.user_id,
            "favoritePlanetId": self.favoritePlanetId,
            "favoritePersonId": self.favoritePersonId,
            "favoriteStarshipId": self.favoriteStarshipId
        }