
from typing import List
from src.constants import session
from src.data_models.DefensiveStatsData import DefensiveStatsData
from src.data_models.KickingStatsData import KickingStatsData
from src.data_models.OffensiveStatsData import OffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.ReturnStatsData import ReturnStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.WeekYearData import WeekYearData
from src.models.Player import PlayerAbilities, PlayerAbilitiesDetailsStats, PlayerDetails, PlayerSeasonAndCareerStats, PlayerStats
from src.models.Stats import DefensiveStats, KickingStats, PassingStats, PlayerDefensiveStats, PlayerKickingStats, PlayerPassingStats, PlayerReceivingStats, PlayerReturnStats, PlayerRushingStats, ReceivingStats, ReturnStats, RushingStats


##################################################
#### Get player details, abilities, and stats ####
##################################################
def _get_player_abilities_details_stats(player: PlayerInfoData) -> PlayerAbilitiesDetailsStats:

    player_details: PlayerDetails = _get_player_details(player=player)
    player_abilities: PlayerAbilities = _get_player_abilities(player=player)
    season_stats: PlayerStats = _get_player_season_stats(player=player)
    career_stats: PlayerStats = _get_player_career_stats(player=player)
    
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


def _get_player_career_stats(player: PlayerInfoData) -> PlayerStats:

    offensive_stats_data: List[OffensiveStatsData] = session.query(OffensiveStatsData).where(
        OffensiveStatsData.player_id == player.id,
    ).all()
    defensive_stats_data: List[DefensiveStatsData] = session.query(DefensiveStatsData).where(
        DefensiveStatsData.player_id == player.id,
    ).all()
    return_stats_data: List[ReturnStatsData] = session.query(ReturnStatsData).where(
        ReturnStatsData.player_id == player.id,
    ).all()
    kicking_stats_data: List[KickingStatsData] = session.query(KickingStatsData).where(
        KickingStatsData.player_id == player.id,
    ).all()

    passing_stats: PassingStats = None
    receiving_stats: ReceivingStats = None
    rushing_stats: RushingStats = None
    defensive_stats: DefensiveStats = None
    return_stats: ReturnStats = None
    kicking_stats: KickingStats = None

    if len(offensive_stats_data) > 0:
        passing_stats = _get_career_passing_stats(offensive_stats_data)
        receiving_stats = _get_career_receiving_stats(offensive_stats_data)
        rushing_stats = _get_career_rushing_stats(offensive_stats_data)
    if len(defensive_stats_data) > 0:
        defensive_stats = _get_career_defensive_stats(defensive_stats_data)
    if len(return_stats_data) > 0:
        return_stats = _get_career_return_stats(return_stats_data)
    if len(kicking_stats_data) > 0:
        kicking_stats = _get_career_kicking_stats(kicking_stats_data)
    
    player_stats: PlayerStats = PlayerStats(
        passing_stats=passing_stats,
        rushing_stats=rushing_stats,
        receiving_stats=receiving_stats,
        defensive_stats=defensive_stats,
        return_stats=return_stats,
        kicking_stats=kicking_stats
    )

    return player_stats


