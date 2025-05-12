from datetime import datetime

from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from ..plugins import db
from .constants import USER, USER_ROLE, ADMIN, INACTIVE, USER_STATUS


class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(db.Integer, primary_key=True)

    name = Column(db.String())

    email = Column(db.String(), unique=True)
    email_activation_key = Column(db.String())

    created_time = Column(db.DateTime, default=datetime.today())

    _password = Column("password", db.String(128), nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    # Hide password encryption by exposing password field only.
    password = db.synonym(
        "_password", descriptor=property(_get_password, _set_password)
    )

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    role_code = Column(db.SmallInteger, default=USER, nullable=False)

    @property
    def role(self):
        return USER_ROLE[self.role_code]

    def is_admin(self):
        return self.role_code == ADMIN

    def is_authenticated(self):
        return True

    # One-to-many relationship between users and user_statuses.
    status_code = Column(db.SmallInteger, default=INACTIVE)

    @property
    def status(self):
        return USER_STATUS[self.status_code]

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(Users.email.ilike(login)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first_or_404()

    def check_email(self, email):
        return Users.query.filter(Users.email == email).count() == 0

    def __unicode__(self):
        _str = "%s. %s" % (self.id, self.name)
        return str(_str)
