from src.utils.season_stats_leaders import (
    _get_season_defensive_stats_leaders,
    _get_season_kick_return_stats_leaders,
    _get_season_kicking_stats_leaders,
    _get_season_passing_stats_leaders,
    _get_season_punt_return_stats_leaders,
    _get_season_punting_stats_leaders,
    _get_season_rec_stats_leaders,
    _get_season_rushing_stats_leaders,
    _get_season_total_stats_leaders
)


def get_season_defense_stats_leaders(request, is_season_specific: bool):
    return _get_season_defensive_stats_leaders(is_season_specific=is_season_specific)


def get_season_kicking_stats_leaders(request, is_season_specific: bool):
    return _get_season_kicking_stats_leaders(is_season_specific=is_season_specific)


def get_season_passing_stats_leaders(request, is_season_specific: bool):
    return _get_season_passing_stats_leaders(is_season_specific=is_season_specific)


def get_season_receiving_stats_leaders(request, is_season_specific: bool):
    return _get_season_rec_stats_leaders(is_season_specific=is_season_specific)


def get_season_rushing_stats_leaders(request, is_season_specific: bool):
    return _get_season_rushing_stats_leaders(is_season_specific=is_season_specific)


def get_season_stats_leaders(request, is_season_specific: bool):

        response = {
            'defense': _get_season_defensive_stats_leaders(is_season_specific=is_season_specific),
            'kick_return': _get_season_kick_return_stats_leaders(is_season_specific=is_season_specific),
            'kicking': _get_season_kicking_stats_leaders(is_season_specific=is_season_specific),
            'passing': _get_season_passing_stats_leaders(is_season_specific=is_season_specific),
            'punt_return': _get_season_punt_return_stats_leaders(is_season_specific=is_season_specific),
            'punting': _get_season_punting_stats_leaders(is_season_specific=is_season_specific),
            'receiving': _get_season_rec_stats_leaders(is_season_specific=is_season_specific),
            'rushing': _get_season_rushing_stats_leaders(is_season_specific=is_season_specific),
            'total': _get_season_total_stats_leaders(is_season_specific=is_season_specific)
        }

        return response
