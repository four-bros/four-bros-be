from typing import List
from sqlalchemy import desc
from src.constants import (
    defensive_stats_schema,
    kicking_stats_schema,
    passing_stat_schema,
    passing_stats_schema,
    receiving_stats_schema,
    return_stats_schema,
    rushing_stats_schema,
    session
)
from src.data_models.DefensiveStatsData import DefensiveStatsData
from src.data_models.KickingStatsData import KickingStatsData
from src.data_models.OffensiveStatsData import OffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.ReturnStatsData import ReturnStatsData
from src.data_models.WeekYearData import WeekYearData
from src.models.Stats import PlayerDefensiveStats, PlayerKickingStats, PlayerPassingStats, PlayerReceivingStats, PlayerReturnStats, PlayerRushingStats
from src.utils.player_stats import(
    _get_player_defensive_stats,
    _get_player_kicking_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_return_stats,
    _get_player_rushing_stats
)


#################################################
######### Get defensive stats leaders ###########
#################################################
def _get_season_specific_defensive_stats_leaders():

    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Querying PlayerInfo first and DefensiveStats second will return 
    # a set or tuple to the players variable.
    long_int_ret_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.long_int_ret)).limit(10)
    sacks_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.sacks)).limit(10)
    ff_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.forced_fumbles)).limit(10)
    safeties_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.safeties)).limit(10)
    pass_def_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.pass_def)).limit(10)
    blocked_kicks_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.blocked_kicks)).limit(10)
    tfl_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.tfl)).limit(10)
    ints_made_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.forced_fumbles)).limit(10)
    fr_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.fumbles_rec)).limit(10)
    def_td_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.def_tds)).limit(10)
    fr_yards_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.fum_rec_yards)).limit(10)
    int_ret_yards_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.int_ret_yards)).limit(10)
    total_tkls_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.total_tkls)).limit(10)
    total_sacks_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.total_sacks)).limit(10)
    
    # Convert data into models
    converted_long_int_ret: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in long_int_ret_data]
    converted_sacks: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in sacks_data]
    converted_ff: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in ff_data]
    converted_safeties: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in safeties_data]
    converted_pass_def: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in pass_def_data]
    converted_blocked_kicks: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in blocked_kicks_data]
    converted_tfl: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in tfl_data]
    converted_ints_made: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in ints_made_data]
    converted_fr: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in fr_data]
    converted_def_td: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in def_td_data]
    converted_fr_yards: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in fr_yards_data]
    converted_int_ret_yards: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in int_ret_yards_data]
    converted_total_tkls: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in total_tkls_data]
    converted_total_sacks: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in total_sacks_data]

    # Convert top ten lists into json
    long_int_ret_leaders_json = defensive_stats_schema.dump(converted_long_int_ret)
    sacks_leaders_json = defensive_stats_schema.dump(converted_sacks)
    forced_fumbles_leaders_json = defensive_stats_schema.dump(converted_ff)
    safeties_leaders_json = defensive_stats_schema.dump(converted_safeties)
    pass_def_leaders_json = defensive_stats_schema.dump(converted_pass_def)
    blocked_kicks_leaders_json = defensive_stats_schema.dump(converted_blocked_kicks)
    tfl_leaders_json = defensive_stats_schema.dump(converted_tfl)
    ints_made_leaders_json = defensive_stats_schema.dump(converted_ints_made)
    fumbles_rec_leaders_json = defensive_stats_schema.dump(converted_fr)
    def_tds_leaders_json = defensive_stats_schema.dump(converted_def_td)
    fum_rec_yards_leaders_json = defensive_stats_schema.dump(converted_fr_yards)
    int_ret_yards_leaders_json = defensive_stats_schema.dump(converted_int_ret_yards)
    total_tkls_leaders_json = defensive_stats_schema.dump(converted_total_tkls)
    total_sacks_leaders_json = defensive_stats_schema.dump(converted_total_sacks)


    response = {
        'long_int_ret_leaders': long_int_ret_leaders_json,
        'sacks_leaders': sacks_leaders_json,
        'forced_fumbles_leaders': forced_fumbles_leaders_json,
        'safeties_leaders': safeties_leaders_json,
        'pass_def_leaders': pass_def_leaders_json,
        'blocked_kicks_leaders': blocked_kicks_leaders_json,
        'tfl_leaders': tfl_leaders_json,
        'ints_made_leaders': ints_made_leaders_json,
        'fumbles_rec_leaders': fumbles_rec_leaders_json,
        'def_tds_leaders': def_tds_leaders_json,
        'fum_rec_yards_leaders': fum_rec_yards_leaders_json,
        'int_ret_yards_leaders': int_ret_yards_leaders_json,
        'total_tkls_leaders': total_tkls_leaders_json,
        'total_sack_leaders': total_sacks_leaders_json
    }

    return response


