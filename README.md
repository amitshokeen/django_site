# Meetups Web App

A Django-based web application for managing and attending meetups.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django (version specified in requirements.txt)

### Installation

1. Clone the repository:
   `cd meetups-webapp`  

2. Install required packages:
   `pip install -r requirements.txt`   

3. Perform database migrations:
   `python manage.py makemigrations`   
   `python manage.py migrate`   

4. Create a superuser (admin account):   
    `python manage.py createsuperuser`   
    Follow the prompts to set up your admin credentials.

## Running the Application

To start the development server:   
`python manage.py runserver`   

The application will be available at `http://127.0.0.1:8000`.

## Accessing the Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin`
2. Log in using your superuser credentials
3. Use the admin panel to create Meetups and add Locations

## User Guide

1. Access the main application at `http://127.0.0.1:8000`
2. Browse upcoming meetups
3. Register for meetups of interest





 
 
