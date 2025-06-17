 # Pizza Restaurant API for managing pizza restaurants and their menus.

 RESTful API for a pizza restaurant using flask. Containing implemented models,validations and routes. Postman will be used to test the API.

 setup
 creating and activating virtual environment...
 pipenv install flask flask_sqlalchemy flask_migrate
 pipenv install
 pipenv shell

 initialize
 export FLASK_APP=server.app
 flask db init

 migrations
 flask db migrate -m "Initial migration"
 flask db upgrade
