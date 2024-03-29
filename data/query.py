from typing import List
from sqlalchemy import LABEL_STYLE_DISAMBIGUATE_ONLY, desc
from sqlalchemy.sql import exists

from data import (
    def_stats,
    player_info,
    off_stats,
    team_info,
    week_year
)
from src.constants import (
    Base,
    player_defensive_stats_schema,
    engine,
    session
)
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.WeekYearData import WeekYearData
from src.models.Stats import PlayerDefensiveStats
from src.schemas.Stats import PassingStatsSchema
from src.schemas.Players import PlayerSchema
from src.utils.player import _get_player_season_defensive_stats


passing_stat_schema = PassingStatsSchema()
passing_stats_schema = PassingStatsSchema(many=True)
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

week_year: WeekYearData = session.query(WeekYearData).first()

top_long_int_ret_data = session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
    PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
    SeasonDefensiveStatsData.year == week_year.year
).order_by(desc(SeasonDefensiveStatsData.long_int_ret)).limit(10)


converted_players: List[PlayerDefensiveStats] = [
    _get_player_season_defensive_stats(player) for player in top_long_int_ret_data]

converted_players_json = player_defensive_stats_schema.dump(converted_players)

print(len(converted_players))

print(converted_players_json[0])
