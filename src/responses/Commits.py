from marshmallow import Schema, fields


class CommitsSchema(Schema):
    stars = fields.Int()
    name = fields.String()
    position = fields.String()
    rank = fields.Int()
    school = fields.String()
    week = fields.Int()
    year = fields.Int()
