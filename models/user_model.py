# from db import db
# from datetime import datetime
#
#
# class UserModel(db.Model):
#     # __tablename__ = "user"
#
#     user_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(20), unique=False, nullable=False)
#     email = db.Column(db.String(50), unique=False, nullable=False)
#     date_joined = db.Column(db.Date, default=datetime.utcnow)
#
#     # pets = db.relationship('ServiceModel', backref='owner')
#     # ser_services = db.relationship('ServiceModel', backref='user_owner')
#     # user_services = db.Column(db.String(50), foreign_key='ServiceModel.')
#
#     #TODO Try later back_populates= need to be from both sides relation assigned
#     # db.relationship('ServiceModel', backref='usermodel')
#
#     def __repr__(self):
#         return f"Username {UserModel.first_name} email: {UserModel.email}"
