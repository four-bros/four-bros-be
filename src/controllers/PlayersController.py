from typing import List
from src.services.PlayersService import PlayersService
from src.schemas.Players import PlayerSchema

class PlayersController():
    def __init__(self):
        self.PlayersService = PlayersService()

    def get_all_players(self) -> List[PlayerSchema]:
        return self.PlayersService.get_all_players()
    
    def get_player_by_player_id(self, player_id: str) -> PlayerSchema:
        return self.PlayersService.get_player_by_player_id(player_id)
    
    def get_player_of_the_week(self):
        return self.PlayersService.get_player_of_the_week()

    def get_hof(self):
        return self.PlayersService.get_hof()
