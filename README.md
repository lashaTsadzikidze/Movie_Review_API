# Movie Review API
Welcome to the Movie Review API, a RESTful API that allows users to explore, create, and manage movie reviews.

## Features
* User Authentication: Secure user registration, login, and token-based authentication.
* Movie Management: Add, update, delete, and retrieve movie details.
* Review System: Create, edit, delete, and view reviews for movies.
* Ratings: Rate movies.
* User-Friendly Endpoints: Clean and intuitive API endpoints for ease of use.

## Technologies Used
* Django Rest Framework (DRF)
* SQLite (default).
* Git & GitHub
* Python

## Installation
### 1. Clone the repository:
```
git clone https://github.com/lashaTsadzikidze/Movie_Review_API.git
cd Movie_Review_API
```

### 2. Create a virtual environment:
```
python -m venv env  
source env/bin/activate   # On Windows: env\Scripts\activate  
```

### 3. Install dependencies:
```
pip install -r requirements.txt
```

### 4. Apply migrations:
```
python manage.py migrate
```

### 5. Create Superuser
```
python manage.py createsuperuser
```
#### Enter User details
- Username: The username for the superuser.
- Email Address: (Optional).
- Password: Set a secure password (you’ll need to confirm it).
example:
```
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### 6. Create simple user
Open the Django shell
```
python manage.py shell
```
Import the `User` model
```
from django.contrib.auth.models import User
```
Create the user with `create_user`:
```
user = User.objects.create_user(
    username='simpleuser',  # Replace with desired username
    password='securepassword123',  # Replace with a secure password
    email='simpleuser@example.com'  # Optional email field
)
```
Exit the shell:
```
exit()
```
### 7. Generate Tokens for Existing Users
```
python manage.py drf_create_token <username>
```
This will output the token for the specified user.

### 8. Run the development server:
```
python manage.py runserver
```

## API Endpoints
| Endpoints                            | Method   | Description                                                                                      |
|:------------------------------------ |:-------- |:------------------------------------------------------------------------------------------------ |
| /api/movies/                         | GET      | List all movies                                                                                  |
| /api/movies/[id]/                    | GET      | Retrieve a specific movie by ID                                                                  |
| /api/movies/                         | POST     | Add a new movie (Only the admin has the permission to do this)                                   |
| /api/movies/[movie_id]/reviews/      | POST     | Add a new Review for specific Movie by ID (Only Authorized users have the permission to do this)|
| /api/movies/[movie_id]/reviews/[id]/ | DELETE   | Delete a review (Only the admin has the permission to do this)                                   |

## How to use
### Add New Movie
#### 1. Open Postman
#### 2. Create a New Request
- Click on New > Request > POST.
- Set the URL. Use your endpoint.
  ```
  http://127.0.0.1:8000/api/movies/
  ```
- Set the Headers In the "Headers" tab, add the following:\
  Key: `Content-Type`\
  Value: `application/json`

  (Authorization as superuser)\
  Key: `Authorization`\
  Value: `Token <superuser token>`
- Go to the "Body" tab, check "raw" and set the data to json format. For example:
  ```
  {
    "id": 1,
    "title": "Title 1",
    "genre": "Genre 1",
    "description": "Description 1",
    "release_date": "2024-11-21"
  }
  ```
- Click the send button.

### Get a list of movies
- Change "POST" to "GET"
- Click the Send button
- Or open the Following link in browser: `http://127.0.0.1:8000/api/movies/`

### Add a new Review for specific Movie by ID
- Change "GET" to "POST"
- Set the URL. `http://127.0.0.1:8000/api/movies/1/reviews/`
- In "Headers" tab value of "Authorization" Replace with the token of the user you want to write a review with.
- Go to the "Body" tab, check "raw" and set the data to json format. For example:
  ```
  {
    "rating": 10,
    "comment": "Random Comment."
  }
  ```
- Click the Send button.