def _get_player_season_stats(player: PlayerInfoData) -> PlayerStats:

    week_year: WeekYearData = session.query(WeekYearData).first()

    offensive_stats_data: OffensiveStatsData = session.query(OffensiveStatsData).where(
        OffensiveStatsData.player_id == player.id,
        OffensiveStatsData.year == week_year.year
    ).scalar()
    defensive_stats_data: DefensiveStatsData = session.query(DefensiveStatsData).where(
        DefensiveStatsData.player_id == player.id,
        DefensiveStatsData.year == week_year.year
    ).scalar()
    return_stats_data: ReturnStatsData = session.query(ReturnStatsData).where(
        ReturnStatsData.player_id == player.id,
        ReturnStatsData.year == week_year.year
    ).scalar()
    kicking_stats_data: KickingStatsData = session.query(KickingStatsData).where(
        KickingStatsData.player_id == player.id,
        KickingStatsData.year == week_year.year
    ).scalar()

    passing_stats: PassingStats = None
    receiving_stats: ReceivingStats = None
    rushing_stats: RushingStats = None
    defensive_stats: DefensiveStats = None
    return_stats: ReturnStats = None
    kicking_stats: KickingStats = None

    if offensive_stats_data:
        passing_stats = _get_season_passing_stats(offensive_stats_data)
        receiving_stats = _get_season_receiving_stats(offensive_stats_data)
        rushing_stats = _get_season_rushing_stats(offensive_stats_data)
    if defensive_stats_data:
        defensive_stats = _get_season_defensive_stats(defensive_stats_data)
    if return_stats_data:
        return_stats = _get_season_return_stats(return_stats_data)
    if kicking_stats_data:
        kicking_stats = _get_season_kicking_stats(kicking_stats_data)
    
    player_stats: PlayerStats = PlayerStats(
        passing_stats=passing_stats,
        rushing_stats=rushing_stats,
        receiving_stats=receiving_stats,
        defensive_stats=defensive_stats,
        return_stats=return_stats,
        kicking_stats=kicking_stats
    )

    return player_stats


################################################
######### Get player defensive stats ###########
################################################
def _get_season_defensive_stats(defensive_stats: DefensiveStatsData) -> DefensiveStats:

    defensive_stats_all: DefensiveStats = DefensiveStats(
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
        int_ret_yards=defensive_stats.int_ret_yards,
        total_tkls=defensive_stats.total_tkls,
        total_sacks=defensive_stats.total_sacks
    )

    return defensive_stats_all


def _get_player_defensive_stats(player) -> PlayerDefensiveStats:

    player_info: PlayerInfoData = player[0]
    def_stats: DefensiveStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    defensive_stats: DefensiveStatsData = _get_season_defensive_stats(defensive_stats=def_stats)

    player_defensive_stats: PlayerDefensiveStats = PlayerDefensiveStats(
        player_details=player_details,
        defensive_stats=defensive_stats
    )

    return player_defensive_stats


def _get_career_defensive_stats(defensive_stats: List[DefensiveStatsData]) -> DefensiveStats:

    yearly_def_stats: List[DefensiveStats] = [_get_season_defensive_stats(year) for year in defensive_stats]
    
    long_int_ret = max([stats.long_int_ret for stats in yearly_def_stats])
    sacks = sum([stats.sacks for stats in yearly_def_stats])
    forced_fumbles = sum([stats.forced_fumbles for stats in yearly_def_stats])
    games_played = sum([stats.games_played for stats in yearly_def_stats])
    solo_tkls = sum([stats.solo_tkls for stats in yearly_def_stats])
    safeties = sum([stats.safeties for stats in yearly_def_stats])
    pass_def = sum([stats.pass_def for stats in yearly_def_stats])
    blocked_kicks = sum([stats.blocked_kicks for stats in yearly_def_stats])
    tfl = sum([stats.tfl for stats in yearly_def_stats])
    ints_made = sum([stats.ints_made for stats in yearly_def_stats])
    fumbles_rec = sum([stats.fumbles_rec for stats in yearly_def_stats])
    half_a_sack = sum([stats.half_a_sack for stats in yearly_def_stats])
    asst_tkls = sum([stats.asst_tkls for stats in yearly_def_stats])
    def_tds = sum([stats.def_tds for stats in yearly_def_stats])
    fum_rec_yards = sum([stats.fum_rec_yards for stats in yearly_def_stats])
    int_ret_yards = sum([stats.int_ret_yards for stats in yearly_def_stats])
    total_tkls = sum([solo_tkls, asst_tkls])
    total_sacks = sum([sacks, half_a_sack])
    
    career_def_stats: DefensiveStats = DefensiveStats(
        long_int_ret=long_int_ret,
        sacks=sacks,
        forced_fumbles=forced_fumbles,
        games_played=games_played,
        solo_tkls=solo_tkls,
        safeties=safeties,
        pass_def=pass_def,
        blocked_kicks=blocked_kicks,
        tfl=tfl,
        ints_made=ints_made,
        fumbles_rec=fumbles_rec,
        half_a_sack=half_a_sack,
        asst_tkls=asst_tkls,
        def_tds=def_tds,
        fum_rec_yards=fum_rec_yards,
        int_ret_yards=int_ret_yards,
        total_tkls=total_tkls,
        year=None,
        total_sacks=total_sacks
    )
    
    return career_def_stats


