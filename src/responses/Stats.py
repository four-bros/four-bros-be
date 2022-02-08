from marshmallow import fields, Schema

from responses.Players import PlayerSchema


class PassingStatsSchema(Schema):
    class Meta:
        fields = (
            'player_id',
            'first_name',
            'last_name',
            'pass_yards',
            'longest_pass',
            'year',
            'pass_tds',
            'games_played',
            'completions',
            'ints',
            'pass_att'
        )
