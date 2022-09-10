from marshmallow import Schema, fields


class WeekYearSchema(Schema):
    week = fields.Int()
    year = fields.Int()
