from src.blueprints.view_methods.stats import(
    get_season_defense_stats_leaders,
    get_season_kicking_stats_leaders,
    get_season_passing_stats_leaders,
    get_season_receiving_stats_leaders,
    get_season_return_stats_leaders,
    get_season_rushing_stats_leaders
)
from src.utils.career_stats_leaders import (
    _get_career_defensive_stats_leaders,
    _get_career_kicking_stats_leaders,
    _get_career_passing_stats_leaders,
    _get_career_rec_stats_leaders,
    _get_career_return_stats_leaders,
    _get_career_rush_stats_leaders
)
from src.utils.game_stats_leaders import (
    _get_game_defensive_stats_leaders,
    _get_game_kicking_stats_leaders,
    _get_game_passing_stats_leaders,
    _get_game_rec_stats_leaders,
    _get_game_return_stats_leaders,
    _get_game_rush_stats_leaders
)


def get_career_records(request):

    response = {
        'defense': _get_career_defensive_stats_leaders(),
        'kicking': _get_career_kicking_stats_leaders(),
        'passing': _get_career_passing_stats_leaders(),
        'receiving': _get_career_rec_stats_leaders(),
        'return': _get_career_return_stats_leaders(),
        'rushing': _get_career_rush_stats_leaders()
    }

    return response


def get_game_records(request):

    response = {
        'defense': _get_game_defensive_stats_leaders(),
        'kicking': _get_game_kicking_stats_leaders(),
        'passing': _get_game_passing_stats_leaders(),
        'receiving': _get_game_rec_stats_leaders(),
        'return': _get_game_return_stats_leaders(),
        'rushing': _get_game_rush_stats_leaders()
    }

    return response


def get_season_records(request):

    response = {
        'defense': get_season_defense_stats_leaders(request, is_season_specific=False),
        'kicking': get_season_kicking_stats_leaders(request, is_season_specific=False),
        'passing': get_season_passing_stats_leaders(request, is_season_specific=False),
        'receiving': get_season_receiving_stats_leaders(request, is_season_specific=False),
        'return': get_season_return_stats_leaders(request, is_season_specific=False),
        'rushing': get_season_rushing_stats_leaders(request, is_season_specific=False)
    }

    return response



