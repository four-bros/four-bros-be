from src.data_services.RecordsDataService import RecordsDataService

class RecordsService():
    def __init__(self) -> None:
        self.RecordsDataService = RecordsDataService()

    def get_player_career_records_cache(self):
        return self.RecordsDataService.get_player_career_records_cache()


    def get_player_game_records_cache(self):
        return self.RecordsDataService.get_player_game_records_cache()


    def get_player_season_records_cache(self):
        return self.RecordsDataService.get_player_season_records_cache()


    def get_team_game_records_cache(self):
        return self.RecordsDataService.get_team_game_records_cache()


    def get_team_season_records_cache(self):
        return self.RecordsDataService.get_team_season_records_cache()