################################################
########## Get player kicking stats ############
################################################
def _get_career_kicking_stats(kicking_stats: List[KickingStatsData]) -> KickingStats:

    yearly_kick_stats: List[KickingStats] = [_get_season_kicking_stats(year) for year in kicking_stats]
    
    fg_made_17_29 = sum([stats.fg_made_17_29 for stats in yearly_kick_stats])
    fg_att_17_29 = sum([stats.fg_att_17_29 for stats in yearly_kick_stats])
    long_fg = max([stats.long_fg for stats in yearly_kick_stats])
    ko_touchbacks = sum([stats.ko_touchbacks for stats in yearly_kick_stats])
    long_punt = max([stats.long_punt for stats in yearly_kick_stats])
    xp_att = sum([stats.xp_att for stats in yearly_kick_stats])
    punts_blocked = sum([stats.punts_blocked for stats in yearly_kick_stats])
    fg_att = sum([stats.fg_att for stats in yearly_kick_stats])
    total_punt_yards = sum([stats.total_punt_yards for stats in yearly_kick_stats])
    xp_blocked = sum([stats.xp_blocked for stats in yearly_kick_stats])
    fg_blocked = sum([stats.fg_blocked for stats in yearly_kick_stats])
    fg_att_40_49 = sum([stats.fg_att_40_49 for stats in yearly_kick_stats])
    fg_made_40_49 = sum([stats.fg_made_40_49 for stats in yearly_kick_stats])
    fg_att_30_39 = sum([stats.fg_att_30_39 for stats in yearly_kick_stats])
    fg_made_30_39 = sum([stats.fg_made_30_39 for stats in yearly_kick_stats])
    fg_att_50_plus = sum([stats.fg_att_50_plus for stats in yearly_kick_stats])
    fg_made_50_plus = sum([stats.fg_made_50_plus for stats in yearly_kick_stats])
    punt_touchbacks = sum([stats.punt_touchbacks for stats in yearly_kick_stats])
    games_played = sum([stats.games_played for stats in yearly_kick_stats])
    kickoffs = sum([stats.kickoffs for stats in yearly_kick_stats])
    xp_made = sum([stats.xp_made for stats in yearly_kick_stats])
    net_punting = sum([stats.net_punting for stats in yearly_kick_stats])
    fg_made = sum([stats.fg_made for stats in yearly_kick_stats])
    number_punts = sum([stats.number_punts for stats in yearly_kick_stats])
    inside_twenty = sum([stats.inside_twenty for stats in yearly_kick_stats])
    fg_pct = round(fg_made / fg_att * 100, 1)
    xp_pct = round(xp_made / xp_att * 100, 1)
    fg_50_plus_pct = round(fg_made_50_plus / fg_att_50_plus * 100, 1)
    punt_avg = round(total_punt_yards / number_punts, 1)
    
    career_kicking_stats: KickingStats = KickingStats(
        fg_made_17_29=fg_made_17_29,
        fg_att_17_29=fg_att_17_29,
        long_fg=long_fg,
        ko_touchbacks=ko_touchbacks,
        long_punt=long_punt,
        xp_att=xp_att,
        punts_blocked=punts_blocked,
        fg_att=fg_att,
        total_punt_yards=total_punt_yards,
        xp_blocked=xp_blocked,
        fg_blocked=fg_blocked,
        fg_att_40_49=fg_att_40_49,
        fg_made_40_49=fg_made_40_49,
        fg_att_30_39=fg_att_30_39,
        fg_made_30_39=fg_made_30_39,
        fg_att_50_plus=fg_att_50_plus,
        fg_made_50_plus=fg_made_50_plus,
        punt_touchbacks=punt_touchbacks,
        games_played=games_played,
        kickoffs=kickoffs,
        xp_made=xp_made,
        net_punting=net_punting,
        fg_made=fg_made,
        number_punts=number_punts,
        inside_twenty=inside_twenty,
        year=None,
        fg_pct=fg_pct,
        xp_pct=xp_pct,
        fg_50_plus_pct=fg_50_plus_pct,
        punt_avg=punt_avg
    )
    
    return career_kicking_stats


