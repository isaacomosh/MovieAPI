from flask import Blueprint,request,jsonify
from app.models import Movie
from app import db
movie_bp=Blueprint("movies",__name__)

#get all movies
2
@movie_bp.route("/movies",methods=["GET"])
def get_movies():
    movies=Movie.query.all()
    return jsonify([movie.to_dict()for movie in movies])

#get single movie
@movie_bp.route("/movies/<int:id>",methods=["GET"])
def get_movie(id):
    movie=Movie.query.get_or_404(id)
    return jsonify(movie.to_dict())

#add movie
@movie_bp.route("/movies",methods=["POST"])
def add_movie():
    data=request.get_json()

    movie=Movie(title=data["title"],genre=data.get("genre"),
        director=data.get("director"),
        release_year=data.get("release_year"),
        rating=data.get("rating"),
        description=data.get("description"))

    db.session.add(movie)
    db.session.commit()

    return jsonify(movie.to_dict()), 201

#update movie
