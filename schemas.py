from marshmallow import Schema, fields


# class PlainPetSchema(Schema):
#     pet_id = fields.Int(dump_only=True)
#     name = fields.Str(required=True)
#     age = fields.Int()
#
#
# class PlainOwnerSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str(required=True)
#     address = fields.Str()
#
#
# class PetSchema(PlainPetSchema):
#     owner_id = fields.Int(required=True, load_only=True)
#     owner = fields.Nested(PlainOwnerSchema(), dump_only=True)
#
#
# class OwnerSchema(PlainOwnerSchema):
#     pets = fields.List(fields.Nested(PlainOwnerSchema()), dump_only=True)


class PlainItemSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()


class PlainPersonSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    klas = fields.Str()


class ItemSchema(PlainItemSchema):
    owner_id = fields.Int(required=True, load_only=True)
    persona = fields.Nested(PlainPersonSchema(), dump_only=True)


class PersonSchema(PlainPersonSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    owner = fields.Str()


class PersonUpdateSchema(Schema):
    item_id = fields.Integer(dump_only=True)
    klas = fields.Str()
    name = fields.Str()
