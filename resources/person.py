from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.person_model import PersonModel
from schemas import PlainPersonSchema, PersonSchema, PersonUpdateSchema

blt = Blueprint('person_res', __name__, description='Thisdad sad awd awdadw')


@blt.route('/person/<string:person_id>')
class Person(MethodView):

    @blt.response(200, PersonSchema)
    def get(self, person_id):
        person = PersonModel.query.get_or_404(person_id)  # -> use of get or 404 maybe later
        return person
        # try:
        #     person = PersonModel.query.filter_by(id=name_id).first()
        #     return person
        # except SQLAlchemyError as se:
        #     raise se

    @blt.arguments(PersonUpdateSchema)
    @blt.response(200, PersonUpdateSchema)
    def put(self, payload, person_id):

        person = PersonModel.query.filter_by(id=person_id).first()
        if person:
            person.klas = payload['klas']
            person.name = payload['name']
        else:
            person = PersonModel(id=person_id, **payload)

        db.session.add(person)
        db.session.commit()
        return {"Message": "user updated!!!"}

    def delete(self, person_id):
        person = PersonModel.query.filter_by(id=person_id).first()
        # person = PersonModel.query.get_or_404(name=name)
        db.session.delete(person)
        db.session.commit()
        return {"Message": f"ID {person_id} succesfully deleted!"}


@blt.route('/persons')
class ManyPersons(MethodView):

    @blt.response(200, PersonSchema(many=True))
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
            return {"Message": f"person successfully created!!!"}

        except IntegrityError:
            abort(400, message="a person with that name already exists!")

        except SQLAlchemyError:
            abort(500, message='Some error occurred while creating an item')


@blt.route('/persons/<string:name>/items')
class PersonItems(ManyPersons):
    @blt.response(200, PersonSchema)
    def get(self, name):

        person = PersonModel.query.filter_by(name=name).first()
        # one = PersonModel.query.get_or_404(name=name)
        # items = []
        # for item in person:
        #     items.append(item.items)
        return person.items
