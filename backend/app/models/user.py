from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(500))
    profile_picture = db.Column(db.String(500))
    firebase_uid = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
