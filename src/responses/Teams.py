from marshmallow import Schema


class TeamSchema(Schema):
    class Meta:
        fields = (
            'id',
            'team_name',
            'team_short_name',
            'is_user',
            'coachs_poll_1st_votes',
            'nickname',
            'wins',
            'bcs_rank',
            'coachs_poll_rank',
            'media_poll_rank',
            'losses',
            'media_poll_points',
            'coachs_poll_points'
            )
