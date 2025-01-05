# Meetups Web App using Django

To make the db migrations:
1. On the terminal, navigate to the path containing the "manage.py" file.
2. `$ python manage.py makemigrations`
3. `$python manage.py migrate`  

To create an administrator/super user:
1. On the terminal, navigate to the path containing the "manage.py" file.
2. `$ python manage.py createsuperuser`  
3. Enter all relevant info related to the admin account.

To run the server:  
1. On the terminal, navigate to the path containing the "manage.py" file.
2. `$ python manage.py runserver`

To access the web app's admin:
1. On a browser, navigate to `127.0.0.1:8000/admin`  
2. Use the admin panel to create Meetups and add Locations

For the end user: 
1. On a browser, navigate to `127.0.0.1:8000`
2. Here you will see the upcoming meetups.
3. You may register for the meetups.

