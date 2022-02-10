from typing import List

from src.constants import session
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.responses.Stats import PassingStatsSchema
from src.responses.Players import PlayerSchema


passing_stat_schema = PassingStatsSchema()
passing_stats_schema = PassingStatsSchema(many=True)
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


def get_season_passing_stats(request):

    players = session.query(OffensiveStats, PlayerInfo)\
        .filter(OffensiveStats.player_id == PlayerInfo.id)\
        .all()
    
    pass_yards_leaders = sorted(players, key=lambda p: p.pass_yards)

    players_json = []
    
    # for player in players:
    #     players_json.append({
    #         **passing_stat_schema.dump(player[0]),
    #         **passing_stat_schema.dump(player[1])
    #     })

    for player in pass_yards_leaders:
        players_json.append({
            **passing_stat_schema.dump(player[0]),
            **passing_stat_schema.dump(player[1])
        })
    
    response = {
        'players': players_json
    }
    
    return response


def get_season_passing_leaders_stats(request):

    players: List[(PlayerInfo, OffensiveStats)] = session.query(PlayerInfo, OffensiveStats)\
        .filter(OffensiveStats.player_id == PlayerInfo.id)\
        .all()

    player_objects = []

    for player in players:
        player_objects.append(
            **passing_stat_schema.dump(player[0]),
            **passing_stat_schema.dump(player[1])
        )
    
    passing_yards_leaders = sorted(player_objects, key=lambda p: p['pass_yards'])[:10]

    response = {
        'pass_yards': passing_yards_leaders
    }

    return response