def _get_season_kicking_stats(kicking_stats: KickingStatsData) -> KickingStats:

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
        fg_pct=kicking_stats.fg_pct,
        xp_pct=kicking_stats.xp_pct,
        fg_50_plus_pct=kicking_stats.fg_50_plus_pct,
        punt_avg=kicking_stats.punt_avg
    )

    return kicking_stats_all


def _get_player_kicking_stats(player) -> PlayerKickingStats:

    player_info: PlayerInfoData = player[0]
    kicking_stats_data: KickingStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    kicking_stats: KickingStats = _get_season_kicking_stats(kicking_stats=kicking_stats_data)

    player_kicking_stats: PlayerKickingStats = PlayerKickingStats(
        player_details=player_details,
        kicking_stats=kicking_stats
    )

    return player_kicking_stats


################################################
########## Get player passing stats ############
################################################
def _get_player_passing_stats(player) -> PlayerPassingStats:

    player_info: PlayerInfoData = player[0]
    off_stats: OffensiveStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    passing_stats: PassingStats = _get_season_passing_stats(offensive_stats=off_stats)

    player_passing_stats: PlayerPassingStats = PlayerPassingStats(
        player_details=player_details,
        passing_stats=passing_stats
    )

    return player_passing_stats


def _get_season_passing_stats(offensive_stats: OffensiveStatsData) -> PassingStats:

    passing_stats: PassingStats = PassingStats(
        pass_yards=offensive_stats.pass_yards,
        longest_pass=offensive_stats.longest_pass,
        year=offensive_stats.year,
        pass_tds=offensive_stats.pass_tds,
        games_played=offensive_stats.games_played,
        completions=offensive_stats.completions,
        ints=offensive_stats.ints,
        pass_att=offensive_stats.pass_att,
        pass_yp_attempt=offensive_stats.pass_yp_attempt,
        pass_yp_game=offensive_stats.pass_yp_game,
        pass_rating=offensive_stats.pass_rating
    )

    return passing_stats


def _get_career_passing_stats(offensive_stats: List[OffensiveStatsData]) -> PassingStats:

    yearly_passing_stats: List[PassingStats] = [_get_season_passing_stats(year) for year in offensive_stats]
    
    pass_yards = sum([stats.pass_yards for stats in yearly_passing_stats])
    longest_pass = max([stats.longest_pass for stats in yearly_passing_stats])
    pass_tds = sum([stats.pass_tds for stats in yearly_passing_stats])
    games_played = sum([stats.games_played for stats in yearly_passing_stats])
    completions = sum([stats.completions for stats in yearly_passing_stats])
    ints = sum([stats.ints for stats in yearly_passing_stats])
    pass_att = sum([stats.pass_att for stats in yearly_passing_stats])
    pass_yp_attempt = round(
        pass_yards / pass_att if pass_att != 0 else 0,
        1
    )
    pass_yp_game = round(pass_yards / games_played, 1)
    pass_rating_calc = (
        0 if pass_att == 0 else \
        ((8.4 * pass_yards) + (330 * pass_tds) + \
        (100 * completions) - (200 * ints)) / pass_att
        )
    pass_rating = round(pass_rating_calc, 1)
    
    career_passing_stats: PassingStats = PassingStats(
        pass_yards=pass_yards,
        longest_pass=longest_pass,
        pass_tds=pass_tds,
        games_played=games_played,
        completions=completions,
        ints=ints,
        pass_att=pass_att,
        pass_yp_attempt=pass_yp_attempt,
        pass_yp_game=pass_yp_game,
        pass_rating=pass_rating,
        year=None
    )
    
    return career_passing_stats


