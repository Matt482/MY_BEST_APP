from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.person_model import PersonModel
from models.tag import TagModel
from models.item_model import ItemModel
from schemas import TagSchema, TagAndItemSchema

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

    @blt.response(
        202,
        description='Deletes a tag if no item is tagged with it',
        example={'message': 'Tag deleted!'}
    )
    @blt.alt_response(404, description='Tag not found')
    @blt.alt_response(400, description='tag is assigned to one or more items. In this case the tag is not deleted!')
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"Message": "Tag succesfully deleted"}
        abort(
            400,
            message='Could not delete tag. Make sure not a single item is associated within tag!'
        )


@blt.route('/item/<string:item_id>/tag/<string:tag_id>')
class LinkTagsToItem(MethodView):

    @blt.response(200, TagSchema)
    def post(self, item_id, tag_id):

        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message='An error occurred while inserting a tag')

        return tag

    @blt.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message='An error occurred while inserting a tag')

        return {"Message": "Item removed from tag", "item": item, "tag": tag}


@blt.route('/all_tags')
class TagAll(MethodView):

    @blt.response(200, TagSchema(many=True))
    def get(self):
        all_tags = TagModel.query.all()
        return all_tags
