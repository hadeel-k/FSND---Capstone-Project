# FSND---Capstone

# Casting Agency Project

## About The Project

This is the final project of Udacity's Connect Intensive - Full-Stack Developer Nanodegree. It's to use all of the concepts and the skills taught in the courses to build an API from start to finish and host it.

The Casting Agency project details exactly how the API should be structured: models, attributes, endpoints, roles, permissions, and tests.

It models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Models:

Movies with attributes title and release date
Actors with attributes name, age and gender

### Endpoints:

GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

### Roles:

##### Casting Assistant

Can view actors and movies

##### Casting Director

All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies

##### Executive Producer

All permissions a Casting Director has and…
Add or delete a movie from the database

### Tests:

One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

#### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

To run the server, execute:

```bash
python3 app.py
```

We can now also open the application via Heroku using the URL:
https://fsnd-hadeel.herokuapp.com/

## Data Modeling

#### Models.py

The schema for the database and helper methods to simplify API behavior are in models.py:

- There are two tables created: Movies, and Actors
- The Movies table is used to view, add, delete, and modify movies.
- The Actors table is used to view, add, delete, and modify actors.

## API Reference

### Error Handling:

Errors are returned as JSON objects in the following format:

```bash
    {
    "error": 404,
    "message": "resource not found",
    "success": false
    }
```

The API will return four error types when requests fail:

- 404: Resource Not Found
- 422: Unprocessable Request
- 400: Bad Request
- 500: Internal Server Error

### Endpoints

GET '/actors'
GET '/movies'
POST '/actors'
POST '/movies'
PATCH '/actors/[actor_id]'
PATCH '/movies/[movie_id]'
DELETE '/actors/[actor_id]'
DELETE '/movies/[movie_id]'

#### GET '/actors'
**General**
- Returns a list of all actors added to the database.
- **Sample Request:**
  curl https://fsnd-hadeel.herokuapp.com/actors -H"Authorization: Bearer <Token>"
- **Sample Response:**

```bash
    {
  "actor": {
    "1": "John Doe",
    "2": "Jane Doe",
    "3": "Jana Doe"
  },
  "success": true
}
```

#### GET '/movies'
**General**
- Returns a list of all movies added to the database.
- **Sample Request:**
  curl https://fsnd-hadeel.herokuapp.com/movies -H"Authorization: Bearer <Insert_Token_Here>"
- **Sample Response:**

```bash

    {
    "movies": [
        {
            "id": 1,
            "release_date": "Thu, 20 Feb 2020 00:00:00 GMT",
            "title": "The First Movie"
        },
        {
            "id": 2,
            "release_date": "Sat, 10 Oct 2020 00:00:00 GMT",
            "title": "The Secound Movie"
        },
        {
            "id": 3,
            "release_date": "Sat, 10 Oct 2020 00:00:00 GMT",
            "title": "The Secound Movie"
        }
    ],
    "success": true
    }

```

#### POST '/actors'
**General**
- Used to add a new actor to the database.
- **Sample Request:**
  curl -X POST https://fsnd-hadeel.herokuapp.com/actors -H "Authorization: Bearer <Insert_Token_Here> -H "Content-Type: application/json" -d '{\"name\":\"Denzel Washington\", \"gender\":\"Male\", \"age\":\"65\"}'
- **Sample Response:**

```bash
    {
    "id": 5,
    "name": "Denzel Washington",
    "age": 65,
    "gender": "Male",
    }
```

#### POST '/movies'
**General**
- Used to add a new movie to the database.
- **Sample Request:**
  curl -X POST https://fsnd-hadeel.herokuapp.com/movies -H "Authorization: Bearer <Insert_Token_Here> -H "Content-Type: application/json" -d '{\"title\":\"The Fifth Movie\", \"release_date\":\"Sat, 10 Oct 2022 00:00:00 GMT\"}'
- **Sample Response:**

```bash
    {
    "id": 6,
    "release_date": "Sun, 20 Feb 2022 00:00:00 GMT",
    "title": "The Fifth Movie"
        }
```

#### PATCH '/movies/[movie_id]'
**General**
- Used to modify a movie using the movie ID
- **Sample Request:**
```bash
curl https://fsnd-hadeel.herokuapp.com//movies/3 -X PATCH -H"Authorization: Bearer <Insert_Token_Here>" -H"Content-Type: application/json" -d"{\"title\":\"The Third Movie\", \"release_date\":\"2021-01-01 00:00:00 GMT\"}'
```
- **Sample Response:**

```bash
{
  "movie": [
    {
      "id": 3,
      "release_date": "Thu, 20 Feb 2020 00:00:00 GMT",
      "title": "The Third Movie"
    }
    ],
  "success": true
}
```

#### PATCH '/actors/[actor_id]'
**General**
- Used to modify an actor using the actor ID.
- **Sample Request:**
```bash
curl https://fsnd-hadeel.herokuapp.com//actors/6 -X PATCH -H"Authorization: Bearer <Insert_Token_Here>" -H"Content-Type: application/json" -d"{\"name\":\"Scarlett Johansson\", \"gender\":\"Female\", \"age\":\"35\"}"
```
- **Sample Response:**
```bash

    {
    "actor": [
        {
        "name": "Scarlett Johansson",
        "gender": "Female",
        "age": "35"
        }
        ],
    "success": true
    }

```

#### DELETE '/actors/[actor_id]'
**General**
- Used to delete an actor from the database.
- **Sample Request:**
```bash
curl https://fsnd-hadeel.herokuapp.com//actors/5 -X DELETE -H"Authorization: Bearer <Insert_Token_Here>"
```
- **Sample Response:**

```bash
{
    "success": true,
    "delete": 5
}

```

#### DELETE '/movies/[movie_id]'
**General**
- Used to delete a movie from the database.
- **Sample Request:**
```bash
curl https://fsnd-hadeel.herokuapp.com//movies/5 -X DELETE -H"Authorization: Bearer <Insert_Token_Here>"
```
- **Sample Response:**

```bash
{
    "success": true,
    "delete": 5
}

```
