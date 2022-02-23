from src.utils.stats_leaders import (
    _get_season_all_time_kicking_stats_leaders,
    _get_season_all_time_defensive_stats_leaders,
    _get_season_all_time_passing_stats_leaders,
    _get_season_all_time_rec_stats_leaders,
    _get_season_all_time_return_stats_leaders,
    _get_season_all_time_rush_stats_leaders,
    _get_season_specific_defensive_stats_leaders,
    _get_season_specific_kicking_stats_leaders,
    _get_season_specific_passing_stats_leaders,
    _get_season_specific_rec_stats_leaders,
    _get_season_specific_return_stats_leaders,
    _get_season_specific_rush_stats_leaders
)


def get_season_defense_stats_leaders(request, is_season_specific: bool):
    if is_season_specific:
        return _get_season_specific_defensive_stats_leaders()
    else:
        return _get_season_all_time_defensive_stats_leaders()


def get_season_kicking_stats_leaders(request, is_season_specific: bool):
    if is_season_specific:
        return _get_season_specific_kicking_stats_leaders()

    else:
        return _get_season_all_time_kicking_stats_leaders()


def get_season_passing_stats_leaders(request, is_season_specific: bool):
    if is_season_specific:
        return _get_season_specific_passing_stats_leaders()
    else:
        return _get_season_all_time_passing_stats_leaders()


def get_season_receiving_stats_leaders(request, is_season_specific: bool):
    if is_season_specific:
        return _get_season_specific_rec_stats_leaders()
    else:
        return _get_season_all_time_rec_stats_leaders()


def get_season_return_stats_leaders(request, is_season_specific: bool):
    if is_season_specific:
        return _get_season_specific_return_stats_leaders()

    else:
        return _get_season_all_time_return_stats_leaders()


def get_season_rushing_stats_leaders(request, is_season_specific: bool):
    if is_season_specific:
        return _get_season_specific_rush_stats_leaders()
    else:
        return _get_season_all_time_rush_stats_leaders()
