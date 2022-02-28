from src.blueprints.view_methods.stats import(
    get_season_defense_stats_leaders,
    get_season_kicking_stats_leaders,
    get_season_passing_stats_leaders,
    get_season_receiving_stats_leaders,
    get_season_return_stats_leaders,
    get_season_rushing_stats_leaders
)


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


def get_career_records(request):
    #TODO: Create method
    response = {}

    return response
