from flask import Blueprint, render_template, request, redirect, url_for
from crud_app.models import User
from crud_app.database import db

crud_bp = Blueprint("crud_bp", __name__)


@crud_bp.route("/", methods=['GET', 'POST'])
def index():
    all_users = User.query.paginate(
        page=request.args.get('page', 1, type=int), per_page=2, error_out=False)
    if request.method == 'POST':
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        email = request.form.get("email")
        password = request.form.get("password")
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud_bp.index'))
    title = "index"
    return render_template("index.html", all_users=all_users, title=title)


@crud_bp.route("/update/<int:user_id>", methods=["GET", "POST"])
def update(user_id):
    user_to_update = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user_to_update.first_name = request.form.get("fname")
        user_to_update.last_name = request.form.get("lname")
        user_to_update.email = request.form.get("email")
        user_to_update.password = request.form.get("password")
        db.session.commit()
        return redirect(url_for('crud_bp.index'))
    title = "update"
    return render_template('update.html', user=user_to_update, title=title)


@crud_bp.route("/delete/<int:user_id>", methods=["GET", "POST"])
def delete(user_id):
    user_to_delete = User.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for('crud_bp.index'))
