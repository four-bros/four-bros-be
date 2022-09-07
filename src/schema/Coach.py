from marshmallow import Schema, fields


class CoachInfoSchema(Schema):
    id = fields.Str()
    user = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    team_id = fields.Int()
    team_name = fields.Str()


class CoachStatsSchema(Schema):
    id = fields.Str()
    user = fields.Str()
    year = fields.Int()
    wins = fields.Int()
    losses = fields.Int()
    national_title = fields.Bool()


class CoachSeasonRecordSchema(Schema):
    team_id = fields.Int()
    team_name = fields.Str()
    year = fields.Int()
    wins = fields.Int()
    losses = fields.Int()
    national_title = fields.Bool()
