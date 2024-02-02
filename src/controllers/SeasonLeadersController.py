from src.services.SeasonLeadersService import SeasonLeadersService

class SeasonLeadersController():
    def __init__(self):
        self.SeasonLeadersService = SeasonLeadersService()

    def get_player_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        response = {
            'defense': self.SeasonLeadersService.get_season_defensive_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'kick_return': self.SeasonLeadersService.get_season_kick_return_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'kicking': _get_season_kicking_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'passing': _get_season_passing_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'punt_return': _get_season_punt_return_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'punting': _get_season_punting_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'receiving': _get_season_rec_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'rushing': _get_season_rushing_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only),
            'total': _get_season_total_stats_leaders(is_season_specific=is_season_specific, is_users_only=is_users_only)
        }

        return response
