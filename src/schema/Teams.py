from marshmallow import Schema, fields

from src.schema.Players import PlayerDetailsSchema


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


class TeamInfoSchema(Schema):
    id = fields.Int()
    team_name = fields.Str()
    nickname = fields.Str()
    is_user = fields.Bool()


class TeamRosterSchema(PlayerDetailsSchema):
    id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    height = fields.Str()
    weight = fields.Int()
    jersey_number = fields.Int()
    player_year = fields.Str()
    redshirt = fields.Boolean()
    position = fields.Str()
    hometown_desc = fields.Int()
    overall = fields.Int()


class TeamGameStatsSchema(Schema):
    year = fields.Int()
    games_played = fields.Int()
    total_points = fields.Int()
    pass_yds = fields.Int()
    pass_tds = fields.Int()
    ints = fields.Int()
    sacked = fields.Int()
    rush_yds = fields.Int()
    rush_tds = fields.Int()
    fumbles = fields.Int()
    rec_yds = fields.Int()
    rec_tds = fields.Int()
    drops = fields.Int()
    off_yards = fields.Int()
    off_ypg = fields.Float()
    total_yards = fields.Int()
    off_turnovers = fields.Int()
    sacks = fields.Int()
    tfl = fields.Int()
    ints_made = fields.Int()
    ff = fields.Int()
    fr = fields.Int()
    def_turnovers = fields.Int()
    to_margin = fields.Int()
    pass_def = fields.Int()
    safeties = fields.Int()
    blocked_kicks = fields.Int()
    def_tds = fields.Int()
    kr_yds = fields.Int()
    kr_tds = fields.Int()
    pr_yds = fields.Int()
    pr_tds = fields.Int()


class TeamSeasonStatsSchema(Schema):
    year = fields.Int()
    games_played = fields.Int()
    total_points = fields.Int()
    ppg = fields.Float()
    pass_yds = fields.Int()
    pass_ypg = fields.Float()
    pass_tds = fields.Int()
    ints = fields.Int()
    sacked = fields.Int()
    rush_yds = fields.Int()
    rush_ypg = fields.Float()
    rush_tds = fields.Int()
    fumbles = fields.Int()
    rec_yds = fields.Int()
    rec_ypg = fields.Float()
    rec_tds = fields.Int()
    drops = fields.Int()
    off_yards = fields.Int()
    off_ypg = fields.Float()
    total_yards = fields.Int()
    total_ypg = fields.Float()
    off_turnovers = fields.Int()
    sacks = fields.Int()
    tfl = fields.Int()
    ints_made = fields.Int()
    ff = fields.Int()
    fr = fields.Int()
    def_turnovers = fields.Int()
    to_margin = fields.Int()
    pass_def = fields.Int()
    safeties = fields.Int()
    blocked_kicks = fields.Int()
    def_tds = fields.Int()
    kr_yds = fields.Int()
    kr_tds = fields.Int()
    pr_yds = fields.Int()
    pr_tds = fields.Int()


class TeamSummarySchema(Schema):
    team_details = fields.Nested(TeamDetailsSchema)
    team_roster = fields.List(fields.Nested(TeamRosterSchema))
    team_stats = fields.Nested(TeamSeasonStatsSchema)


class TeamGameRecordSchema(Schema):
    team_info = fields.Nested(TeamInfoSchema)
    team_stats = fields.Nested(TeamGameStatsSchema)


class TeamSeasonRecordSchema(Schema):
    team_info = fields.Nested(TeamInfoSchema)
    team_stats = fields.Nested(TeamSeasonStatsSchema)
