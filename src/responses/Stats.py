from marshmallow import Schema, fields

from src.responses.Players import PlayerDetailsSchema


class PassingStatsSchema(Schema):
    pass_yards = fields.Int()
    longest_pass = fields.Int()
    year = fields.Int()
    pass_tds = fields.Int()
    games_played = fields.Int()
    completions = fields.Int()
    ints = fields.Int()
    pass_att = fields.Int()


class PlayerPassingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    passing_stats = fields.Nested(PassingStatsSchema)
