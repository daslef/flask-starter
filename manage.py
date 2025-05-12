import click
from sqlalchemy.orm.mapper import configure_mappers

from app.bootstrap import create_app
from app.plugins import db
from app.auth import Users, ADMIN, USER, ACTIVE
from app.albums import AlbumModel

application = create_app()


@click.group()
def main():
    """CLI"""


@main.command()
def runserver():
    application.run(debug=True)


@main.command()
def initdb():
    """Init/reset database."""

    with application.app_context():
        db.drop_all()
        configure_mappers()
        db.create_all()

        admin = Users(
            name="Admin Flask-Starter",
            email="admin@your-mail.com",
            password="adminpassword",
            role_code=ADMIN,
            status_code=ACTIVE,
        )

        db.session.add(admin)

        for i in range(1, 2):
            user = Users(
                name="Demo User",
                email="demo@your-mail.com",
                password="demopassword",
                role_code=USER,
                status_code=ACTIVE,
            )
            db.session.add(user)

        for i in range(1, 5):
            _album = AlbumModel(title=f"Album ## {i}", user_id=2)
            db.session.add(_album)

        db.session.commit()

        print("Database initialized with 2 users (admin, demo)")
        print("Database initialized with 4 random albums (Album ##)")


if __name__ == "__main__":
    main()
