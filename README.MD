# SOCIAL MEDIA APP
It is a REST API-based social network in Django where Users can sign up and create text posts, as well as view, like, and unlike other Users posts.

## Setup
Clone the repository and then move to the 'social-media-app' branch using the following command

	git checkout social-media-app

### Local Environment Configurations
Configure the Python virtual environment and then install all the dependencies available in the requirements.txt file using the following command

	pip install –r requirements.txt

After that create a database in Postgresql with the name “social-media”. 

In the terminal or command prompt, navigate to the directory where your Django project is located.

Create a .env file and set the environment variables according to your need. For example,

	IP_GEO_LOCATION_API_KEY=""
	SQL_HOST=""
	SQL_PORT=""
	SQL_USER=""
	SQL_PASSWORD=""
	SQL_DATABASE=""

Django uses database migrations to manage database schema changes. Run the following command to apply any pending migrations:

	python manage.py migrate

Use the following command to start the Django development server

	python manage.py runserver

The Django app should now be running. You can access it by opening a web browser and visiting

	http://localhost:8000/

### Docker Configurations
After that create a database in Postgresql with the name “social-media”. 

In the terminal or command prompt, navigate to the directory where your Django project is located.

Create a .env file and set the environment variables according to your need. For example,

	IP_GEO_LOCATION_API_KEY=""
	SQL_HOST=""
	SQL_PORT=""
	SQL_USER=""
	SQL_PASSWORD=""
	SQL_DATABASE=""

To migrate the new PostgreSQL database running in Docker execute the following command:

	docker-compose exec web python manage.py migrate

If you wanted to run createsuperuser you'd also prefix it with docker-compose exec web. So:

	docker-compose exec web python manage.py createsuperuser

Now build and run the container using

	docker-compose up -d –build

Django app should now be running. You can access it by opening a web browser and visiting 

http://0.0.0.0:8000/


## API Endpoints:
Register
	http://localhost:8000/api/posts/register/

Login 
	http://localhost:8000/api/posts/login/

Get User Details
	http://localhost:8000/api/posts/get-user-details/

Like-Unlike Posts
        http://localhost:8000/api/posts/like-unlike/

List of Posts
	http://localhost:8000/api/posts/posts/

Create Posts
	http://localhost:8000/api/posts/posts/

Read Posts
	http://localhost:8000/api/posts/posts/{id}/
	
Update Posts
	http://localhost:8000/api/posts/posts/{id}/

Delete Posts
	http://localhost:8000/api/posts/posts/{id}/


## Swagger Docs URL
After the app is started, go to the Swagger docs URL

For docker:	

	http://0.0.0.0:8000/swagger/

For localhost:	
 
 	http://localhost:8000/swagger/

This URL contains all the API requests going toward the backend along with the example of the required JSON format with every API.

## Run Test Cases
 First we need to run following command to export settings variables:

 	export DJANGO_SETTINGS_MODULE=SocialMediaApp.settings  

 Then run the following command to run the test cases:

 	pytest

