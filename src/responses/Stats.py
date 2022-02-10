from marshmallow import Schema, fields

from src.responses.Players import PlayerDetailsSchema


class PassingStatsSchema(Schema):
    class Meta:
        fields = (
            'player_id',
            'first_name',
            'last_name',
            'player_year',
            'pass_yards',
            'longest_pass',
            'year',
            'pass_tds',
            'games_played',
            'completions',
            'ints',
            'pass_att'
        )


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
