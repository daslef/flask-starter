from itsdangerous import URLSafeSerializer

from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
    flash,
    url_for,
    redirect,
)
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user,
)

from . import Users, ACTIVE
from ..plugins import db, login_manager

auth_blueprint = Blueprint("frontend", __name__)


@auth_blueprint.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("albums.all_albums"))

    return redirect(url_for("auth.login"))


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("albums.all_albums"))

    if request.method == "GET":
        return render_template("auth/login.html", _active_login=True)

    # TODO


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out", "success")
    return redirect(url_for("auth.login"))


@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("albums.all_albums"))

    if request.method == "GET":
        return render_template("auth/signup.html", _active_signup=True)

    # TODO
