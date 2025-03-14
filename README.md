# inf117-mse

#Archive of Informatics 117 Database group project done for school of material sciences.#

MSE Backend:

Setup:

in /INF117-MSE/
pipenv shell
pipenv update

cd mse_faculty_db
python manage.py runserver

Usage:
Go to localhost:8000/admin/
Login- usr:admin, pw:admin

You will now be on the admin page where you can view and modify the models. 


How to add models: 

go to staff_data/models.py and add your models as classes
register them in admin.py 

after changes are made: 
python manage.py makemigrations 
python manage.py migrate 

How to create API calls:

1. Create serializer for model in seralizers.py
2. Create views for model in views.py
3. Add URL to urls.py

How to create admin account initially:
python manage.py createsuperuser
y for bypass

How to delete venv since we installed w pipenv:

pipenv --rm
