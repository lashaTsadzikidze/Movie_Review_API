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

### 6. Run the development server:
```
python manage.py runserver
```

### API Endpoints
| Endpoints                 | Method   | Description                                                    |
|:------------------------- |:-------- |:-------------------------------------------------------------- |
| /api/movies/              | GET      | Retrieve all movies                                            |
| /api/movies/[id]/         | GET      | Retrieve a specific movie by ID                                |
| /api/movies/              | POST     | Add a new movie (Only the admin has the permission to do this) |
| /api/movies/[id]/reviews/ | POST     | Add a new Review for specific Moview by ID                     |
