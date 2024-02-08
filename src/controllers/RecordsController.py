from src.services.RecordsService import RecordsService


class RecordsController():
    def __init__(self):
        self.RecordsService = RecordsService()

    def get_player_of_the_week_cache(self):
        return self.RecordsService.get_player_of_the_week_cache()

    def get_player_career_records_cache(self):
        return self.RecordsService.get_player_career_records_cache()

    def get_player_game_records_cache(self):
        return self.RecordsService.get_player_game_records_cache()
    
    def get_player_season_records_cache(self):
        return self.RecordsService.get_player_season_records_cache()

    def get_team_game_records_cache(self):
        return self.RecordsService.get_team_game_records_cache()

    def get_team_season_records_cache(self):
        return self.RecordsService.get_team_season_records_cache()
