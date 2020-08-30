import os
import models
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth, get_token_auth_header
from flask import Flask, request, abort, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship, aliased
import json
from flask_cors import CORS
import random
import inspect
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# Pagination

MOVIES_PER_PAGE = 10


def paginate_movies(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * MOVIES_PER_PAGE
    end = start + MOVIES_PER_PAGE

    movies = [movie.format() for movie in selection]
    current_movies = movies[start:end]

    return current_movies


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # -------------- CORS Headers

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    # --------------  Main Page

    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify("FSND - Capstone Project")

    # -------------- GET - Movies

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies():
        page = request.args.get('page', default=1, type=int)
        movies = Movie.query.order_by(Movie.id).all()
        page_of_movies = Movie.query.order_by(Movie.id).\
            paginate(page, MOVIES_PER_PAGE).items
        actors = Actor.query.all()

        if len(movies) == 0:
            abort(404)

        else:
            return jsonify({
                'success': True,
                'movies': [movie.format()
                           for movie in page_of_movies],
                'total_movies': len(movies),
                'actors': {actor.format()['id']: actor.format()['name']
                           for category in categories},
                'current_category': None,
            })

    # -------------- GET - Actors

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors():
        actors = Actor.query.order_by(Actor.id).all()
        formatted_actors = \
            {Actor.id: Actor.name for Actor in actors}

        return jsonify({
            'success': True,
            'actor': formatted_actors
        })

    # -------------- PATCH - Actors

    @app.route('/actors', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(actor_id):
        body = request.get_json()

        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            if actor is None:
                abort(404)

            actor.update()

            return jsonify({
                'success': True,
                'actor': actor
            })
        except Exception:
            abort(422)

    # -------------- PATCH - Movies

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(movie_id):
        body = request.get_json()

        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)

            movie.update()

            return jsonify({
                'success': True,
                'movie': movie.id
            })
        except Exception:
            abort(422)

    # -------------- POST - Actor

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(jwt):
        x = request.get_json()
        actorss = Actor(name=x['name'], gender=x['gender'], age=x['age'])
        actorss.insert()
        return jsonify({
            'success': True,
            'actors': actorss
        }), 200

    # -------------- POST - Movies

    @ app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(jwt):
        x = request.get_json()
        moviess = Movie(title=x['title'], release_date=x['release_date'])
        moviess.insert()
        return jsonify({
            'success': True,
            'movies': moviess
        }), 200

    # -------------- DELETE - Actor

    @ app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(actor_id):
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'deleted': actor_id,
            })

        except:
            abort(422)

    # -------------- DELETE - Movie

    @ app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(movie_id):
        try:
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'deleted': movie_id,
            })

        except:
            abort(422)

    # -------------- Error Handlers

    @ app.errorhandler(500)
    def internal_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @ app.errorhandler(422)
    def unprocessable_request(error):
        return jsonify({
            'error': 422,
            'success': False,
            'message': 'Unprocessable Request'
        }), 422

    @ app.errorhandler(405)
    def not_found(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @ app.errorhandler(404)
    def not_found(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @ app.errorhandler(400)
    def bad_request(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(AuthError)
    def autherror(error):
        print(error)
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
