from marshmallow import Schema, fields


class ItemSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
