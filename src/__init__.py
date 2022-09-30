from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)

#Cargar las configuraciones
    app.config.from_object('config.DevelopmentConfig')
    db = SQLAlchemy(app)

#Importar vistas 
    from src.views.auth import auth
    app.register_blueprint(auth)

    from src.views.blog import blog
    app.register_blueprint(blog)
    app.add_url_rule('/', endpoint='index')

    db.create_all()
