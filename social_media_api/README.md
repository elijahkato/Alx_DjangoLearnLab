# Social Media API

This is a Django-based Social Media API with user authentication.

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- Register: POST `/api/register/`
  - Payload: `{"username": "...", "email": "...", "password": "..."}`
- Login: POST `/api/login/`
  - Payload: `{"username": "...", "password": "..."}`

Both endpoints return a token upon successful operation.

## User Model

The custom user model includes fields for:
- Username
- Email
- Password
- Bio
- Profile picture
- Followers (Many-to-Many relationship)

To use the API, register a user, then use the returned token in the Authorization header for subsequent requests.