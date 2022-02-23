from marshmallow import Schema, fields


# Create Player Details Schema to avoid circular import
class PlayerDetailsSchema(Schema):
    id = fields.Int()
    team_id = fields.Int()
    team_name = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    height = fields.Str()
    weight = fields.Int()
    jersey_number = fields.Int()
    player_year = fields.Str()
    redshirt = fields.Str()
    position = fields.Str()
    hometown_desc = fields.Int()

#############################
### Stat Category Schemas ###
#############################
class DefensiveStatsSchema(Schema):
    long_int_ret = fields.Int()
    sacks = fields.Float()
    year = fields.Str()
    forced_fumbles = fields.Int()
    solo_tkls = fields.Float()
    safeties = fields.Int()
    pass_def = fields.Int()
    blocked_kicks = fields.Int()
    tfl = fields.Int()
    ints_made = fields.Int()
    games_played = fields.Int()
    fumbles_rec = fields.Int()
    half_a_sack = fields.Float()
    asst_tkls = fields.Float()
    def_tds = fields.Int()
    fum_rec_yards = fields.Int()
    int_ret_yards = fields.Int()
    total_tkls = fields.Float()
    total_sacks = fields.Float()


class KickingStatsSchema(Schema):
    fg_made_17_29 = fields.Int()
    fg_att_17_29 = fields.Int()
    long_fg = fields.Int()
    ko_touchbacks = fields.Int()
    long_punt = fields.Int()
    xp_att = fields.Int()
    year = fields.Str()
    punts_blocked = fields.Int()
    fg_att = fields.Int()
    total_punt_yards = fields.Int()
    xp_blocked = fields.Int()
    fg_blocked = fields.Int()
    fg_att_40_49 = fields.Int()
    fg_made_40_49 = fields.Int()
    fg_att_30_39 = fields.Int()
    fg_made_30_39 = fields.Int()
    fg_att_50_plus = fields.Int()
    fg_made_50_plus = fields.Int()
    punt_touchbacks = fields.Int()
    games_played = fields.Int()
    kickoffs = fields.Int()
    xp_made = fields.Int()
    net_punting = fields.Int()
    fg_made = fields.Int()
    number_punts = fields.Int()
    inside_twenty = fields.Int()
    fg_pct = fields.Float()
    xp_pct = fields.Float()
    fg_50_plus_pct = fields.Float()
    punt_avg = fields.Float()


class PassingStatsSchema(Schema):
    pass_yards = fields.Int()
    longest_pass = fields.Int()
    year = fields.Str()
    pass_tds = fields.Int()
    games_played = fields.Int()
    completions = fields.Int()
    ints = fields.Int()
    pass_att = fields.Int()
    pass_yp_attempt = fields.Float()
    pass_yp_game = fields.Float()
    pass_rating = fields.Float()


class ReceivingStatsSchema(Schema):
    receptions = fields.Int()
    rec_yards = fields.Int()
    rec_tds = fields.Int()
    yac = fields.Int()
    drops = fields.Int()
    rec_yp_catch = fields.Float()
    rec_yp_game = fields.Float()
    games_played = fields.Int()
    year = fields.Str()


class ReturnStatsSchema(Schema):
    kick_returns = fields.Int()
    year = fields.Str()
    long_kr = fields.Int()
    punt_returns = fields.Int()
    long_pr = fields.Int()
    games_played = fields.Int()
    kr_tds = fields.Int()
    pr_tds = fields.Int()
    kr_yds = fields.Int()
    pr_yds = fields.Int()
    kr_avg = fields.Float()
    pr_avg = fields.Float()


class RushingStatsSchema(Schema):
    rush_att = fields.Int()
    rush_yards = fields.Int()
    rush_tds = fields.Int()
    ya_contact = fields.Int()
    broke_tkls = fields.Int()
    fumbles = fields.Int()
    twenty_plus_yd_runs = fields.Int()
    rush_yp_carry = fields.Float()
    rush_yp_game = fields.Float()
    games_played = fields.Int()
    year = fields.Int()


##############################################
### Player Details + Stat Category Schemas ###
##############################################
class PlayerDefensiveStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    defensive_stats = fields.Nested(DefensiveStatsSchema)


class PlayerKickingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    kicking_stats = fields.Nested(KickingStatsSchema)


class PlayerReceivingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    receiving_stats = fields.Nested(ReceivingStatsSchema)


class PlayerReturnStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    return_stats = fields.Nested(ReturnStatsSchema)    


class PlayerRushingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    rushing_stats = fields.Nested(RushingStatsSchema)


class PlayerPassingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    passing_stats = fields.Nested(PassingStatsSchema)