def _get_season_all_time_defensive_stats_leaders():

    # Querying PlayerInfo first and DefensiveStats second will return 
    # a set or tuple to the players variable.
    long_int_ret_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.long_int_ret)).limit(10)
    sacks_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.sacks)).limit(10)
    ff_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.forced_fumbles)).limit(10)
    safeties_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.safeties)).limit(10)
    pass_def_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.pass_def)).limit(10)
    blocked_kicks_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.blocked_kicks)).limit(10)
    tfl_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.tfl)).limit(10)
    ints_made_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.forced_fumbles)).limit(10)
    fr_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.fumbles_rec)).limit(10)
    def_td_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.def_tds)).limit(10)
    fr_yards_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.fum_rec_yards)).limit(10)
    int_ret_yards_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.int_ret_yards)).limit(10)
    total_tkls_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.total_tkls)).limit(10)
    total_sacks_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        ).order_by(desc(DefensiveStatsData.total_sacks)).limit(10)
    
    # Convert data into models
    converted_long_int_ret: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in long_int_ret_data]
    converted_sacks: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in sacks_data]
    converted_ff: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in ff_data]
    converted_safeties: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in safeties_data]
    converted_pass_def: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in pass_def_data]
    converted_blocked_kicks: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in blocked_kicks_data]
    converted_tfl: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in tfl_data]
    converted_ints_made: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in ints_made_data]
    converted_fr: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in fr_data]
    converted_def_td: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in def_td_data]
    converted_fr_yards: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in fr_yards_data]
    converted_int_ret_yards: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in int_ret_yards_data]
    converted_total_tkls: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in total_tkls_data]
    converted_total_sacks: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in total_sacks_data]

    # Convert top ten lists into json
    long_int_ret_leaders_json = defensive_stats_schema.dump(converted_long_int_ret)
    sacks_leaders_json = defensive_stats_schema.dump(converted_sacks)
    forced_fumbles_leaders_json = defensive_stats_schema.dump(converted_ff)
    safeties_leaders_json = defensive_stats_schema.dump(converted_safeties)
    pass_def_leaders_json = defensive_stats_schema.dump(converted_pass_def)
    blocked_kicks_leaders_json = defensive_stats_schema.dump(converted_blocked_kicks)
    tfl_leaders_json = defensive_stats_schema.dump(converted_tfl)
    ints_made_leaders_json = defensive_stats_schema.dump(converted_ints_made)
    fumbles_rec_leaders_json = defensive_stats_schema.dump(converted_fr)
    def_tds_leaders_json = defensive_stats_schema.dump(converted_def_td)
    fum_rec_yards_leaders_json = defensive_stats_schema.dump(converted_fr_yards)
    int_ret_yards_leaders_json = defensive_stats_schema.dump(converted_int_ret_yards)
    total_tkls_leaders_json = defensive_stats_schema.dump(converted_total_tkls)
    total_sacks_leaders_json = defensive_stats_schema.dump(converted_total_sacks)


    response = {
        'long_int_ret_leaders': long_int_ret_leaders_json,
        'sacks_leaders': sacks_leaders_json,
        'forced_fumbles_leaders': forced_fumbles_leaders_json,
        'safeties_leaders': safeties_leaders_json,
        'pass_def_leaders': pass_def_leaders_json,
        'blocked_kicks_leaders': blocked_kicks_leaders_json,
        'tfl_leaders': tfl_leaders_json,
        'ints_made_leaders': ints_made_leaders_json,
        'fumbles_rec_leaders': fumbles_rec_leaders_json,
        'def_tds_leaders': def_tds_leaders_json,
        'fum_rec_yards_leaders': fum_rec_yards_leaders_json,
        'int_ret_yards_leaders': int_ret_yards_leaders_json,
        'total_tkls_leaders': total_tkls_leaders_json,
        'total_sack_leaders': total_sacks_leaders_json
    }

    return response


