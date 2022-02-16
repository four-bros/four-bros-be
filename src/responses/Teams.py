from marshmallow import Schema, fields


class TeamSchema(Schema):
    id = fields.Int()
    team_name = fields.Str()
    team_short_name = fields.Str()
    is_user = fields.Bool()
    avg_overall = fields.Float()
    avg_offense = fields.Float()
    avg_defense = fields.Float()
    avg_sp_teams = fields.Float()
    coachs_poll_1st_votes = fields.Int()
    nickname = fields.Str()
    wins = fields.Int()
    bcs_rank = fields.Int()
    coachs_poll_rank = fields.Int()
    media_poll_rank = fields.Int()
    losses = fields.Int()
    media_poll_points = fields.Int()
    coachs_poll_points = fields.Int()
