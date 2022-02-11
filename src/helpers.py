from src.constants import session
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.data_models.TeamInfo import TeamInfo
from src.models.Player import Player, PlayerAbilities, PlayerDetails
from src.models.Stats import PassingStats, PlayerPassingStats, PlayerRushingStats


def _convert_stats_year(year: int) -> int:
    return year + 2013


def _get_player_details_and_abilities(player: PlayerInfo) -> Player:

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

    converted_player: Player = Player(
        player_details=player_details,
        player_abilities=player_abilities
    )

    return converted_player


def _get_player_passing_stats(player) -> PlayerPassingStats:

    player_info: PlayerDetails = player[0]
    player_passing_stats: OffensiveStats = player[1]

    team_info: TeamInfo = session.query(TeamInfo).filter(TeamInfo.id == player_info.team_id).one()

    player_details: PlayerDetails = PlayerDetails(
        id=player_info.id,
        team_id=player_info.team_id,
        team_name=team_info.team_name,
        first_name=player_info.first_name,
        last_name=player_info.last_name,
        height=player_info.height,
        weight=player_info.weight,
        jersey_number=player_info.jersey_number,
        player_year=player_info.player_year,
        redshirt=player_info.redshirt,
        position=player_info.position,
        hometown_desc=player_info.hometown_desc
    )

    passing_stats: PassingStats = PassingStats(
        pass_yards=player_passing_stats.pass_yards,
        longest_pass=player_passing_stats.longest_pass,
        year=player_passing_stats.year,
        pass_tds=player_passing_stats.pass_tds,
        games_played=player_passing_stats.games_played,
        completions=player_passing_stats.completions,
        ints=player_passing_stats.ints,
        pass_att=player_passing_stats.pass_att
    )

    player_passing_stats: PlayerPassingStats = PlayerPassingStats(
        player_details=player_details,
        passing_stats=passing_stats
    )

    return player_passing_stats


def _get_player_rushing_stats(player) -> PlayerRushingStats:
    pass
