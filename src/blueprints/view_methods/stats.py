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
    
    players: List[PassingStatsSchema] = session.query(PlayerInfo, OffensiveStats)\
        .select_from(PlayerInfo, OffensiveStats)\
        .join(OffensiveStats, OffensiveStats.player_id == PlayerInfo.id)\
        .all()
    
    players_json = []
    
    for player in players:
        players_json.append({
            **passing_stat_schema.dump(player[0]),
            **passing_stat_schema.dump(player[1])
        })
    
    response = {
        'players': players_json
    }
    
    return response