##################################################
########## Get player receiving stats ############
##################################################
def _get_season_receiving_stats(offensive_stats: OffensiveStatsData) -> ReceivingStats:

    receiving_stats: ReceivingStats = ReceivingStats(
        receptions=offensive_stats.receptions,
        rec_yards=offensive_stats.rec_yards,
        rec_tds=offensive_stats.rec_tds,
        yac=offensive_stats.yac,
        drops=offensive_stats.drops,
        rec_yp_catch=offensive_stats.rec_yp_catch,
        rec_yp_game=offensive_stats.rec_yp_game,
        games_played=offensive_stats.games_played,
        year=offensive_stats.year
    )

    return receiving_stats


def _get_career_receiving_stats(offensive_stats: List[OffensiveStatsData]) -> ReceivingStats:
    
    yearly_rec_stats: List[ReceivingStats] = [_get_season_receiving_stats(year) for year in offensive_stats]
    
    receptions = sum([stats.receptions for stats in yearly_rec_stats])
    rec_yards = sum([stats.rec_yards for stats in yearly_rec_stats])
    rec_tds = sum([stats.rec_tds for stats in yearly_rec_stats])
    games_played = sum([stats.games_played for stats in yearly_rec_stats])
    yac = sum([stats.yac for stats in yearly_rec_stats])
    drops = sum([stats.drops for stats in yearly_rec_stats])
    rec_yp_catch = round(
        rec_yards / receptions if receptions != 0 else 0,
        1
    )
    rec_yp_game = round(rec_yards / games_played, 1)

    
    career_receiving_stats: ReceivingStats = ReceivingStats(
        receptions=receptions,
        rec_yards=rec_yards,
        rec_tds=rec_tds,
        games_played=games_played,
        yac=yac,
        drops=drops,
        rec_yp_catch=rec_yp_catch,
        rec_yp_game=rec_yp_game,
        year=None
    )
    
    return career_receiving_stats


def _get_player_receiving_stats(player) -> PlayerReceivingStats:

    player_info: PlayerInfoData = player[0]
    offensive_stats: OffensiveStatsData = player[1]

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
def _get_season_return_stats(return_stats: ReturnStatsData) -> ReturnStats:

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
        pr_yds=return_stats.pr_yds,
        kr_avg=return_stats.kr_avg,
        pr_avg=return_stats.pr_avg
    )

    return converted_return_stats


def _get_player_return_stats(player) -> PlayerReturnStats:

    player_info: PlayerInfoData = player[0]
    return_stats_data: ReturnStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    return_stats: ReturnStats = _get_season_return_stats(return_stats=return_stats_data)

    player_kicking_stats: PlayerReturnStats = PlayerReturnStats(
        player_details=player_details,
        return_stats=return_stats
    )

    return player_kicking_stats


