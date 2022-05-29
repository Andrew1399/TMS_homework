import flask
import os
from app.users.api.methods import main
from app.users.api.auth import auth
from app.models.base import db
from flask_login import LoginManager
from flask_migrate import Migrate

def create_app() -> flask.Flask:
    """
    Создает и конфигурирует приложение.
    """
    app = flask.Flask(__name__, template_folder='template')

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.base import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    db.create_all(app=app)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app



