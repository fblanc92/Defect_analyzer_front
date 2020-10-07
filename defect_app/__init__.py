from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from defect_app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # extentions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from defect_app.users.routes import users
    from defect_app.posts.routes import posts
    from defect_app.main.routes import main
    from defect_app.errors.handlers import errors

    from defect_app.analyzerconfigs.routes import analyzer_config_blueprint

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(analyzer_config_blueprint)

    return app
