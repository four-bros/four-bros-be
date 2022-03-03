from typing import List
from src.constants import session
from src.data_models.CareerDefensiveStatsData import CareerDefensiveStatsData
from src.data_models.CareerKickingStatsData import CareerKickingStatsData
from src.data_models.CareerOffensiveStatsData import CareerOffensiveStatsData
from src.data_models.CareerReturnStatsData import CareerReturnStatsData
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.models.Player import PlayerStats
from src.models.Stats import (
    DefensiveStats,
    KickingStats,
    PassingStats,
    ReceivingStats,
    ReturnStats,
    RushingStats,
    TotalStats
)
from src.utils.season_stats import (
    _get_defensive_stats,
    _get_kicking_stats,
    _get_passing_stats,
    _get_receiving_stats,
    _get_return_stats,
    _get_rushing_stats,
    _get_total_stats
)


#############################################
### Compile player stats for db insertion ###
#############################################
def _compile_player_career_stats(player: PlayerInfoData) -> PlayerStats:

    offensive_stats_data: List[SeasonOffensiveStatsData] = session.query(SeasonOffensiveStatsData).where(
        SeasonOffensiveStatsData.player_id == player.id,
    ).all()
    defensive_stats_data: List[SeasonDefensiveStatsData] = session.query(SeasonDefensiveStatsData).where(
        SeasonDefensiveStatsData.player_id == player.id,
    ).all()
    return_stats_data: List[SeasonReturnStatsData] = session.query(SeasonReturnStatsData).where(
        SeasonReturnStatsData.player_id == player.id,
    ).all()
    kicking_stats_data: List[SeasonKickingStatsData] = session.query(SeasonKickingStatsData).where(
        SeasonKickingStatsData.player_id == player.id,
    ).all()

    passing_stats: PassingStats = None
    receiving_stats: ReceivingStats = None
    rushing_stats: RushingStats = None
    defensive_stats: DefensiveStats = None
    return_stats: ReturnStats = None
    kicking_stats: KickingStats = None

    if len(offensive_stats_data) > 0:
        passing_stats = _compile_career_passing_stats(offensive_stats_data)
        receiving_stats = _compile_career_receiving_stats(offensive_stats_data)
        rushing_stats = _compile_career_rushing_stats(offensive_stats_data)
    if len(defensive_stats_data) > 0:
        defensive_stats = _compile_career_defensive_stats(defensive_stats_data)
    if len(return_stats_data) > 0:
        return_stats = _compile_career_return_stats(return_stats_data)
    if len(kicking_stats_data) > 0:
        kicking_stats = _compile_career_kicking_stats(kicking_stats_data)
    
    player_stats: PlayerStats = PlayerStats(
        passing=passing_stats,
        rushing=rushing_stats,
        receiving=receiving_stats,
        defensive=defensive_stats,
        kick_return=return_stats,
        kicking=kicking_stats
    )

    return player_stats


def _compile_career_defensive_stats(defensive_stats: List[SeasonDefensiveStatsData]) -> DefensiveStats:

    yearly_def_stats: List[DefensiveStats] = [_get_defensive_stats(year) for year in defensive_stats]
    
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


def _compile_career_kicking_stats(kicking_stats: List[SeasonKickingStatsData]) -> KickingStats:

    yearly_kick_stats: List[KickingStats] = [_get_kicking_stats(year) for year in kicking_stats]
    
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
    fg_pct = 0 if fg_att == 0 else round(fg_made / fg_att * 100, 1)
    xp_pct = 0 if xp_att == 0 else round(xp_made / xp_att * 100, 1)
    fg_50_plus_pct = 0 if fg_att_50_plus == 0 else round(fg_made_50_plus / fg_att_50_plus * 100, 1)
    punt_avg = 0 if number_punts == 0 else round(total_punt_yards / number_punts, 1)
    
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


def _compile_career_passing_stats(offensive_stats: List[SeasonOffensiveStatsData]) -> PassingStats:

    yearly_passing_stats: List[PassingStats] = [_get_passing_stats(year) for year in offensive_stats]
    
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
    sacked = sum([stats.sacked for stats in yearly_passing_stats])
    
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
        year=None,
        sacked=sacked
    )
    
    return career_passing_stats


