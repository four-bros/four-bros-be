from marshmallow import Schema, fields

from src.responses.Players import PlayerDetailsSchema


class TeamDetailsSchema(Schema):
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


class TeamRosterSchema(PlayerDetailsSchema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    height = fields.Str()
    weight = fields.Int()
    jersey_number = fields.Int()
    player_year = fields.Str()
    redshirt = fields.Str()
    position = fields.Str()
    hometown_desc = fields.Int()
    overall = fields.Int()


class TeamStatsSchema(Schema):
    total_points = fields.Int()
    ppg = fields.Float()
    pass_yds = fields.Int()
    pass_ypg = fields.Float()
    pass_tds = fields.Int()
    rush_yds = fields.Int()
    rush_ypg = fields.Float()
    rush_tds = fields.Int()
    rec_yds = fields.Int()
    rec_ypg = fields.Float()
    rec_tds = fields.Int()
    sacks = fields.Int()
    ints = fields.Int()
    ff = fields.Int()
    fr = fields.Int()
    pass_def = fields.Int()
    safeties = fields.Int()
    def_tds = fields.Int()
    kr_yds = fields.Int()
    kr_tds = fields.Int()
    pr_yds = fields.Int()
    pr_tds = fields.Int()


class TeamInfoSchema(Schema):
    team_details = fields.Nested(TeamDetailsSchema)
    team_roster = fields.Nested(TeamRosterSchema)
    team_stats = fields.Nested(TeamStatsSchema)
