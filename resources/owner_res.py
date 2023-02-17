from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.owner_model import Owner

from flask import request


blt = Blueprint('owners', __name__, description="This suits for owners")


@blt.route('/owners')
def get_owner_names():
    all_owners = Owner.query.all()
    res = []
    for own in all_owners:
        res.append(own.name)

    return {'Owners': list(res)}


@blt.route('/owner/<string:name>')
def get_one_owner(name):
    try:
        one_owner = Owner.query.filter_by(name=name).first()
        return {'Owners name': one_owner.name, "owner id": one_owner.id}
    except SQLAlchemyError as se:
        raise se


@blt.route('/owner/<string:name>/all_pets')
def get_owner_pets(name):
    try:
        own = Owner.query.filter_by(name=name).first()
        owner_pets = [pet.name for pet in own.pets]
        return {"Owner_pets": owner_pets}

    except SQLAlchemyError as se:
        raise se


@blt.route('/create_owner', methods=['POST'])
def create_owner():
    req = request.get_json()
    try:
        own = Owner(name=req['name'], address=req['address'])
        db.session.add(own)
        db.session.commit()
        return {"Message": f"owner {own.name} created succesfully"}, 201

    except SQLAlchemyError as se:
        raise se


@blt.route('/owner_del/<string:name>', methods=['DELETE'])
def delete_owner(name):
    try:
        own = Owner.query.filter_by(name=name).first()
        db.session.delete(own)
        db.session.commit()
        return {"Message": f"user {own.name} succesfully deleted!"}, 201

    except SQLAlchemyError as se:
        raise se
