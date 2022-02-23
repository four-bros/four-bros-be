from typing import List
from sqlalchemy import LABEL_STYLE_DISAMBIGUATE_ONLY, desc
from sqlalchemy.sql import exists

from data import(
    def_stats,
    player_info,
    off_stats,
    team_info,
    week_year
)
from src.constants import(
    Base,
    defensive_stats_schema,
    engine,
    session
)
from src.data_models.DefensiveStatsData import DefensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.OffensiveStatsData import OffensiveStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.WeekYearData import WeekYearData
from src.models.Stats import PlayerDefensiveStats
from src.responses.Stats import PassingStatsSchema
from src.responses.Players import PlayerSchema
from src.utils.player_stats import _get_player_defensive_stats


passing_stat_schema = PassingStatsSchema()
passing_stats_schema = PassingStatsSchema(many=True)
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

week_year: WeekYearData = session.query(WeekYearData).first()

top_long_int_ret_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        DefensiveStatsData.year == week_year.year
        ).order_by(desc(DefensiveStatsData.long_int_ret)).limit(10)


converted_players: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in top_long_int_ret_data]

converted_players_json = defensive_stats_schema.dump(converted_players)

print(len(converted_players))

print(converted_players_json[0])
