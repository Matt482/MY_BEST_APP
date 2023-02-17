from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.person_model import PersonModel
from schemas import ItemSchema, PersonSchema

blt = Blueprint('person_res', __name__, description='Thisdad sad awd awdadw')


@blt.route('/person/<string:name>')
class Person(MethodView):

    @blt.response(200, PersonSchema)
    def get(self, name):
        person = PersonModel.query.filter_by(name=name).first()
        return person

    @blt.arguments(PersonSchema)
    @blt.response(201, PersonSchema)
    def post(self, payload, name):
        try:
            person = PersonModel(**payload)
            db.session.add(person)
            db.session.commit()
            return {"Message": f"person succesfully created!!!"}
        except IntegrityError as ie:
            print('Cant create duplicate persons with same name!')
            raise ie

    @blt.response(201, PersonSchema)
    def delete(self, name):
        person = PersonModel.query.filter_by(name=name).first()
        db.session.delete(person)
        db.session.commit()
        return {"Message": f"person {name} succesfully deleted!"}


@blt.route('/persons')
class ManyPersons(MethodView):

    @blt.response(200, PersonSchema(many=True))
    def get(self):

        all_persons = PersonModel.query.all()
        return all_persons
