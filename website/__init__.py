from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "data_base.db"

# defines a function that sets up the flask app
def create_app():
    app = Flask(__name__) # an instance of the flask app called, using (__name__) to help flask know where to look for resources like tamplates and static files.
    app.config['SECRET_KEY'] = 's3cr3t_k3y' # sets up secret key for flask, which is important to secure cookies and important data in our sql server.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # sets the URI for the database, telling SQLAlchemy where the sqlite database is located
    db.init_app(app) # this allows flask to interact with the database.

    from .views import views
    from .auth import auth
    
    from .models import User, Note
    create_database(app) # calls the create_app function to make sure database and its tables are created if they don't already exist.

    login_manager = LoginManager() # an instance of loginmanager which is a flask extention used to manage user sessions and authentication.
    login_manager.login_view = 'auth.login' # sets the default login page to auth.login.
    login_manager.init_app(app) # initializes the LoginManager with the flask app, enabling user session management.

    @login_manager.user_loader # This decorator tells Flask how to load a user from their ID when accessing a protected route.
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

def create_database(app): # This function ensures that the database is created if it doesn't already exist.
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database has Created!')