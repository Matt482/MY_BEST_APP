from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()


class PlainPersonSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    klas = fields.Str()


class PlainTagSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)


class TagSchema(PlainTagSchema):
    owner_id = fields.Int(load_only=True)
    persona = fields.Nested(PlainPersonSchema(), dump_only=True)
    # list of nested plain item schemas!
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class ItemSchema(PlainItemSchema):
    owner_id = fields.Int(required=True, load_only=True)
    persona = fields.Nested(PlainPersonSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class PersonSchema(PlainPersonSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    owner = fields.Str()


class PersonUpdateSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    klas = fields.Str()
    name = fields.Str()


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema())
    tag = fields.Nested(TagSchema())


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)  # -> load only rly important so noone can see pw
