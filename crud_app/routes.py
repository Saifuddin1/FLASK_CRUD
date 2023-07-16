from flask import Blueprint


crud_bp = Blueprint("crud_bp", __name__)


@crud_bp.route("/")
def user_creation():
    return "This is User Creation page"