#################################################
########## Get kicking stats leaders ############
#################################################
def _get_season_specific_kicking_stats_leaders():
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    fg_made_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.fg_made)).limit(10)
    fg_att_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.fg_att)).limit(10)
    fg_pct_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.fg_pct)).limit(10)
    long_fg_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.long_fg)).limit(10)
    fg_made_50_plus_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.fg_made_50_plus)).limit(10)
    fg_50_plus_pct_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.fg_50_plus_pct)).limit(10)
    long_punt_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.long_punt)).limit(10)
    num_punts_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.number_punts)).limit(10)
    total_punt_yards_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.total_punt_yards)).limit(10)
    punt_avg_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.punt_avg)).limit(10)
    net_punting_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.net_punting)).limit(10)
    inside_twenty_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
            KickingStatsData.year == week_year.year
        ).order_by(desc(KickingStatsData.inside_twenty)).limit(10)

    # Convert players to PlayerKickingStats model so they can be dumped to json
    converted_fg_made: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_made_data]
    converted_fg_att: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_att_data]
    converted_fg_pct: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_pct_data]
    converted_long_fg: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in long_fg_data]
    converted_fg_made_50_plus: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_made_50_plus_data]
    converted_fg_50_plus_pct: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_50_plus_pct_data]
    converted_long_punt: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in long_punt_data]
    converted_num_punts: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in num_punts_data]
    converted_total_punt_yards: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in total_punt_yards_data]
    converted_punt_avg: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in punt_avg_data]
    converted_net_punting: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in net_punting_data]
    converted_inside_twenty: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in inside_twenty_data]

    # Convert top ten lists into json
    fg_made_leaders_json = kicking_stats_schema.dump(converted_fg_made)
    fg_att_leaders_json = kicking_stats_schema.dump(converted_fg_att)
    fg_pct_leaders_json = kicking_stats_schema.dump(converted_fg_pct)
    long_fg_leaders_json = kicking_stats_schema.dump(converted_long_fg)
    fg_made_50_plus_leaders_json = kicking_stats_schema.dump(converted_fg_made_50_plus)
    fg_50_plus_pct_json = kicking_stats_schema.dump(converted_fg_50_plus_pct)
    long_punt_leaders_json = kicking_stats_schema.dump(converted_long_punt)
    number_punts_leaders_json = kicking_stats_schema.dump(converted_num_punts)
    total_punt_yards_json = kicking_stats_schema.dump(converted_total_punt_yards)
    punt_avg_json = kicking_stats_schema.dump(converted_punt_avg)
    net_punting_leaders_json = kicking_stats_schema.dump(converted_net_punting)
    inside_twenty_leaders_json = kicking_stats_schema.dump(converted_inside_twenty)

    response = {
        'fg_made': fg_made_leaders_json,
        'fg_att': fg_att_leaders_json,
        'fg_pct': fg_pct_leaders_json,
        'long_fg': long_fg_leaders_json,
        'fg_50_plus_made': fg_made_50_plus_leaders_json,
        'fg_50_plus_pct': fg_50_plus_pct_json,
        'long_punt': long_punt_leaders_json,
        'total_punt_yards': total_punt_yards_json,
        'number_punts': number_punts_leaders_json,
        'punt_avg': punt_avg_json,
        'net_punting': net_punting_leaders_json,
        'inside_twenty': inside_twenty_leaders_json,
    }

    return response


