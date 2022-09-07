from marshmallow import Schema, fields

from src.schema.Stats import(
    DefensiveStatsSchema,
    KickReturnStatsSchema,
    KickingAndPuntingStatsSchema,
    PassingStatsSchema,
    PuntReturnStatsSchema,
    PuntingStatsSchema,
    ReceivingStatsSchema,
    RushingStatsSchema,
    TotalStatsSchema
)


class PlayerDetailsSchema(Schema):
    id = fields.Str()
    team_id = fields.Int()
    team_name = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    height = fields.Str()
    weight = fields.Int()
    jersey_number = fields.Int()
    player_year = fields.Str()
    redshirt = fields.Boolean()
    position = fields.Str()
    hometown_desc = fields.Int()


class PlayerAbilitiesSchema(Schema):
    play_recognition = fields.Int()
    press = fields.Int()
    power_moves = fields.Int()
    kick_accuracy = fields.Int()
    throwing_power = fields.Int()
    throwing_accuracy = fields.Int()
    overall = fields.Int()
    agility = fields.Int()
    stamina = fields.Int()
    acceleration = fields.Int()
    pursuit = fields.Int()
    route_running = fields.Int()
    speed = fields.Int()
    trucking = fields.Int()
    ball_carrier_vision = fields.Int()
    catch_in_traffic = fields.Int()
    block_shedding = fields.Int()
    strength = fields.Int()
    catch = fields.Int()
    injury = fields.Int()
    tackling = fields.Int()
    pass_blocking = fields.Int()
    run_blocking = fields.Int()
    break_tackle = fields.Int()
    impact_blocking = fields.Int()
    jump = fields.Int()
    carry = fields.Int()
    stiff_arm = fields.Int()
    kick_power = fields.Int()
    awareness = fields.Int()
    release = fields.Int()
    spec_catch = fields.Int()
    elusiveness = fields.Int()
    spin_move = fields.Int()
    hit_power = fields.Int()
    kick_return = fields.Int()
    man_coverage = fields.Int()
    zone_coverage = fields.Int()
    finesse_moves = fields.Int()
    juke_move = fields.Int()


class PlayerStatsSchema(Schema):
    passing = fields.Nested(PassingStatsSchema)
    rushing = fields.Nested(RushingStatsSchema)
    receiving = fields.Nested(ReceivingStatsSchema)
    defensive = fields.Nested(DefensiveStatsSchema)
    kick_return = fields.Nested(KickReturnStatsSchema)
    kicking = fields.Nested(KickingAndPuntingStatsSchema)
    punting = fields.Nested(PuntingStatsSchema)
    punt_return = fields.Nested(PuntReturnStatsSchema)
    total = fields.Nested(TotalStatsSchema)


class PlayerSchema(Schema):
    details = fields.Nested(PlayerDetailsSchema)
    abilities = fields.Nested(PlayerAbilitiesSchema)
    career_stats = fields.Nested(PlayerStatsSchema)
    season_stats = fields.Nested(PlayerStatsSchema)
    game_stats = fields.Nested(PlayerStatsSchema)