def _compile_career_receiving_stats(offensive_stats: List[SeasonOffensiveStatsData]) -> ReceivingStats:
    
    yearly_rec_stats: List[ReceivingStats] = [_get_receiving_stats(year) for year in offensive_stats]
    
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
    longest_rec = max([stats.longest_rec for stats in yearly_rec_stats])

    
    career_receiving_stats: ReceivingStats = ReceivingStats(
        receptions=receptions,
        rec_yards=rec_yards,
        rec_tds=rec_tds,
        games_played=games_played,
        yac=yac,
        drops=drops,
        rec_yp_catch=rec_yp_catch,
        rec_yp_game=rec_yp_game,
        year=None,
        longest_rec=longest_rec
    )
    
    return career_receiving_stats


def _compile_career_return_stats(return_stats: List[SeasonReturnStatsData]) -> ReturnStats:
    
    yearly_rec_stats: List[ReturnStats] = [_get_return_stats(year) for year in return_stats]
    
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


def _compile_career_rushing_stats(offensive_stats: List[SeasonOffensiveStatsData]) -> RushingStats:
    
    yearly_rush_stats: List[RushingStats] = [_get_rushing_stats(year) for year in offensive_stats]
    
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
    longest_run = max([stats.longest_run for stats in yearly_rush_stats])

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
        year=None,
        longest_run=longest_run
    )
    
    return career_rushing_stats


def _compile_career_total_stats(offensive_stats: List[SeasonOffensiveStatsData]) -> TotalStats:
    
    yearly_total_stats: List[TotalStats] = [_get_total_stats(year) for year in offensive_stats]
    
    total_yards = sum([stats.total_yards for stats in yearly_total_stats])
    total_tds = sum([stats.total_tds for stats in yearly_total_stats])
    games_played = sum([stats.games_played for stats in yearly_total_stats])
    total_ypg = round(
        total_yards / games_played if games_played != 0 else 0,
        1
    )

    career_total_stats: TotalStats = TotalStats(
        total_yards=total_yards,
        total_tds=total_tds,
        total_ypg=total_ypg,
        games_played=games_played,
        year=None
    )
    
    return career_total_stats


###########################################
### Get player stats for GET endpoints ###
###########################################
def _get_player_career_stats(player: PlayerInfoData) -> PlayerStats:

    offensive_stats_data: List[CareerOffensiveStatsData] = session.query(CareerOffensiveStatsData).where(
        CareerOffensiveStatsData.player_id == player.id,
    ).scalar()
    defensive_stats_data: List[CareerDefensiveStatsData] = session.query(CareerDefensiveStatsData).where(
        CareerDefensiveStatsData.player_id == player.id,
    ).scalar()
    return_stats_data: List[CareerReturnStatsData] = session.query(CareerReturnStatsData).where(
        CareerReturnStatsData.player_id == player.id,
    ).scalar()
    kicking_stats_data: List[CareerKickingStatsData] = session.query(CareerKickingStatsData).where(
        CareerKickingStatsData.player_id == player.id,
    ).scalar()

    passing_stats: PassingStats = None
    receiving_stats: ReceivingStats = None
    rushing_stats: RushingStats = None
    defensive_stats: DefensiveStats = None
    return_stats: ReturnStats = None
    kicking_stats: KickingStats = None

    if offensive_stats_data:
        passing_stats = _get_passing_stats(offensive_stats_data)
        receiving_stats = _get_receiving_stats(offensive_stats_data)
        rushing_stats = _get_rushing_stats(offensive_stats_data)
    if defensive_stats_data:
        defensive_stats = _get_defensive_stats(defensive_stats_data)
    if return_stats_data:
        return_stats = _get_return_stats(return_stats_data)
    if kicking_stats_data:
        kicking_stats = _get_kicking_stats(kicking_stats_data)
    
    player_stats: PlayerStats = PlayerStats(
        passing=passing_stats,
        rushing=rushing_stats,
        receiving=receiving_stats,
        defensive=defensive_stats,
        kick_return=return_stats,
        kicking=kicking_stats
    )

    return player_stats
