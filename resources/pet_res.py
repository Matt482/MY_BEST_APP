from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db

from models.pet_modelo import Pet
from models.owner_model import Owner

from flask import request

blt = Blueprint('pet', __name__, description="This suits for pets from all different owners")


@blt.route('/pets')
def get_pets_names():
    all_pets = Pet.query.all()
    res = []
    for pet in all_pets:
        res.append(pet.name)

    return {'Pets': list(res)}


@blt.route('/pet/<string:name>')
def get_one_pet(name):
    try:
        one_pet = Pet.query.filter_by(name=name).first()
        return {'Pets name': one_pet.name}, 200

    except SQLAlchemyError as se:
        raise se


@blt.route('/create_pet', methods=['POST'])
def create_pet():
    try:
        req = request.get_json()
        pet = Pet(name=req['name'], age=req['age'], owner_id=req['owner'])
        # his_owner = Owner.query.filter_by(id=pet.owner_id).first()
        db.session.add(pet)
        db.session.commit()

        return {"Message": f"Pet {pet.name} succesfully created!"}
    except SQLAlchemyError as se:
        raise se


@blt.route('/pet_del/<string:name>', methods=['DELETE'])
def delete_pet(name):
    try:
        own = Pet.query.filter_by(name=name).first()
        db.session.delete(own)
        db.session.commit()
        return {"Message": f"pet {own.name} succesfully deleted!"}, 201

    except SQLAlchemyError as se:
        raise se


