from typing import List

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
from src.helpers import(
    _get_player_defensive_stats,
    _get_player_kicking_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_return_stats,
    _get_player_rushing_stats
)
from src.models.Stats import(
    PlayerDefensiveStats,
    PlayerKickingStats,
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerReturnStats,
    PlayerRushingStats
)


def get_season_records(request):

    response = {
        
    }

    return response