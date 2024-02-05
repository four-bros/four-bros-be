from src.services.TeamsService import TeamsService


class TeamsController():
    def __init__(self):
        self.TeamsService = TeamsService()

    def get_all_teams(self):
        return self.TeamsService.get_all_teams()

    def get_team_details_by_id(self, team_id):
        return self.TeamsService.get_team_details_by_id(team_id)

    def get_user_teams_details(self):
        return self.TeamsService.get_user_teams_details()

    def get_roster_by_team_id(self, team_id):
        return self.TeamsService.get_roster_by_team_id(team_id)

    def get_players_stats_by_team_id(self, team_id: int):
        return self.TeamsService.get_team_player_stats_by_team_id(team_id)

    def get_user_teams_player_stats(self):
        return self.TeamsService.get_user_teams_player_stats()
    
    def get_team_stats_by_id(self, team_id: int):
        return self.TeamsService.get_team_stats_by_id(team_id)

    def get_user_teams_stats(self):
        return self.TeamsService.get_user_teams_stats()
