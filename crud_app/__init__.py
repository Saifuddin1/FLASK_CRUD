from flask import Flask
import secrets
from crud_app.routes import crud_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:saif123@saifuddin"
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.register_blueprint(crud_bp, url_prefix="/")
    return app
