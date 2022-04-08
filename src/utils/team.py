from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamStatsData import TeamStatsData
from src.models.Teams import TeamInfo, TeamSeasonRecord, TeamStats
from src.utils.team_stats import (
    _get_team_info,
    _get_team_stats
)

def _get_team_info_and_stats(team):

    team_info_data: TeamInfoData = team[0]
    team_stats_data: TeamStatsData = team[1]

    team_info: TeamInfo = _get_team_info(team_info_data)
    team_stats: TeamStats = _get_team_stats(team_stats_data)

    team_season_record: TeamSeasonRecord = TeamSeasonRecord(
        team_info=team_info,
        team_stats=team_stats
    )

    return team_season_record