def _get_season_all_time_kicking_stats_leaders():
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    fg_made_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.fg_made)).limit(10)
    fg_att_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.fg_att)).limit(10)
    fg_pct_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.fg_pct)).limit(10)
    long_fg_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.long_fg)).limit(10)
    fg_made_50_plus_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.fg_made_50_plus)).limit(10)
    fg_50_plus_pct_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.fg_50_plus_pct)).limit(10)
    long_punt_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.long_punt)).limit(10)
    num_punts_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.number_punts)).limit(10)
    total_punt_yards_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.total_punt_yards)).limit(10)
    punt_avg_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.punt_avg)).limit(10)
    net_punting_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.net_punting)).limit(10)
    inside_twenty_data = session.query(PlayerInfoData, KickingStatsData).filter(
            KickingStatsData.player_id == PlayerInfoData.id,
        ).order_by(desc(KickingStatsData.inside_twenty)).limit(10)

    # Convert players to PlayerKickingStats model so they can be dumped to json
    converted_fg_made: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_made_data]
    converted_fg_att: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_att_data]
    converted_fg_pct: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_pct_data]
    converted_long_fg: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in long_fg_data]
    converted_fg_made_50_plus: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_made_50_plus_data]
    converted_fg_50_plus_pct: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in fg_50_plus_pct_data]
    converted_long_punt: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in long_punt_data]
    converted_num_punts: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in num_punts_data]
    converted_total_punt_yards: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in total_punt_yards_data]
    converted_punt_avg: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in punt_avg_data]
    converted_net_punting: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in net_punting_data]
    converted_inside_twenty: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in inside_twenty_data]

    # Convert top ten lists into json
    fg_made_leaders_json = kicking_stats_schema.dump(converted_fg_made)
    fg_att_leaders_json = kicking_stats_schema.dump(converted_fg_att)
    fg_pct_leaders_json = kicking_stats_schema.dump(converted_fg_pct)
    long_fg_leaders_json = kicking_stats_schema.dump(converted_long_fg)
    fg_made_50_plus_leaders_json = kicking_stats_schema.dump(converted_fg_made_50_plus)
    fg_50_plus_pct_json = kicking_stats_schema.dump(converted_fg_50_plus_pct)
    long_punt_leaders_json = kicking_stats_schema.dump(converted_long_punt)
    number_punts_leaders_json = kicking_stats_schema.dump(converted_num_punts)
    total_punt_yards_json = kicking_stats_schema.dump(converted_total_punt_yards)
    punt_avg_json = kicking_stats_schema.dump(converted_punt_avg)
    net_punting_leaders_json = kicking_stats_schema.dump(converted_net_punting)
    inside_twenty_leaders_json = kicking_stats_schema.dump(converted_inside_twenty)

    response = {
        'fg_made': fg_made_leaders_json,
        'fg_att': fg_att_leaders_json,
        'fg_pct': fg_pct_leaders_json,
        'long_fg': long_fg_leaders_json,
        'fg_50_plus_made': fg_made_50_plus_leaders_json,
        'fg_50_plus_pct': fg_50_plus_pct_json,
        'long_punt': long_punt_leaders_json,
        'total_punt_yards': total_punt_yards_json,
        'number_punts': number_punts_leaders_json,
        'punt_avg': punt_avg_json,
        'net_punting': net_punting_leaders_json,
        'inside_twenty': inside_twenty_leaders_json,
    }

    return response


#################################################
########## Get passing stats leaders ############
#################################################   
def _get_season_specific_passing_stats_leaders():
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    completions_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.completions)).limit(10)
    pass_att_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.pass_att)).limit(10)
    long_pass_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.longest_pass)).limit(10)
    pass_yards_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.pass_yards)).limit(10)
    pass_tds_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.pass_tds)).limit(10)
    ints_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.ints)).limit(10)
    pass_yp_attempt_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.pass_yp_attempt)).limit(10)
    pass_yp_game_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.pass_yp_game)).limit(10)

    # Convert players to PlayerPassingStats model so they can be sorted
    converted_completions: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in completions_data]
    converted_pass_att: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_att_data]
    converted_long_pass: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in long_pass_data]
    converted_pass_yards: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_yards_data]
    converted_pass_tds: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_tds_data]
    converted_ints: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in ints_data]
    converted_pass_yp_attempt: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_yp_attempt_data]
    converted_pass_yp_game: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_yp_game_data]

    # Convert top ten lists into json
    completions_leaders_json = passing_stats_schema.dump(converted_completions)
    pass_att_leaders_jason = passing_stat_schema.dump(converted_pass_att)
    longest_pass_leaders_jason = passing_stat_schema.dump(converted_long_pass)
    pass_yard_leaders_json = passing_stats_schema.dump(converted_pass_yards)
    pass_td_leaders_json = passing_stats_schema.dump(converted_pass_tds)
    int_leaders_json = passing_stats_schema.dump(converted_ints)
    pass_yp_attempt_leaders_json = passing_stats_schema.dump(converted_pass_yp_attempt)
    pass_yp_game_leaders_json = passing_stats_schema.dump(converted_pass_yp_game)

    response = {
        'completions': completions_leaders_json,
        'pass_att': pass_att_leaders_jason,
        'longest_pass': longest_pass_leaders_jason,
        'pass_yards': pass_yard_leaders_json,
        'pass_tds': pass_td_leaders_json,
        'interceptions': int_leaders_json,
        'pass_yp_attempt': pass_yp_attempt_leaders_json,
        'pass_yp_game': pass_yp_game_leaders_json
    }

    return response


