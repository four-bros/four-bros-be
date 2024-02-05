from src.services.TeamsSeasonStatsService import TeamsSeasonStatsService


class TeamsSeasonLeadersController():
    def __init__(self):
        self.TeamsSeasonStatsService = TeamsSeasonStatsService()

    def get_team_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        return self.TeamsSeasonStatsService.get_team_season_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only)