def _get_career_return_stats(return_stats: List[ReturnStatsData]) -> ReturnStats:
    
    yearly_rec_stats: List[ReturnStats] = [_get_season_return_stats(year) for year in return_stats]
    
    kick_returns = sum([stats.kick_returns for stats in yearly_rec_stats])
    long_kr = max([stats.long_kr for stats in yearly_rec_stats])
    punt_returns = sum([stats.punt_returns for stats in yearly_rec_stats])
    long_pr = max([stats.long_pr for stats in yearly_rec_stats])
    games_played = sum([stats.games_played for stats in yearly_rec_stats])
    kr_tds = sum([stats.kr_tds for stats in yearly_rec_stats])
    pr_tds = sum([stats.pr_tds for stats in yearly_rec_stats])
    kr_yds = sum([stats.kr_yds for stats in yearly_rec_stats])
    pr_yds = sum([stats.pr_yds for stats in yearly_rec_stats])
    kr_avg = round(
        kr_yds / kick_returns if kick_returns != 0 else 0,
        1
    )
    pr_avg = round(
        pr_yds / punt_returns if punt_returns != 0 else 0,
        1
    )
    
    career_return_stats: ReturnStats = ReturnStats(
        kick_returns=kick_returns,
        long_kr=long_kr,
        punt_returns=punt_returns,
        games_played=games_played,
        long_pr=long_pr,
        kr_tds=kr_tds,
        pr_tds=pr_tds,
        kr_yds=kr_yds,
        pr_yds=pr_yds,
        kr_avg=kr_avg,
        pr_avg=pr_avg,
        year=None
    )
    
    return career_return_stats


################################################
########## Get player rushing stats ############
################################################
def _get_player_rushing_stats(player) -> PlayerRushingStats:

    player_info: PlayerInfoData = player[0]
    offensive_stats: OffensiveStatsData = player[1]

    player_details: PlayerDetails = _get_player_details(player=player_info)
    rushing_stats: RushingStats = _get_season_rushing_stats(offensive_stats=offensive_stats)

    player_rushing_stats: PlayerRushingStats = PlayerRushingStats(
        player_details=player_details,
        rushing_stats=rushing_stats
    )

    return player_rushing_stats


def _get_season_rushing_stats(offensive_stats: OffensiveStatsData) -> RushingStats:

    rushing_stats: RushingStats = RushingStats(
        rush_att=offensive_stats.rush_att,
        rush_yards=offensive_stats.rush_yards,
        rush_tds=offensive_stats.rush_tds,
        ya_contact=offensive_stats.ya_contact,
        broke_tkls=offensive_stats.broke_tkls,
        fumbles=offensive_stats.fumbles,
        twenty_plus_yd_runs=offensive_stats.twenty_plus_yd_runs,
        rush_yp_carry=offensive_stats.rush_yp_carry,
        rush_yp_game=offensive_stats.rush_yp_game,
        games_played=offensive_stats.games_played,
        year=offensive_stats.year
    )
    
    return rushing_stats


def _get_career_rushing_stats(offensive_stats: List[OffensiveStatsData]) -> RushingStats:
    
    yearly_rush_stats: List[RushingStats] = [_get_season_rushing_stats(year) for year in offensive_stats]
    
    rush_att = sum([stats.rush_att for stats in yearly_rush_stats])
    rush_yards = sum([stats.rush_yards for stats in yearly_rush_stats])
    rush_tds = sum([stats.rush_tds for stats in yearly_rush_stats])
    games_played = sum([stats.games_played for stats in yearly_rush_stats])
    ya_contact = sum([stats.ya_contact for stats in yearly_rush_stats])
    broke_tkls = sum([stats.broke_tkls for stats in yearly_rush_stats])
    fumbles = sum([stats.fumbles for stats in yearly_rush_stats])
    twenty_plus_yd_runs = sum([stats.twenty_plus_yd_runs for stats in yearly_rush_stats])

    rush_yp_carry = round(
        rush_yards / rush_att if rush_att != 0 else 0,
        1
    )
    rush_yp_game = round(rush_yards / games_played, 1)

    
    career_rushing_stats: RushingStats = RushingStats(
        rush_att=rush_att,
        rush_yards=rush_yards,
        rush_tds=rush_tds,
        games_played=games_played,
        ya_contact=ya_contact,
        broke_tkls=broke_tkls,
        fumbles=fumbles,
        twenty_plus_yd_runs=twenty_plus_yd_runs,
        rush_yp_carry=rush_yp_carry,
        rush_yp_game=rush_yp_game,
        year=None
    )
    
    return career_rushing_stats