from app.init import db

class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150),nullable=False)
    genre=db.Column(db.String(100))
    director=db.Column(db.String(100))
    release_year=db.Column(db.Integer)
    rating=db.Column(db.Float)
    description=db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "director": self.director,
            "release_year": self.release_year,
            "rating": self.rating,
            "description": self.description
        }