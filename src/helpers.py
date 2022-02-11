from src.constants import session
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.data_models.TeamInfo import TeamInfo
from src.models.Player import(
    Player, 
    PlayerAbilities, 
    PlayerDetails
)
from src.models.Stats import(
    PassingStats,
    PlayerPassingStats,
    PlayerRushingStats,
    RushingStats
)


def _convert_stats_year(year: int) -> int:
    return year + 2013

################################################
### Get player details and player abilities ####
################################################
def _get_player_details_and_abilities(player: PlayerInfo) -> Player:

    player_details: PlayerDetails = _get_player_details(player=player)
    player_abilities: PlayerAbilities = _get_player_abilities(player=player)

    converted_player: Player = Player(
        player_details=player_details,
        player_abilities=player_abilities
    )

    return converted_player


def _get_player_abilities(player: PlayerInfo) -> PlayerAbilities:

    player_abilities: PlayerAbilities = PlayerAbilities(
        play_recognition=player.play_recognition,
        press=player.press,
        power_moves=player.power_moves,
        kick_accuracy=player.kick_accuracy,
        throwing_power=player.throwing_power,
        throwing_accuracy=player.throwing_accuracy,
        overall=player.overall,
        agility=player.agility,
        stamina=player.stamina,
        acceleration=player.acceleration,
        pursuit=player.pursuit,
        route_running=player.route_running,
        speed=player.speed,
        trucking=player.trucking,
        ball_carrier_vision=player.ball_carrier_vision,
        catch_in_traffic=player.catch_in_traffic,
        block_shedding=player.block_shedding,
        strength=player.strength,
        catch=player.catch,
        injury=player.injury,
        tackling=player.tackling,
        pass_blocking=player.pass_blocking,
        run_blocking=player.run_blocking,
        break_tackle=player.break_tackle,
        impact_blocking=player.impact_blocking,
        jump=player.jump,
        carry=player.carry,
        stiff_arm=player.stiff_arm,
        kick_power=player.kick_power,
        awareness=player.awareness,
        release=player.release,
        spec_catch=player.spec_catch,
        elusiveness=player.elusiveness,
        spin_move=player.spin_move,
        hit_power=player.hit_power,
        kick_return=player.kick_return,
        man_coverage=player.man_coverage,
        zone_coverage=player.zone_coverage,
        finesse_moves=player.finesse_moves,
        juke_move=player.juke_move,
    )

    return player_abilities


def _get_player_details(player: PlayerInfo) -> PlayerDetails:

    team_info: TeamInfo = session.query(TeamInfo).filter(TeamInfo.id == player.team_id).one()

    player_details: PlayerDetails = PlayerDetails(
        id=player.id,
        team_id=player.team_id,
        team_name=team_info.team_name,
        first_name=player.first_name,
        last_name=player.last_name,
        height=player.height,
        weight=player.weight,
        jersey_number=player.jersey_number,
        player_year=player.player_year,
        redshirt=player.redshirt,
        position=player.position,
        hometown_desc=player.hometown_desc
    )

    return player_details


################################################
########## Get player passing stats ############
################################################
def _get_player_passing_stats(player) -> PlayerPassingStats:

    player_info: PlayerInfo = player[0]
    offensive_stats: OffensiveStats = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)

    offensive_stats: PassingStats = _get_passing_stats(offensive_stats=offensive_stats)

    player_passing_stats: PlayerPassingStats = PlayerPassingStats(
        player_details=player_details,
        passing_stats=offensive_stats
    )

    return player_passing_stats


def _get_passing_stats(offensive_stats: OffensiveStats) -> PassingStats:

    offensive_stats: PassingStats = PassingStats(
        pass_yards=offensive_stats.pass_yards,
        longest_pass=offensive_stats.longest_pass,
        year=offensive_stats.year,
        pass_tds=offensive_stats.pass_tds,
        games_played=offensive_stats.games_played,
        completions=offensive_stats.completions,
        ints=offensive_stats.ints,
        pass_att=offensive_stats.pass_att
    )

    return offensive_stats


################################################
########## Get player rushing stats ############
################################################
def _get_player_rushing_stats(player) -> PlayerRushingStats:

    player_info: PlayerInfo = player[0]
    offensive_stats: OffensiveStats = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    rushing_stats: RushingStats = _get_rushing_stats(offensive_stats=offensive_stats)

    player_rushing_stats: PlayerRushingStats = PlayerRushingStats(
        player_details=player_details,
        rushing_stats=rushing_stats
    )

    return player_rushing_stats


def _get_rushing_stats(offensive_stats: OffensiveStats) -> RushingStats:

    rushing_stats: RushingStats = RushingStats(
        rush_att=offensive_stats.rush_att,
        rush_yards=offensive_stats.rush_yards,
        ya_contact=offensive_stats.ya_contact,
        broke_tkls=offensive_stats.broke_tkls,
        fumbles=offensive_stats.fumbles,
        twenty_plus_yd_runs=offensive_stats.twenty_plus_yd_runs,
        year=offensive_stats.year
    )
    
    return rushing_stats
