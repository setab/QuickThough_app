from . import db


class Though(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DataTime, default=db.func.current_timestamp())
    user = db.relationship("User", backref="thoughts")

    def __repr__(self):
        return f"<Thought {self.id} by User {self.user_id}>"
