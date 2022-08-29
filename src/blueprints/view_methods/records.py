from src.blueprints.view_methods.stats import(
    get_player_season_stats_leaders
)
from src.utils.caches import (
    _get_player_career_records_cache,
    _get_player_game_records_cache,
    _get_player_season_records_cache,
    _get_team_game_records_cache,
    _get_team_season_records_cache
)
from src.utils.career_stats_leaders import (
    _get_career_defensive_stats_leaders,
    _get_career_kicking_stats_leaders,
    _get_career_kick_return_stats_leaders,
    _get_career_passing_stats_leaders,
    _get_career_punting_stats_leaders,
    _get_career_punt_return_stats_leaders,
    _get_career_rec_stats_leaders,
    _get_career_rush_stats_leaders,
    _get_career_total_stats_leaders
)
from src.utils.game_stats_leaders import (
    _get_game_defensive_stats_leaders,
    _get_game_kick_return_stats_leaders,
    _get_game_kicking_stats_leaders,
    _get_game_passing_stats_leaders,
    _get_game_punt_return_stats_leaders,
    _get_game_punting_stats_leaders,
    _get_game_rec_stats_leaders,
    _get_game_rush_stats_leaders,
    _get_game_total_stats_leaders
)
from src.utils.team_stats_leaders import (
    _get_team_season_stats_leaders,
    _get_team_game_records
)


def get_career_records(request):

    response = {
        'defense': _get_career_defensive_stats_leaders(),
        'kicking': _get_career_kicking_stats_leaders(),
        'kick_return': _get_career_kick_return_stats_leaders(),
        'passing': _get_career_passing_stats_leaders(),
        'punting': _get_career_punting_stats_leaders(),
        'punt_return': _get_career_punt_return_stats_leaders(),
        'receiving': _get_career_rec_stats_leaders(),
        'rushing': _get_career_rush_stats_leaders(),
        'total': _get_career_total_stats_leaders()
    }

    return response


def get_game_records(request):

    response = {
        'defense': _get_game_defensive_stats_leaders(),
        'kick_return': _get_game_kick_return_stats_leaders(),
        'kicking': _get_game_kicking_stats_leaders(),
        'passing': _get_game_passing_stats_leaders(),
        'punt_return': _get_game_punt_return_stats_leaders(),
        'punting': _get_game_punting_stats_leaders(),
        'receiving': _get_game_rec_stats_leaders(),
        'rushing': _get_game_rush_stats_leaders(),
        'total': _get_game_total_stats_leaders()
    }

    return response


def get_season_records(is_season_specific: bool):
    response = get_player_season_stats_leaders(is_season_specific=False)
    return response


def get_team_game_records():
    return _get_team_game_records()


def get_team_season_records():
    return _get_team_season_stats_leaders(is_season_specific=False)


# cache endpoints
def get_player_career_records_cache():
    return _get_player_career_records_cache()


def get_player_game_records_cache():
    return _get_player_game_records_cache()


def get_player_season_records_cache():
    return _get_player_season_records_cache()


def get_team_game_records_cache():
    return _get_team_game_records_cache()


def get_team_season_records_cache():
    return _get_team_season_records_cache()
