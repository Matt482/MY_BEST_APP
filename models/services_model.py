from db import db
from datetime import datetime


class ServiceModel(db.Model):
    # __tablename__ = "service"

    main_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(20), unique=False, nullable=False)
    service_description = db.Column(db.String(100), unique=False, nullable=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow)

    # user_owner = db.Column(db.Integer, db.ForeignKey('usermodel.user_id'))
    # user_owner_id = db.Column(db.Integer, db.ForeignKey('user_owner.user_id'))
    # owner_id = db.Column(db.Integer, db.ForeignKey('owner.user_id'))

    def __repr__(self):
        return f"Service name: {ServiceModel.service_name}"
