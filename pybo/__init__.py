from flask import Flask ,jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    from .views import main_view,board_view,user_view
    app.register_blueprint(main_view.bp)
    app.register_blueprint(board_view.bp)
    app.register_blueprint(user_view.bp)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models




    return app
