from src.services.PlayersSeasonStatsService import PlayersSeasonStatsService


class PlayersSeasonLeadersController():
    def __init__(self):
        self.PlayersSeasonStatsService = PlayersSeasonStatsService()

    def get_all_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'defense': self.PlayersSeasonStatsService.get_season_defensive_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'kick_return': self.PlayersSeasonStatsService.get_season_kick_return_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'kicking': self.PlayersSeasonStatsService.get_season_kicking_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'passing': self.PlayersSeasonStatsService.get_season_passing_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'punt_return': self.PlayersSeasonStatsService.get_season_punt_return_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'punting': self.PlayersSeasonStatsService.get_season_punting_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'receiving': self.PlayersSeasonStatsService.get_season_rec_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'rushing': self.PlayersSeasonStatsService.get_season_rushing_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
            'total': self.PlayersSeasonStatsService.get_season_total_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            )
        }

        return response

    def get_defensive_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'defense': self.PlayersSeasonStatsService.get_season_defensive_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_kick_return_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'kick_return': self.PlayersSeasonStatsService.get_season_passing_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_kicking_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'kicking': self.PlayersSeasonStatsService.get_season_kicking_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_passing_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'passing': self.PlayersSeasonStatsService.get_season_passing_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_punt_return_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'punt_return': self.PlayersSeasonStatsService.get_season_punt_return_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_punting_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'punting': self.PlayersSeasonStatsService.get_season_punting_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_receiving_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'receiving': self.PlayersSeasonStatsService.get_season_rec_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_rushing_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'rushing': self.PlayersSeasonStatsService.get_season_rushing_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response

    def get_total_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'total': self.PlayersSeasonStatsService.get_season_total_stats_leaders(
                is_season_specific=is_season_specific, is_users_only=is_users_only
            ),
        }

        return response
