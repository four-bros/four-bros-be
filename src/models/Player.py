from typing import List
from src.models.Stats import(
    DefensiveStats,
    KickReturnStats,
    KickingStats,
    PassingStats,
    PuntingStats,
    PuntReturnStats,
    ReceivingStats,
    RushingStats,
    TotalStats
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

    def __repr__(self):
        return f'ID: {self.id}, Name: {self.first_name} {self.last_name}'

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
        passing: PassingStats,
        rushing: RushingStats,
        receiving: ReceivingStats,
        defensive: DefensiveStats,
        kicking: KickingStats,
        kick_return: KickReturnStats,
        punting: PuntingStats,
        punt_return: PuntReturnStats,
        total: TotalStats
    ):
        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving
        self.defensive = defensive
        self.kicking = kicking
        self.kick_return = kick_return
        self.punting = punting
        self.punt_return = punt_return
        self.total = total

    def __repr__(self):
        return f'passing stats: {self.passing}, rushing stats: {self.rushing}, rec stats {self.receiving}'


class PlayerStatsList:
    def __init__(
        self,
        passing: List[PassingStats],
        rushing: List[RushingStats],
        receiving: List[ReceivingStats],
        defensive: List[DefensiveStats],
        kicking: List[KickingStats],
        kick_return: List[KickReturnStats],
        punting: List[PuntingStats],
        punt_return: List[PuntReturnStats],
        total: List[TotalStats]
    ):
        self.passing = passing
        self.rushing = rushing
        self.receiving = receiving
        self.defensive = defensive
        self.kicking = kicking
        self.kick_return = kick_return
        self.punting = punting
        self.punt_return = punt_return
        self.total = total

    def __repr__(self):
        return f'passing stats: {self.passing}, rushing stats: {self.rushing}, rec stats {self.receiving}'


class PlayerAbilitiesDetailsStats:
    def __init__(
        self,
        details: PlayerDetails,
        abilities: PlayerAbilities,
        career_stats: PlayerStats,
        season_stats: PlayerStats,
        game_stats: PlayerStatsList
    ):
        self.details = details
        self.abilities = abilities
        self.career_stats = career_stats
        self.season_stats = season_stats
        self.game_stats = game_stats

    def __repr__(self) -> str:
        return f'game stats: {self.game_stats}'


class PlayerOfTheWeek:
    def __init__(
        self,
        details: PlayerDetails,
        game_stats: PlayerStats
    ):
        self.details = details
        self.game_stats = game_stats

    def __repr__(self) -> str:
        return f'game stats: {self.game_stats}'


class PlayerHofInfo:
    def __init__(
        self,
        details: PlayerDetails,
        abilities: PlayerAbilities,
        career_stats: PlayerStats,
        season_stats: PlayerStatsList
    ):
        self.details = details
        self.abilities = abilities
        self.career_stats = career_stats
        self.season_stats = season_stats
