from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from ..plugins import db

from .models import AlbumModel, SongModel


albums_blueprint = Blueprint("albums", __name__, url_prefix="/albums")


@albums_blueprint.get("/")
def all_albums():
    _all_tasks = AlbumModel.query.filter_by(users_id=current_user.id).all()

    return render_template(
        "albums/all_albums.html", all_tasks=_all_tasks, _active_tasks=True
    )


@albums_blueprint.post("/")
@login_required
def create_album():
    form = request.form
    print(form)

    _task = AlbumModel()
    _task.users_id = current_user.id

    db.session.add(_task)
    db.session.commit()

    db.session.refresh(_task)
    flash("Your task is added successfully!", "success")
    return redirect(url_for("albums.all_albums"))


@albums_blueprint.get("/<id>")
def view_album(id):
    _album = AlbumModel.query.filter_by(id=id).first()

    if not _album:
        flash("Oops! Something went wrong!.", "danger")
        return redirect(url_for("albums.all_albums"))

    return render_template("tasks/view_task.html", album=_album)


@albums_blueprint.post("/<id>")
@login_required
def create_song(id):
    _album = AlbumModel.query.filter_by(id=id, users_id=current_user.id).first()

    if not _album:
        flash("Oops! Something went wrong!.", "danger")
        return redirect(url_for("albums.all_albums"))

    return render_template("tasks/view_task.html", album=_album)
