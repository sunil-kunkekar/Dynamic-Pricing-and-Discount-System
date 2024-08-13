

Dynamic Pricing and Discount System

1) Project Overview: 
This Django-based application implements a dynamic pricing and discount system. It supports various product types with specific discount strategies, including seasonal and bulk discounts. The system also integrates with Django REST Framework for API endpoints, allowing CRUD operations on products, orders, and discounts.

2) Features:
Product Management  : Handle basic products, seasonal products, and bulk products with dynamic pricing.
Discount Management : Apply percentage and fixed amount discounts.
Order Management    : Create and manage orders, calculate totals with applied discounts.
API Integration     : Expose endpoints for managing products, discounts, and orders using Django REST Framework.


3) Technologies Used :
Django                : Web framework for building the application.
Django REST Framework : For creating and managing API endpoints.
MySQL                 : Database backend.
Python                : Programming language.
Postman               : For testing API endpoints.
Env                   :  venv\scripts\activate

4) Prerequisites
Python 3.9.5
Django version 4.2.15
Django REST Framework 3.15.2
DB : SQlit3 
pip (Python package installer)- pip 24.2

git clone https://github.com/yourusername/dynamic_pricing_system.git
cd dynamic_pricing_system


pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 9966

python manage.py createsuperuser

pip freeze > requirements.txt

<!-- 
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver -->



<!--