def _get_season_all_time_passing_stats_leaders():
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    completions_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.completions)).limit(10)
    pass_att_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.pass_att)).limit(10)
    long_pass_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.longest_pass)).limit(10)
    pass_yards_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.pass_yards)).limit(10)
    pass_tds_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.pass_tds)).limit(10)
    ints_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.ints)).limit(10)
    pass_yp_attempt_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.pass_yp_attempt)).limit(10)
    pass_yp_game_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.pass_yp_game)).limit(10)

    # Convert players to PlayerPassingStats model so they can be sorted
    converted_completions: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in completions_data]
    converted_pass_att: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_att_data]
    converted_long_pass: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in long_pass_data]
    converted_pass_yards: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_yards_data]
    converted_pass_tds: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_tds_data]
    converted_ints: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in ints_data]
    converted_pass_yp_attempt: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_yp_attempt_data]
    converted_pass_yp_game: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in pass_yp_game_data]

    # Convert top ten lists into json
    completions_leaders_json = passing_stats_schema.dump(converted_completions)
    pass_att_leaders_jason = passing_stat_schema.dump(converted_pass_att)
    longest_pass_leaders_jason = passing_stat_schema.dump(converted_long_pass)
    pass_yard_leaders_json = passing_stats_schema.dump(converted_pass_yards)
    pass_td_leaders_json = passing_stats_schema.dump(converted_pass_tds)
    int_leaders_json = passing_stats_schema.dump(converted_ints)
    pass_yp_attempt_leaders_json = passing_stats_schema.dump(converted_pass_yp_attempt)
    pass_yp_game_leaders_json = passing_stats_schema.dump(converted_pass_yp_game)

    response = {
        'completions': completions_leaders_json,
        'pass_att': pass_att_leaders_jason,
        'longest_pass': longest_pass_leaders_jason,
        'pass_yards': pass_yard_leaders_json,
        'pass_tds': pass_td_leaders_json,
        'interceptions': int_leaders_json,
        'pass_yp_attempt': pass_yp_attempt_leaders_json,
        'pass_yp_game': pass_yp_game_leaders_json
    }

    return response


###################################################
########## Get receiving stats leaders ############
###################################################
def _get_season_specific_rec_stats_leaders():
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    receptions_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.receptions)).limit(10)
    rec_yards_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.rec_yards)).limit(10)
    rec_tds_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.rec_tds)).limit(10)
    yac_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.yac)).limit(10)
    drops_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.drops)).limit(10)
    rec_yp_catch_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.rec_yp_catch)).limit(10)
    rec_yp_game_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year
            ).order_by(desc(OffensiveStatsData.rec_yp_game)).limit(10)

    # Convert players to PlayerReceivingStats model so they can be sorted
    converted_receptions: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in receptions_data]
    converted_rec_yards: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_yards_data]
    converted_rec_tds: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_tds_data]
    converted_yac: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in yac_data]
    converted_drops: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in drops_data]
    converted_rec_yp_catch: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_yp_catch_data]
    converted_rec_yp_game: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_yp_game_data]

    # Convert top ten lists to json
    reception_leaders_json = receiving_stats_schema.dump(converted_receptions)
    rec_yards_leaders_json = receiving_stats_schema.dump(converted_rec_yards)
    rec_tds_leaders_json = receiving_stats_schema.dump(converted_rec_tds)
    yac_leaders_json = receiving_stats_schema.dump(converted_yac)
    drops_leaders_json = receiving_stats_schema.dump(converted_drops)
    rec_yp_catch_leaders_json = receiving_stats_schema.dump(converted_rec_yp_catch)
    rec_yp_game_leaders_json = receiving_stats_schema.dump(converted_rec_yp_game)

    response = {
        'receptions': reception_leaders_json,
        'rec_yards': rec_yards_leaders_json,
        'rec_tds': rec_tds_leaders_json,
        'yac': yac_leaders_json,
        'drops': drops_leaders_json,
        'rec_yp_catch': rec_yp_catch_leaders_json,
        'rec_yp_game': rec_yp_game_leaders_json
    }

    return response


