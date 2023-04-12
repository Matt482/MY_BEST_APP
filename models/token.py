from db import db


class TokenBlocklist(db.Model):
    __tablename__ = 'tokenblocklist'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(400), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
