from marshmallow import Schema, fields

from src.responses.Players import PlayerDetailsSchema

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


class PassingStatsSchema(Schema):
    pass_yards = fields.Int()
    longest_pass = fields.Int()
    year = fields.Int()
    pass_tds = fields.Int()
    games_played = fields.Int()
    completions = fields.Int()
    ints = fields.Int()
    pass_att = fields.Int()


class ReceivingStatsSchema(Schema):
    receptions = fields.Int()
    rec_yards = fields.Int()
    rec_tds = fields.Int()
    yac = fields.Int()
    drops = fields.Int()


class RushingStatsSchema(Schema):
    rush_att = fields.Int()
    rush_yards = fields.Int()
    ya_contact = fields.Int()
    broke_tkls = fields.Int()
    fumbles = fields.Int()
    twenty_plus_yd_runs = fields.Int()
    year = fields.Int()

##############################################
### Player Details + Stat Category Schemas ###
##############################################
class PlayerDefensiveStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    defensive_stats = fields.Nested(DefensiveStatsSchema)


class PlayerReceivingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    receiving_stats = fields.Nested(ReceivingStatsSchema)


class PlayerPassingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    passing_stats = fields.Nested(PassingStatsSchema)


class PlayerRushingStatsSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    rushing_stats = fields.Nested(RushingStatsSchema)
