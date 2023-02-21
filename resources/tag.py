from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.person_model import PersonModel
from models.tag import TagModel
from schemas import TagSchema

blt = Blueprint('Tags', __name__, description='This blueprint is for operation upon tags')


@blt.route('/person/<string:person_id>/tag')
class TagInStore(MethodView):

    @blt.response(200, TagSchema(many=True))
    def get(self, person_id):
        person = PersonModel.query.get_or_404(person_id)
        return person.tags.all()

    @blt.arguments(TagSchema)
    @blt.response(201, TagSchema)
    def post(self, tag_data, person_id):
        # make an if cond. A tag with that name already exists in that store
        if TagModel.query.filter(TagModel.owner_id == person_id) and TagModel.name == tag_data['name']:
            abort(400,
                  message='A tag with that name already exists with a person! One tag can have only one person!')

        tag = TagModel(name=tag_data['name'], owner_id=person_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return tag


@blt.route('/tag/<string:tag_id>')
class Tag(MethodView):

    @blt.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag


@blt.route('/all_tags')
class TagAll(MethodView):

    @blt.response(200, TagSchema(many=True))
    def get(self):
        all_tags = TagModel.query.all()
        return all_tags
