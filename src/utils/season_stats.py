from typing import Union
from sqlalchemy import desc
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
from src.data_models.WeekYearData import WeekYearData
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


def _get_player_season_stats(player: PlayerInfoData) -> PlayerStats:

    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    offensive_stats_data: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
        SeasonOffensiveStatsData.player_id == player.id,
        SeasonOffensiveStatsData.year == week_year.year
    ).scalar()
    defensive_stats_data: SeasonDefensiveStatsData = session.query(SeasonDefensiveStatsData).where(
        SeasonDefensiveStatsData.player_id == player.id,
        SeasonDefensiveStatsData.year == week_year.year
    ).scalar()
    return_stats_data: SeasonReturnStatsData = session.query(SeasonReturnStatsData).where(
        SeasonReturnStatsData.player_id == player.id,
        SeasonReturnStatsData.year == week_year.year
    ).scalar()
    kicking_stats_data: SeasonKickingStatsData = session.query(SeasonKickingStatsData).where(
        SeasonKickingStatsData.player_id == player.id,
        SeasonKickingStatsData.year == week_year.year
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
def _get_defensive_stats(defensive_stats: Union[SeasonDefensiveStatsData, CareerDefensiveStatsData]) -> DefensiveStats:

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


def _get_kicking_stats(kicking_stats: Union[SeasonKickingStatsData, CareerKickingStatsData]) -> KickingStats:

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


def _get_passing_stats(offensive_stats: Union[SeasonOffensiveStatsData, CareerOffensiveStatsData]) -> PassingStats:

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
        pass_rating=offensive_stats.pass_rating,
        sacked=offensive_stats.sacked
    )

    return passing_stats


def _get_receiving_stats(offensive_stats: Union[SeasonOffensiveStatsData, CareerOffensiveStatsData]) -> ReceivingStats:

    receiving_stats: ReceivingStats = ReceivingStats(
        receptions=offensive_stats.receptions,
        rec_yards=offensive_stats.rec_yards,
        rec_tds=offensive_stats.rec_tds,
        yac=offensive_stats.yac,
        drops=offensive_stats.drops,
        rec_yp_catch=offensive_stats.rec_yp_catch,
        rec_yp_game=offensive_stats.rec_yp_game,
        games_played=offensive_stats.games_played,
        year=offensive_stats.year,
        longest_rec=offensive_stats.longest_rec
    )

    return receiving_stats


def _get_return_stats(return_stats: Union[SeasonReturnStatsData, CareerReturnStatsData]) -> ReturnStats:

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


def _get_rushing_stats(offensive_stats: Union[SeasonOffensiveStatsData, CareerOffensiveStatsData]) -> RushingStats:

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
        year=offensive_stats.year,
        longest_run=offensive_stats.longest_run
    )
    
    return rushing_stats


def _get_total_stats(offensive_stats: Union[SeasonOffensiveStatsData, CareerOffensiveStatsData]) -> TotalStats:

    total_stats: TotalStats = TotalStats(
        total_yards=offensive_stats.total_yards,
        total_tds=offensive_stats.total_tds,
        total_ypg=offensive_stats.total_ypg,
        games_played=offensive_stats.games_played,
        year=offensive_stats.year
    )

    return total_stats
