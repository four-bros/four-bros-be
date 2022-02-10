from marshmallow import Schema


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
