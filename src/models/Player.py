from src.models.Stats import(
    DefensiveStats,
    KickingStats,
    PassingStats,
    ReceivingStats,
    ReturnStats,
    RushingStats
)


class PlayerDetails:
    def __init__(
        self,
        id,
        team_id,
        team_name,
        first_name,
        last_name,
        height,
        weight,
        jersey_number,
        player_year,
        redshirt,
        position,
        hometown_desc
    ):

        self.id = id
        self.team_id = team_id
        self.team_name = team_name
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.jersey_number = jersey_number
        self.player_year = player_year
        self.redshirt = redshirt
        self.position = position
        self.hometown_desc = hometown_desc


class PlayerAbilities:
    def __init__(
        self,
        play_recognition,
        press,
        power_moves,
        kick_accuracy,
        throwing_power,
        throwing_accuracy,
        overall,
        agility,
        stamina,
        acceleration,
        pursuit, 
        route_running,
        speed,
        trucking,
        ball_carrier_vision,
        catch_in_traffic,
        block_shedding,
        strength,
        catch,
        injury,
        tackling,
        pass_blocking, 
        run_blocking,
        break_tackle,
        impact_blocking,
        jump,
        carry,
        stiff_arm,
        kick_power,
        awareness,
        release,
        spec_catch,
        elusiveness, 
        spin_move,
        hit_power, 
        kick_return,
        man_coverage,
        zone_coverage,
        finesse_moves,
        juke_move
    ):

        self.play_recognition = play_recognition
        self.press = press
        self.power_moves = power_moves
        self.kick_accuracy = kick_accuracy
        self.throwing_power = throwing_power
        self.throwing_accuracy = throwing_accuracy
        self.overall = overall
        self.agility = agility
        self.stamina = stamina
        self.acceleration = acceleration
        self.pursuit = pursuit
        self.route_running = route_running
        self.speed = speed
        self.trucking = trucking
        self.ball_carrier_vision = ball_carrier_vision
        self.catch_in_traffic = catch_in_traffic
        self.block_shedding = block_shedding
        self.strength = strength
        self.catch = catch
        self.injury = injury
        self.tackling = tackling
        self.pass_blocking = pass_blocking
        self.run_blocking = run_blocking
        self.break_tackle = break_tackle
        self.impact_blocking = impact_blocking
        self.jump = jump
        self.carry = carry
        self.stiff_arm = stiff_arm
        self.kick_power = kick_power
        self.awareness = awareness
        self.release = release
        self.spec_catch = spec_catch
        self.elusiveness = elusiveness
        self.spin_move = spin_move
        self.hit_power = hit_power
        self.kick_return = kick_return
        self.man_coverage = man_coverage
        self.zone_coverage = zone_coverage
        self.finesse_moves = finesse_moves
        self.juke_move = juke_move


class PlayerStats:
    def __init__(
        self,
        passing_stats: PassingStats,
        rushing_stats: RushingStats,
        receiving_stats: ReceivingStats,
        defensive_stats: DefensiveStats,
        return_stats: ReturnStats,
        kicking_stats: KickingStats
    ):
        self.passing_stats = passing_stats
        self.rushing_stats = rushing_stats
        self.receiving_stats = receiving_stats
        self.defensive_stats = defensive_stats
        self.return_stats = return_stats
        self.kicking_stats = kicking_stats



class PlayerAbilitiesDetailsStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        player_abilities: PlayerAbilities,
        player_stats: PlayerStats
    ):

        self.player_details = player_details
        self.player_abilities = player_abilities
        self.player_stats = player_stats
