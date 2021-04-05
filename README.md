1. Install the virtual environment and go into it:

   pip install pipenv

   pipenv shell

2. Install all the required dependencies:

   pip install djangorestframework

   pip install django-extensions

   pip install psycopg2

3. Setup the database by changing the database information in exercise1/settings.py and create a database called batchRecords

4. Change the file path of the csv file in scripts/load.py. Make sure to change every '\' with '/' if using windows

5. Run the command:'python manage.py migrate'

6. Run the command: 'python manage.py runscript load' to convert the csv data into the database

7. Run the command: 'python manage.py runserver' to start the server

8. Test the api endpoint with postman or the link. Some examples:

   http://127.0.0.1:8000/batch_jobs/

   http://127.0.0.1:8000/batch_jobs/?min_nodes=19000&max_nodes=19583&submitted_after=2018-03-04T11:09:37Z

   http://127.0.0.1:8000/batch_jobs/?min_nodes=15000&max_nodes=18000&submitted_after=2018-03-04T11:45:37Z&submitted_before=2018-03-04T22:55:13Z
