from typing import Union
from sqlalchemy import desc
from src.constants import session
from src.data_models.CareerDefensiveStatsData import CareerDefensiveStatsData
from src.data_models.CareerKickingStatsData import CareerKickingStatsData
from src.data_models.CareerOffensiveStatsData import CareerOffensiveStatsData
from src.data_models.CareerReturnStatsData import CareerReturnStatsData
from src.data_models.GameDefensiveStatsData import GameDefensiveStatsData
from src.data_models.GameKickingStatsData import GameKickingStatsData
from src.data_models.GameOffensiveStatsData import GameOffensiveStatsData
from src.data_models.GameReturnStatsData import GameReturnStatsData
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
    KickReturnStats,
    PassingStats,
    PuntingStats,
    PuntReturnStats,
    ReceivingStats,
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
    kicking_stats: KickingStats = None
    kick_return_stats: KickReturnStats = None
    punting_stats: PuntingStats = None
    punt_return_stats: PuntReturnStats = None
    total_stats: TotalStats = None

    if offensive_stats_data:
        passing_stats = _get_passing_stats(offensive_stats_data)
        receiving_stats = _get_receiving_stats(offensive_stats_data)
        rushing_stats = _get_rushing_stats(offensive_stats_data)
        total_stats = _get_total_stats(offensive_stats_data)
    if defensive_stats_data:
        defensive_stats = _get_defensive_stats(defensive_stats_data)
    if return_stats_data:
        kick_return_stats = _get_kick_return_stats(return_stats_data)
        punt_return_stats = _get_punt_return_stats(return_stats_data)
    if kicking_stats_data:
        kicking_stats = _get_kicking_stats(kicking_stats_data)
        punting_stats = _get_punting_stats(kicking_stats_data)
    
    player_stats: PlayerStats = PlayerStats(
        passing=passing_stats,
        rushing=rushing_stats,
        receiving=receiving_stats,
        defensive=defensive_stats,
        kicking=kicking_stats,
        kick_return=kick_return_stats,
        punting=punting_stats,
        punt_return=punt_return_stats,
        total=total_stats
    )

    return player_stats


################################################
######### Get player defensive stats ###########
################################################
def _get_defensive_stats(
    defensive_stats: Union[CareerDefensiveStatsData, GameDefensiveStatsData, SeasonDefensiveStatsData]
    ) -> DefensiveStats:

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


################################################
####### Get player special teams stats #########
################################################
def _get_kicking_stats(
    kicking_stats: Union[CareerKickingStatsData, GameKickingStatsData, SeasonKickingStatsData]
    ) -> KickingStats:

    kicking_stats_all: KickingStats = KickingStats(
        fg_made_17_29=kicking_stats.fg_made_17_29,
        fg_att_17_29=kicking_stats.fg_att_17_29,
        long_fg=kicking_stats.long_fg,
        ko_touchbacks=kicking_stats.ko_touchbacks,
        xp_att=kicking_stats.xp_att,
        year=kicking_stats.year,
        fg_att=kicking_stats.fg_att,
        xp_blocked=kicking_stats.xp_blocked,
        fg_blocked=kicking_stats.fg_blocked,
        fg_att_40_49=kicking_stats.fg_att_40_49,
        fg_made_40_49=kicking_stats.fg_made_40_49,
        fg_att_30_39=kicking_stats.fg_att_30_39,
        fg_made_30_39=kicking_stats.fg_made_30_39,
        fg_att_50_plus=kicking_stats.fg_att_50_plus,
        fg_made_50_plus=kicking_stats.fg_made_50_plus,
        games_played=kicking_stats.games_played,
        kickoffs=kicking_stats.kickoffs,
        xp_made=kicking_stats.xp_made,
        fg_made=kicking_stats.fg_made,
        fg_pct=kicking_stats.fg_pct,
        xp_pct=kicking_stats.xp_pct,
        fg_50_plus_pct=kicking_stats.fg_50_plus_pct
    )

    return kicking_stats_all


def _get_kick_return_stats(
    return_stats: Union[CareerReturnStatsData, GameReturnStatsData, SeasonReturnStatsData]
    ) -> KickReturnStats:

    kick_return_stats: KickReturnStats = KickReturnStats(
        kick_returns=return_stats.kick_returns,
        year=return_stats.year,
        long_kr=return_stats.long_kr,
        games_played=return_stats.games_played,
        kr_tds=return_stats.kr_tds,
        kr_yds=return_stats.kr_yds,
        kr_avg=return_stats.kr_avg
    )

    return kick_return_stats


def _get_punting_stats(
    punting_stats: Union[CareerKickingStatsData, GameKickingStatsData, SeasonKickingStatsData]
    ) -> PuntingStats:

    punting_stats: PuntingStats = PuntingStats(
        long_punt=punting_stats.long_punt,
        year=punting_stats.year,
        punts_blocked=punting_stats.punts_blocked,
        total_punt_yards=punting_stats.total_punt_yards,
        punt_touchbacks=punting_stats.punt_touchbacks,
        games_played=punting_stats.games_played,
        net_punting=punting_stats.net_punting,
        number_punts=punting_stats.number_punts,
        inside_twenty=punting_stats.inside_twenty,
        punt_avg=punting_stats.punt_avg,
        net_avg=punting_stats.net_avg
    )

    return punting_stats


def _get_punt_return_stats(
    return_stats: Union[CareerReturnStatsData, GameReturnStatsData, SeasonReturnStatsData]
    ) -> PuntReturnStats:

    punt_return_stats: PuntReturnStats = PuntReturnStats(
        year=return_stats.year,
        punt_returns=return_stats.punt_returns,
        long_pr=return_stats.long_pr,
        games_played=return_stats.games_played,
        pr_tds=return_stats.pr_tds,
        pr_yds=return_stats.pr_yds,
        pr_avg=return_stats.pr_avg
    )

    return punt_return_stats


################################################
######### Get player offensive stats ###########
################################################
def _get_passing_stats(
    offensive_stats: Union[CareerOffensiveStatsData, GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> PassingStats:

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
        sacked=offensive_stats.sacked,
        comp_pct=offensive_stats.comp_pct
    )

    return passing_stats


def _get_receiving_stats(
    offensive_stats: Union[CareerOffensiveStatsData, GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> ReceivingStats:

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


def _get_rushing_stats(
    offensive_stats: Union[CareerOffensiveStatsData, GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> RushingStats:

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


def _get_total_stats(
    offensive_stats: Union[CareerOffensiveStatsData, GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> TotalStats:

    total_stats: TotalStats = TotalStats(
        total_yards=offensive_stats.total_yards,
        total_tds=offensive_stats.total_tds,
        total_ypg=offensive_stats.total_ypg,
        games_played=offensive_stats.games_played,
        year=offensive_stats.year,
        turnovers=offensive_stats.turnovers
    )

    return total_stats
