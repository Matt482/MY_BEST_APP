from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)  # -> load only rly important so noone can see pw


class PlainItemSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()


# class PlainTagSchema(Schema):
#     id = fields.Integer(dump_only=True)
#     name = fields.Str(required=True)


# class TagSchema(PlainTagSchema):
#     owner_id = fields.Int(load_only=True)
#     persona = fields.Nested(PlainPersonSchema(), dump_only=True)
#     # list of nested plain item schemas!
#     items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class ItemSchema(PlainItemSchema):
    owner_id = fields.Int(allow_none=True)
    person = fields.Nested(UserSchema(), dump_only=True)
    # tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    owner_id = fields.Int(allow_none=True)


# class TagAndItemSchema(Schema):
#     message = fields.Str()
#     item = fields.Nested(ItemSchema())
#     tag = fields.Nested(TagSchema())
