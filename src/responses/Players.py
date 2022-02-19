from marshmallow import Schema, fields

from src.responses.Stats import(
    DefensiveStatsSchema,
    KickingStatsSchema,
    PassingStatsSchema,
    ReceivingStatsSchema,
    ReturnStatsSchema,
    RushingStatsSchema
)


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
    passing_stats = fields.Nested(PassingStatsSchema)
    rushing_stats = fields.Nested(RushingStatsSchema)
    receiving_stats = fields.Nested(ReceivingStatsSchema)
    defensive_stats = fields.Nested(DefensiveStatsSchema)
    return_stats = fields.Nested(ReturnStatsSchema)
    kicking_stats = fields.Nested(KickingStatsSchema)

class PlayerSchema(Schema):
    player_details = fields.Nested(PlayerDetailsSchema)
    player_abilities = fields.Nested(PlayerAbilitiesSchema)
    player_stats = fields.Nested(PlayerStatsSchema)
