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
DELETE '/actors/[question_id]''
DELETE '/movies/[question_id]''
POST '/actors'
POST '/movies'
PATCH '/actors/[question_id]''
PATCH '/movies/[question_id]''


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
curl https://fsnd-hadeel.herokuapp.com/movies -H"Authorization: Bearer <Token>"
- **Sample Response:**

```bash

    {
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "current_category": null, 
    "questions": [
        {
        "answer": "Apollo 13", 
        "category": 5, 
        "difficulty": 4, 
        "id": 2, 
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
        "answer": "Tom Cruise", 
        "category": 5, 
        "difficulty": 4, 
        "id": 4, 
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
        "answer": "Maya Angelou", 
        "category": 4, 
        "difficulty": 2, 
        "id": 5, 
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
        "answer": "Edward Scissorhands", 
        "category": 5, 
        "difficulty": 3, 
        "id": 6, 
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
        "answer": "Muhammad Ali", 
        "category": 4, 
        "difficulty": 1, 
        "id": 9, 
        "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
        "answer": "Brazil", 
        "category": 6, 
        "difficulty": 3, 
        "id": 10, 
        "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
        "answer": "Uruguay", 
        "category": 6, 
        "difficulty": 4, 
        "id": 11, 
        "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
        "answer": "George Washington Carver", 
        "category": 4, 
        "difficulty": 2, 
        "id": 12, 
        "question": "Who invented Peanut Butter?"
        }, 
        {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
        }, 
        {
        "answer": "The Palace of Versailles", 
        "category": 3, 
        "difficulty": 3, 
        "id": 14, 
        "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ], 
    "success": true, 
    "total_questions": 19
    }

```


#### GET '/categories/[category_id]/questions'

**General**
- Fetches a list of questions for a chosen category in which the keys are the category ids and the value is the corresponding string of questions.
- Returns a paginated lists (10 questions per page) of questions according to the chosen category with it's answers, category, and difficulty score.
- **Sample Request:**
curl http://127.0.0.1:5000/categories/3/questions
- **Sample Response:**

```bash
    {
    "current_category": "Geography", 
    "questions": [
        {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
        }, 
        {
        "answer": "The Palace of Versailles", 
        "category": 3, 
        "difficulty": 3, 
        "id": 14, 
        "question": "In which royal palace would you find the Hall of Mirrors?"
        }, 
        {
        "answer": "Agra", 
        "category": 3, 
        "difficulty": 2, 
        "id": 15, 
        "question": "The Taj Mahal is located in which Indian city?"
        }
    ], 
    "success": true, 
    "total_questions": 3
    }

```


#### DELETE '/questions/[question_id]'

**General**
- Deletes any chosen question by the question id.
- **Sample Request:**
curl -X DELETE -i http://127.0.0.1:5000/questions/22
- **Sample Response:**

```bash
    
    {
    "deleted": 22,
    "success": true
    }

```

#### POST '/actors'

**General**
- To add an actor to the database.

- **Sample Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Viola Davis\", \"gender\":\"Female\", \"age\":\"55\"}" http://127.0.0.1:5000/actors
```

- **Sample Response:**

```bash
    
    {
        "name": "Viola Davis",
        "age": 55
        "gender": "Female"
    },
    "success": true
    }

```



#### POST '/movies'

**General**
- To add an movies to the database.

- **Sample Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"The First Movie\", \"release_date\": \"2020-02-20\"}" http://127.0.0.1:5000/movies
```

- **Sample Response:**

```bash
    
{
  "movies":
    {
      "id": 1, 
      "release_date": "Thu, 20 Feb 2020 00:00:00 GMT", 
      "title": "The First Movie"
    }, 
  "success": true
}

```

#### POST '/questions'

**General**
- Adds new question to the list of Trivia questions.
- **Sample Request:**
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"question\":\"Hematology is a branch of medicine involving the study of what?\", \"answer\":\"Blood\", \"difficulty\":\"4\", \"category\":\"1\"}" http://127.0.0.1:5000/questions
```
(For Windows users, please hence that doublequotes must be masked with backslash inside)
- **Sample Response:**

```bash
    
    {
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 25,
    "question": "Hematology is a branch of medicine involving the study of what?"
    },
    "success": true
    }

```

#### POST '/questions/search'

**General**
- Gets questions based on a search term (case sensetive).
- Returns matching questions, success value, and total number of matching questions.
- **Sample Request:**
```bash
curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d "{\"searchTerm\": \"Giaconda\"}"
```
(For Windows users, please hence that doublequotes must be masked with backslash inside)
- **Sample Response:**

```bash
    
    {
    "current_category": null,
    "questions": [
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        }
    ],
    "success": true,
    "total_questions": 1
    }

```

#### POST '/quizzes'

**General**
- Initiates a new game with unrepeated questions based on a chosen category.
- **Sample Request:**
```bash
curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d "{\"quiz_category\": {\"type\": \"Art\", \"id\": \"2\"}}"
```
(For Windows users, please hence that doublequotes must be masked with backslash inside)
- **Sample Response:**

```bash
    
    {
        "question": {
        "answer": "Escher",
        "category": 2,
        "difficulty": 1,
        "id": 16,
        "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        },
        "success": true
    }

```