def _get_season_all_time_rec_stats_leaders():
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    receptions_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.receptions)).limit(10)
    rec_yards_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rec_yards)).limit(10)
    rec_tds_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rec_tds)).limit(10)
    yac_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.yac)).limit(10)
    drops_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.drops)).limit(10)
    rec_yp_catch_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rec_yp_catch)).limit(10)
    rec_yp_game_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rec_yp_game)).limit(10)

    # Convert players to PlayerReceivingStats model so they can be sorted
    converted_receptions: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in receptions_data]
    converted_rec_yards: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_yards_data]
    converted_rec_tds: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_tds_data]
    converted_yac: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in yac_data]
    converted_drops: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in drops_data]
    converted_rec_yp_catch: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_yp_catch_data]
    converted_rec_yp_game: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in rec_yp_game_data]

    # Convert top ten lists to json
    reception_leaders_json = receiving_stats_schema.dump(converted_receptions)
    rec_yards_leaders_json = receiving_stats_schema.dump(converted_rec_yards)
    rec_tds_leaders_json = receiving_stats_schema.dump(converted_rec_tds)
    yac_leaders_json = receiving_stats_schema.dump(converted_yac)
    drops_leaders_json = receiving_stats_schema.dump(converted_drops)
    rec_yp_catch_leaders_json = receiving_stats_schema.dump(converted_rec_yp_catch)
    rec_yp_game_leaders_json = receiving_stats_schema.dump(converted_rec_yp_game)

    response = {
        'receptions': reception_leaders_json,
        'rec_yards': rec_yards_leaders_json,
        'rec_tds': rec_tds_leaders_json,
        'yac': yac_leaders_json,
        'drops': drops_leaders_json,
        'rec_yp_catch': rec_yp_catch_leaders_json,
        'rec_yp_game': rec_yp_game_leaders_json
    }

    return response


###################################################
########### Get return stats leaders ##############
###################################################
def _get_season_specific_return_stats_leaders():
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    kick_returns_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.kick_returns)).limit(10)
    long_kr_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.long_kr)).limit(10)
    punt_returns_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.punt_returns)).limit(10)
    long_pr_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.long_pr)).limit(10)
    kr_tds_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.kr_tds)).limit(10)
    pr_tds_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.pr_tds)).limit(10)
    kr_yards_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.kr_yds)).limit(10)
    pr_yards_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.pr_yds)).limit(10)
    kr_avg_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.kr_avg)).limit(10)
    pr_avg_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ReturnStatsData.year == week_year.year
            ).order_by(desc(ReturnStatsData.pr_avg)).limit(10)

    # Convert players to PlayerKickingStats model so they can be sorted
    converted_kick_returns: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kick_returns_data]
    converted_long_kr: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in long_kr_data]
    converted_punt_returns: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in punt_returns_data]
    converted_long_pr: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in long_pr_data]
    converted_kr_tds: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kr_tds_data]
    converted_pr_tds: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in pr_tds_data]
    converted_kr_yards: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kr_yards_data]
    converted_pr_yards: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in pr_yards_data]
    converted_kr_avg_data: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kr_avg_data]
    converted_pr_avg_data: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in pr_avg_data]

    # Convert top ten lists to json
    kick_return_leaders_json = return_stats_schema.dump(converted_kick_returns)
    long_kr_leaders_json = return_stats_schema.dump(converted_long_kr)
    punt_returns_leaders_json = return_stats_schema.dump(converted_punt_returns)
    long_pr_leaders_json = return_stats_schema.dump(converted_long_pr)
    kr_tds_leaders_json = return_stats_schema.dump(converted_kr_tds)
    pr_tds_leaders_json = return_stats_schema.dump(converted_pr_tds)
    kr_yds_leaders_json = return_stats_schema.dump(converted_kr_yards)
    pr_yds_leaders_json = return_stats_schema.dump(converted_pr_yards)
    kr_avg_leaders_json = return_stats_schema.dump(converted_kr_avg_data)
    pr_avg_leaders_json = return_stats_schema.dump(converted_pr_avg_data)

    response = {
        'kick_returns': kick_return_leaders_json,
        'long_kr': long_kr_leaders_json,
        'punt_returns': punt_returns_leaders_json,
        'long_pr': long_pr_leaders_json,
        'kr_tds': kr_tds_leaders_json,
        'pr_tds': pr_tds_leaders_json,
        'kr_yards': kr_yds_leaders_json,
        'pr_yards': pr_yds_leaders_json,
        'kr_avg': kr_avg_leaders_json,
        'pr_avg': pr_avg_leaders_json
    }

    return response


