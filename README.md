# Storefront Project

A Django-based e-commerce project with REST API support using Django REST Framework, authentication with JWT via Djoser, and PostgreSQL as the database.

## Installation Guide

### Prerequisites
Ensure you have the following installed:
- Python 3.10 or higher
- PostgreSQL
- Virtual Environment (optional but recommended)

### Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/tamjidzihan/Store_Front_django.git
   cd Store_Front_django
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Update database credentials in `.env` as needed

5. **Setup the database:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Usage

- **Admin Panel:** Visit `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
- **API Endpoints:** The API is accessible under `http://127.0.0.1:8000/`
- **Authentication:** Uses JWT authentication via Djoser. 
  - Obtain token: `POST /auth/jwt/create/`
  - Refresh token: `POST /auth/jwt/refresh/`
  - Verify token: `POST /auth/jwt/verify/`

## Deployment
For production deployment:
- Set `DEBUG = False` in `settings.py`
- Use a production-ready web server (e.g., Gunicorn + Nginx)
- Configure a secure PostgreSQL database

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License
This project is open-source and available under the [MIT License](LICENSE).
