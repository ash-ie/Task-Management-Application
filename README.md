# Task-Management-Application installation

Step-1:activate environment

python -m venv venv
source venv/bin/activate 

Step-2:Install Dependencies

pip install -r requirements.txt

Step-3:Apply Migrations

python manage.py makemigrations
python manage.py migrate

Step-4:Create Superuser for superadmin creation

python manage.py createsuperuser

Step-5:Run the Development Server

python manage.py runserver

Step-6:Access the App

web:http://127.0.0.1:8000
api:http://127.0.0.1:8000/api/v1/user_app/user_signin/