def _get_season_all_time_return_stats_leaders():
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    kick_returns_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.kick_returns)).limit(10)
    long_kr_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.long_kr)).limit(10)
    punt_returns_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.punt_returns)).limit(10)
    long_pr_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.long_pr)).limit(10)
    kr_tds_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.kr_tds)).limit(10)
    pr_tds_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.pr_tds)).limit(10)
    kr_yards_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.kr_yds)).limit(10)
    pr_yards_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.pr_yds)).limit(10)
    kr_avg_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.kr_avg)).limit(10)
    pr_avg_data = session.query(PlayerInfoData, ReturnStatsData).filter(
            PlayerInfoData.id == ReturnStatsData.player_id,
            ).order_by(desc(ReturnStatsData.pr_avg)).limit(10)

    # Convert players to PlayerKickingStats model so they can be sorted
    converted_kick_returns: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kick_returns_data]
    converted_long_kr: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in long_kr_data]
    converted_punt_returns: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in punt_returns_data]
    converted_long_pr: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in long_pr_data]
    converted_kr_tds: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kr_tds_data]
    converted_pr_tds: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in pr_tds_data]
    converted_kr_yards: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kr_yards_data]
    converted_pr_yards: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in pr_yards_data]
    converted_kr_avg_data: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kr_avg_data]
    converted_pr_avg_data: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in pr_avg_data]

    # Convert top ten lists to json
    kick_return_leaders_json = return_stats_schema.dump(converted_kick_returns)
    long_kr_leaders_json = return_stats_schema.dump(converted_long_kr)
    punt_returns_leaders_json = return_stats_schema.dump(converted_punt_returns)
    long_pr_leaders_json = return_stats_schema.dump(converted_long_pr)
    kr_tds_leaders_json = return_stats_schema.dump(converted_kr_tds)
    pr_tds_leaders_json = return_stats_schema.dump(converted_pr_tds)
    kr_yds_leaders_json = return_stats_schema.dump(converted_kr_yards)
    pr_yds_leaders_json = return_stats_schema.dump(converted_pr_yards)
    kr_avg_leaders_json = return_stats_schema.dump(converted_kr_avg_data)
    pr_avg_leaders_json = return_stats_schema.dump(converted_pr_avg_data)

    response = {
        'kick_returns': kick_return_leaders_json,
        'long_kr': long_kr_leaders_json,
        'punt_returns': punt_returns_leaders_json,
        'long_pr': long_pr_leaders_json,
        'kr_tds': kr_tds_leaders_json,
        'pr_tds': pr_tds_leaders_json,
        'kr_yards': kr_yds_leaders_json,
        'pr_yards': pr_yds_leaders_json,
        'kr_avg': kr_avg_leaders_json,
        'pr_avg': pr_avg_leaders_json
    }

    return response


