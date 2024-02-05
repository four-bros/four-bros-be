from typing import List

from src.constants import (
    commits_schema,
    user_team_names
)
from src.data_services.CommitsDataService import CommitsDataService
from src.data_services.WeekYearDataService import WeekYearDataService
from src.data_models.WeekYearData import WeekYearData
from src.data_models.CommitsData import CommitsData

class CommitsService():
    def __init__(self) -> None:
        self.CommitsDataService = CommitsDataService()
        self.WeekYearDataService = WeekYearDataService()

    def get_all_commits(self) -> dict:
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        commits_data: List[CommitsData] = self.CommitsDataService.get_all_commits(week_year.year)

        response = {}

        for team in user_team_names:
            key = team.replace(' ', '_').lower()
            response[key] = commits_schema.dump(
                [commit for commit in commits_data if commit.school == team])

        return response
