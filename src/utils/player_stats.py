from src.constants import session
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.models.Player import (
    PlayerAbilities,
    PlayerAbilitiesDetailsStats,
    PlayerDetails,
    PlayerSeasonAndCareerStats,
    PlayerStats
)
from src.models.Stats import (
    KickingStats,
    PassingStats,
    PlayerDefensiveStats,
    PlayerKickingStats,
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerReturnStats,
    PlayerRushingStats,
    ReceivingStats,
    ReturnStats,
    RushingStats
)
from src.utils.career_stats import (
    _compile_player_career_stats
)
from src.utils.season_stats import (
    _get_player_season_stats,
    _get_season_defensive_stats,
    _get_season_kicking_stats,
    _get_season_passing_stats,
    _get_season_receiving_stats,
    _get_season_return_stats,
    _get_season_rushing_stats
)


##################################################
#### Get player details, abilities, and stats ####
##################################################
def _get_player_abilities_details_stats(player: PlayerInfoData) -> PlayerAbilitiesDetailsStats:

    player_details: PlayerDetails = _get_player_details(player=player)
    player_abilities: PlayerAbilities = _get_player_abilities(player=player)
    season_stats: PlayerStats = _get_player_season_stats(player=player)
    career_stats: PlayerStats = _compile_player_career_stats(player=player)
    
    stats: PlayerSeasonAndCareerStats = PlayerSeasonAndCareerStats(
        season=season_stats,
        career=career_stats
    )

    player_abilities_details_stats: PlayerAbilitiesDetailsStats = PlayerAbilitiesDetailsStats(
        details=player_details,
        abilities=player_abilities,
        stats=stats
    )

    return player_abilities_details_stats


def _get_player_abilities(player: PlayerInfoData) -> PlayerAbilities:

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


def _get_player_details(player: PlayerInfoData) -> PlayerDetails:

    team_info: TeamInfoData = session.query(TeamInfoData).filter(TeamInfoData.id == player.team_id).one()

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


########################################
########## Get player stats ############
########################################
def _get_player_defensive_stats(player) -> PlayerDefensiveStats:

    player_info: PlayerInfoData = player[0]
    def_stats: SeasonDefensiveStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    defensive_stats: SeasonDefensiveStatsData = _get_season_defensive_stats(defensive_stats=def_stats)

    player_defensive_stats: PlayerDefensiveStats = PlayerDefensiveStats(
        player_details=player_details,
        defensive_stats=defensive_stats
    )

    return player_defensive_stats


def _get_player_kicking_stats(player) -> PlayerKickingStats:

    player_info: PlayerInfoData = player[0]
    kicking_stats_data: SeasonKickingStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    kicking_stats: KickingStats = _get_season_kicking_stats(kicking_stats=kicking_stats_data)

    player_kicking_stats: PlayerKickingStats = PlayerKickingStats(
        player_details=player_details,
        kicking_stats=kicking_stats
    )

    return player_kicking_stats


def _get_player_passing_stats(player) -> PlayerPassingStats:

    player_info: PlayerInfoData = player[0]
    off_stats: SeasonOffensiveStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    passing_stats: PassingStats = _get_season_passing_stats(offensive_stats=off_stats)

    player_passing_stats: PlayerPassingStats = PlayerPassingStats(
        player_details=player_details,
        passing_stats=passing_stats
    )

    return player_passing_stats


def _get_player_receiving_stats(player) -> PlayerReceivingStats:

    player_info: PlayerInfoData = player[0]
    offensive_stats: SeasonOffensiveStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    receiving_stats: ReceivingStats = _get_season_receiving_stats(offensive_stats=offensive_stats)

    player_receiving_stats: PlayerReceivingStats = PlayerReceivingStats(
        player_details=player_details,
        receiving_stats=receiving_stats
    )

    return player_receiving_stats


##############################################
######### Get player return stats ###########
##############################################



def _get_player_return_stats(player) -> PlayerReturnStats:

    player_info: PlayerInfoData = player[0]
    return_stats_data: SeasonReturnStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    return_stats: ReturnStats = _get_season_return_stats(return_stats=return_stats_data)

    player_kicking_stats: PlayerReturnStats = PlayerReturnStats(
        player_details=player_details,
        return_stats=return_stats
    )

    return player_kicking_stats


def _get_player_rushing_stats(player) -> PlayerRushingStats:

    player_info: PlayerInfoData = player[0]
    offensive_stats: SeasonOffensiveStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    rushing_stats: RushingStats = _get_season_rushing_stats(offensive_stats=offensive_stats)

    player_rushing_stats: PlayerRushingStats = PlayerRushingStats(
        player_details=player_details,
        rushing_stats=rushing_stats
    )

    return player_rushing_stats