###################################################
########### Get rushing stats leaders #############
###################################################
def _get_season_specific_rush_stats_leaders():
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    rush_att_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.rush_att)).limit(10)
    rush_yards_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.rush_yards)).limit(10)
    ya_contact_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.ya_contact)).limit(10)
    broke_tkls_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.broke_tkls)).limit(10)
    fumbles_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.fumbles)).limit(10)
    twenty_plus_yd_runs_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.twenty_plus_yd_runs)).limit(10)
    rush_yp_carry_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.rush_yp_carry)).limit(10)
    rush_yp_game_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            ).order_by(desc(OffensiveStatsData.rush_yp_game)).limit(10)

    # Convert players to PlayerRushingStats model so they can be sorted
    converted_rush_att: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_att_data]
    converted_rush_yards: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_yards_data]
    converted_ya_contact: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in ya_contact_data]
    converted_broke_tkls: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in broke_tkls_data]
    converted_fumbles: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in fumbles_data]
    converted_twenty_plus_yd_runs: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in twenty_plus_yd_runs_data]
    converted_rush_yp_carry: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_yp_carry_data]
    converted_rush_yp_game: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_yp_game_data]

    # Convert top ten lists to json
    rush_att_leaders_json = rushing_stats_schema.dump(converted_rush_att)
    rush_yards_leaders_json = rushing_stats_schema.dump(converted_rush_yards)
    ya_contact_leaders_json = rushing_stats_schema.dump(converted_ya_contact)
    broke_tkls_leaders_json = rushing_stats_schema.dump(converted_broke_tkls)
    fumbles_leaders_json = rushing_stats_schema.dump(converted_fumbles)
    twenty_plus_yd_runs_leaders_json = rushing_stats_schema.dump(converted_twenty_plus_yd_runs)
    rush_yp_carry_leaders_json = rushing_stats_schema.dump(converted_rush_yp_carry)
    rush_yp_game_leaders_json = rushing_stats_schema.dump(converted_rush_yp_game)

    response = {
        'rush_att': rush_att_leaders_json,
        'rush_yards': rush_yards_leaders_json,
        'ya_contact': ya_contact_leaders_json,
        'broken_tackles': broke_tkls_leaders_json,
        'fumbles': fumbles_leaders_json,
        'twenty_plus_runs': twenty_plus_yd_runs_leaders_json,
        'rush_yp_carry': rush_yp_carry_leaders_json,
        'rush_yp_game': rush_yp_game_leaders_json
    }

    return response


def _get_season_all_time_rush_stats_leaders():
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    rush_att_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rush_att)).limit(10)
    rush_yards_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rush_yards)).limit(10)
    ya_contact_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.ya_contact)).limit(10)
    broke_tkls_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.broke_tkls)).limit(10)
    fumbles_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.fumbles)).limit(10)
    twenty_plus_yd_runs_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.twenty_plus_yd_runs)).limit(10)
    rush_yp_carry_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rush_yp_carry)).limit(10)
    rush_yp_game_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.id == OffensiveStatsData.player_id,
            ).order_by(desc(OffensiveStatsData.rush_yp_game)).limit(10)

    # Convert players to PlayerRushingStats model so they can be sorted
    converted_rush_att: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_att_data]
    converted_rush_yards: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_yards_data]
    converted_ya_contact: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in ya_contact_data]
    converted_broke_tkls: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in broke_tkls_data]
    converted_fumbles: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in fumbles_data]
    converted_twenty_plus_yd_runs: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in twenty_plus_yd_runs_data]
    converted_rush_yp_carry: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_yp_carry_data]
    converted_rush_yp_game: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rush_yp_game_data]

    # Convert top ten lists to json
    rush_att_leaders_json = rushing_stats_schema.dump(converted_rush_att)
    rush_yards_leaders_json = rushing_stats_schema.dump(converted_rush_yards)
    ya_contact_leaders_json = rushing_stats_schema.dump(converted_ya_contact)
    broke_tkls_leaders_json = rushing_stats_schema.dump(converted_broke_tkls)
    fumbles_leaders_json = rushing_stats_schema.dump(converted_fumbles)
    twenty_plus_yd_runs_leaders_json = rushing_stats_schema.dump(converted_twenty_plus_yd_runs)
    rush_yp_carry_leaders_json = rushing_stats_schema.dump(converted_rush_yp_carry)
    rush_yp_game_leaders_json = rushing_stats_schema.dump(converted_rush_yp_game)

    response = {
        'rush_att': rush_att_leaders_json,
        'rush_yards': rush_yards_leaders_json,
        'ya_contact': ya_contact_leaders_json,
        'broken_tackles': broke_tkls_leaders_json,
        'fumbles': fumbles_leaders_json,
        'twenty_plus_runs': twenty_plus_yd_runs_leaders_json,
        'rush_yp_carry': rush_yp_carry_leaders_json,
        'rush_yp_game': rush_yp_game_leaders_json
    }

    return response
