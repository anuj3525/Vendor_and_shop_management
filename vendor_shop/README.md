<!-- Vendor & Shop Managemnet System

This project provides a REST API for vendor registration, login, and shop management, including adding, updating, retrieving, and finding nearby shops.

Prerequisites

Ensure you have the following installed:

Python (>=3.8)
Django (>=4.0)
Django REST Framework
Django Simple JWT
Geopy -->


<!-- Installation
activate a virtual environment: -->
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows


<!-- 1. Install dependencies: -->

pip install -r requirements.txt

<!-- 2. Apply migrations: -->
python manage.py makemigrations
python manage.py migrate

<!-- 3. Create a superuser (optional): -->
python manage.py createsuperuser



<!-- 5. Run the Server -->
python manage.py runserver


NOTE:- Run all cmd in prompt
Note :- All endpoints are tested on postman and worked perfectly.
