from src.services.RankingsService import RankingsService

class RankingsController():
    def __init__(self):
        self.RankingsService = RankingsService()

    def get_all_rankings(self):
        return self.RankingsService.get_all_rankings()
