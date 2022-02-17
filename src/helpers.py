<<<<<<< Updated upstream
from typing import List
from src.constants import(
    Positions,
    session
)
from src.data_models.DefensiveStats import DefensiveStats
from src.data_models.KickingStats import KickingStats as KickingStatsDataModel
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.data_models.ReturnStats import ReturnStats as ReturnStatsDataModel
from src.data_models.TeamInfo import TeamInfo
from src.models.Player import(
=======
from constants import session
from data_models.DefensiveStats import DefensiveStats
from data_models.KickingStats import KickingStats as KickingStatsDataModel
from data_models.OffensiveStats import OffensiveStats
from data_models.PlayerInfo import PlayerInfo
from data_models.ReturnStats import ReturnStats as ReturnStatsDataModel
from data_models.TeamInfo import TeamInfo
from models.Player import(
>>>>>>> Stashed changes
    Player, 
    PlayerAbilities, 
    PlayerDetails
)
from models.Stats import(
    DefensiveStatsAll,
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
from src.models.Team import Team, TeamRoster


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
######### Get player defensive stats ###########
################################################
def _get_defensive_stats(defensive_stats: DefensiveStats) -> DefensiveStatsAll:

    defensive_stats_all: DefensiveStatsAll = DefensiveStatsAll(
        long_int_ret=defensive_stats.long_int_ret,
        sacks=defensive_stats.sacks,
        year=defensive_stats.year,
        forced_fumbles=defensive_stats.forced_fumbles,
        solo_tkls=defensive_stats.solo_tkls,
        safeties=defensive_stats.safeties,
        pass_def=defensive_stats.pass_def,
        blocked_kicks=defensive_stats.blocked_kicks,
        tfl=defensive_stats.tfl,
        ints_made=defensive_stats.ints_made,
        games_played=defensive_stats.games_played,
        fumbles_rec=defensive_stats.fumbles_rec,
        half_a_sack=defensive_stats.half_a_sack,
        asst_tkls=defensive_stats.asst_tkls,
        def_tds=defensive_stats.def_tds,
        fum_rec_yards=defensive_stats.fum_rec_yards,
        int_ret_yards=defensive_stats.int_ret_yards
    )

    return defensive_stats_all


def _get_player_defensive_stats(player) -> PlayerDefensiveStats:

    player_info: PlayerInfo = player[0]
    def_stats: DefensiveStats = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    defensive_stats: DefensiveStats = _get_defensive_stats(defensive_stats=def_stats)

    player_defensive_stats: PlayerDefensiveStats = PlayerDefensiveStats(
        player_details=player_details,
        defensive_stats=defensive_stats
    )

    return player_defensive_stats


################################################
######### Get player kicking stats ###########
################################################
def _get_kicking_stats(kicking_stats: KickingStatsDataModel) -> KickingStats:

    kicking_stats_all: KickingStats = KickingStats(
        fg_made_17_29=kicking_stats.fg_made_17_29,
        fg_att_17_29=kicking_stats.fg_att_17_29,
        long_fg=kicking_stats.long_fg,
        ko_touchbacks=kicking_stats.ko_touchbacks,
        long_punt=kicking_stats.long_punt,
        xp_att=kicking_stats.xp_att,
        year=kicking_stats.year,
        punts_blocked=kicking_stats.punts_blocked,
        fg_att=kicking_stats.fg_att,
        total_punt_yards=kicking_stats.total_punt_yards,
        xp_blocked=kicking_stats.xp_blocked,
        fg_blocked=kicking_stats.fg_blocked,
        fg_att_40_49=kicking_stats.fg_att_40_49,
        fg_made_40_49=kicking_stats.fg_made_40_49,
        fg_att_30_39=kicking_stats.fg_att_30_39,
        fg_made_30_39=kicking_stats.fg_made_30_39,
        fg_att_50_plus=kicking_stats.fg_att_50_plus,
        fg_made_50_plus=kicking_stats.fg_made_50_plus,
        punt_touchbacks=kicking_stats.punt_touchbacks,
        games_played=kicking_stats.games_played,
        kickoffs=kicking_stats.kickoffs,
        xp_made=kicking_stats.xp_made,
        net_punting=kicking_stats.net_punting,
        fg_made=kicking_stats.fg_made,
        number_punts=kicking_stats.number_punts,
        inside_twenty=kicking_stats.inside_twenty,
    )

    return kicking_stats_all


def _get_player_kicking_stats(player) -> PlayerKickingStats:

    player_info: PlayerInfo = player[0]
    kicking_stats_data: KickingStatsDataModel = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    kicking_stats: KickingStats = _get_kicking_stats(kicking_stats=kicking_stats_data)

    player_kicking_stats: PlayerKickingStats = PlayerKickingStats(
        player_details=player_details,
        kicking_stats=kicking_stats
    )

    return player_kicking_stats


################################################
########## Get player passing stats ############
################################################
def _get_player_passing_stats(player) -> PlayerPassingStats:

    player_info: PlayerInfo = player[0]
    off_stats: OffensiveStats = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    passing_stats: PassingStats = _get_passing_stats(offensive_stats=off_stats)

    player_passing_stats: PlayerPassingStats = PlayerPassingStats(
        player_details=player_details,
        passing_stats=passing_stats
    )

    return player_passing_stats


def _get_passing_stats(offensive_stats: OffensiveStats) -> PassingStats:

    passing_stats: PassingStats = PassingStats(
        pass_yards=offensive_stats.pass_yards,
        longest_pass=offensive_stats.longest_pass,
        year=offensive_stats.year,
        pass_tds=offensive_stats.pass_tds,
        games_played=offensive_stats.games_played,
        completions=offensive_stats.completions,
        ints=offensive_stats.ints,
        pass_att=offensive_stats.pass_att
    )

    return passing_stats


##################################################
########## Get player receiving stats ############
##################################################
def _get_receiving_stats(offensive_stats: OffensiveStats) -> ReceivingStats:

    receiving_stats: ReceivingStats = ReceivingStats(
        receptions=offensive_stats.receptions,
        rec_yards=offensive_stats.rec_yards,
        rec_tds=offensive_stats.rec_tds,
        yac=offensive_stats.yac,
        drops=offensive_stats.drops
    )

    return receiving_stats


def _get_player_receiving_stats(player) -> PlayerReceivingStats:

    player_info: PlayerInfo = player[0]
    offensive_stats: OffensiveStats = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    receiving_stats: ReceivingStats = _get_receiving_stats(offensive_stats=offensive_stats)

    player_receiving_stats: PlayerReceivingStats = PlayerReceivingStats(
        player_details=player_details,
        receiving_stats=receiving_stats
    )

    return player_receiving_stats


##############################################
######### Get player return stats ###########
##############################################
def _get_return_stats(return_stats: ReturnStatsDataModel) -> ReturnStats:

    converted_return_stats: ReturnStats = ReturnStats(
        kick_returns=return_stats.kick_returns,
        year=return_stats.year,
        long_kr=return_stats.long_kr,
        punt_returns=return_stats.punt_returns,
        long_pr=return_stats.long_pr,
        games_played=return_stats.games_played,
        kr_tds=return_stats.kr_tds,
        pr_tds=return_stats.pr_tds,
        kr_yds=return_stats.kr_yds,
        pr_yds=return_stats.pr_yds
    )

    return converted_return_stats


def _get_player_return_stats(player) -> PlayerReturnStats:

    player_info: PlayerInfo = player[0]
    return_stats_data: ReturnStatsDataModel = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    return_stats: ReturnStats = _get_return_stats(return_stats=return_stats_data)

    player_kicking_stats: PlayerReturnStats = PlayerReturnStats(
        player_details=player_details,
        return_stats=return_stats
    )

    return player_kicking_stats


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


################################################
########## Get team info and stats #############
################################################
def _get_team_info(team_info: TeamInfo, players: List[PlayerInfo]) -> Team:

    offense_players: List[PlayerInfo] = [player for player in players if player.position in Positions.offense_positions]
    defense_players: List[PlayerInfo] = [player for player in players if player.position in Positions.defense_positions]
    sp_team_players: List[PlayerInfo] = [player for player in players if player.position in Positions.sp_teams_positions]

    avg_overall = round(sum([player.overall for player in players]) / len(players), 1)
    avg_offense = round(sum(player.overall for player in offense_players) / len(offense_players), 1)
    avg_defense = round(sum(player.overall for player in defense_players) / len(defense_players), 1)
    avg_sp_teams = round(sum(player.overall for player in sp_team_players) / len(sp_team_players), 1)

    team: Team = Team(
        id=team_info.id,
        team_name=team_info.team_name,
        team_short_name=team_info.team_short_name,
        is_user=team_info.is_user,
        avg_overall=avg_overall,
        avg_offense=avg_offense,
        avg_defense=avg_defense,
        avg_sp_teams=avg_sp_teams,
        coachs_poll_1st_votes=team_info.coachs_poll_1st_votes,
        nickname=team_info.nickname,
        wins=team_info.wins,
        bcs_rank=team_info.bcs_rank,
        coachs_poll_rank=team_info.coachs_poll_rank,
        media_poll_rank=team_info.media_poll_rank,
        losses=team_info.losses,
        media_poll_points=team_info.media_poll_points,
        coachs_poll_points=team_info.coachs_poll_points
    )

    return team


def _get_team_roster(player: PlayerInfo) -> TeamRoster:

    player_details: TeamRoster = TeamRoster(
        id=player.id,
        first_name=player.first_name,
        last_name=player.last_name,
        height=player.height,
        weight=player.weight,
        jersey_number=player.jersey_number,
        player_year=player.player_year,
        redshirt=player.redshirt,
        position=player.position,
        hometown_desc=player.hometown_desc,
        overall=player.overall
    )

    return player_details



def _get_team_stats(team_info: TeamInfo, players: List[PlayerInfo]):
    # TODO: create function to get team passing stats, rushing stats, etc.
    pass
