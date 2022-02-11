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


class RushingStatsSchema(Schema):
    rush_att = fields.Int()
    rush_yards = fields.Int()
    ya_contact = fields.Int()
    broke_tkls = fields.Int()
    fumbles = fields.Int()
    twenty_plus_yd_runs = fields.Int()


class PlayerPassingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    passing_stats = fields.Nested(PassingStatsSchema)


class PlayerRushingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    rushing_stats = fields.Nested(RushingStatsSchema)
