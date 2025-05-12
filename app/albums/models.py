from datetime import datetime

from sqlalchemy import Column

from ..auth.models import Users
from ..plugins import db


class AlbumModel(db.Model):
    __tablename__ = "albums"

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(2048))
    user_id = Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("Users", backref="albums")
    created_at = Column(db.DateTime, default=datetime.today())

    def __unicode__(self):
        return f"ID: {self.id}, Album: {self.task}"


class SongModel(db.Model):
    __tablename__ = "songs"

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(2048))
    created_at = Column(db.DateTime, default=datetime.today())
    album_id = Column(db.Integer, db.ForeignKey("albums.id"))
    album = db.relationship("AlbumModel", backref="songs")

    def __unicode__(self):
        return f"ID: {self.id}, Song: {self.task}, Album: {self.album}"
