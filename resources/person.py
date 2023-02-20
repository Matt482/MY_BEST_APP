from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.person_model import PersonModel
from schemas import PlainPersonSchema, PersonSchema, ItemUpdateSchema

blt = Blueprint('person_res', __name__, description='Thisdad sad awd awdadw')


@blt.route('/person/<string:name>')
class Person(MethodView):

    @blt.response(200, PlainPersonSchema)
    def get(self, name):
        # person = PersonModel.query.get_or_404(name=name)
        person = PersonModel.query.filter_by(name=name).first()
        return person

    @blt.response(200, ItemUpdateSchema)
    def put(self, payload, name):

        raise NotImplementedError("put person not implemented yet!!!")

    @blt.response(201, PlainPersonSchema)
    def delete(self, name):
        person = PersonModel.query.filter_by(name=name).first()
        # person = PersonModel.query.get_or_404(name=name)
        db.session.delete(person)
        db.session.commit()
        return {"Message": f"person {name} succesfully deleted!"}


@blt.route('/persons')
class ManyPersons(MethodView):

    @blt.response(200, PlainPersonSchema(many=True))
    def get(self):

        all_persons = PersonModel.query.all()
        return all_persons

    @blt.arguments(PlainPersonSchema)
    @blt.response(201, PlainPersonSchema)
    def post(self, payload):
        try:
            person = PersonModel(**payload)
            db.session.add(person)
            db.session.commit()
            return {"Message": f"person succesfully created!!!"}

        except IntegrityError:
            abort(400, message="a store with that name already exists!")

        except SQLAlchemyError:
            abort(500, message='Some error occured while creating an item')


@blt.route('/persons/<string:name>/items')
class PersonItems(ManyPersons):
    @blt.response(200, PersonSchema)
    def get(self, name):

        one = PersonModel.query.filter_by(name=name).first()
        # one = PersonModel.query.get_or_404(name=name)
        return one
