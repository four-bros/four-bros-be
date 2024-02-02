from typing import List
from src.constants import week_year_schema
from src.data_models.WeekYearData import WeekYearData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_services.TeamInfoDataService import TeamInfoDataService
from src.data_services.WeekYearDataService import WeekYearDataService
from src.models.WeekYear import WeekYear
from src.schemas.Teams import teams_details_schema

class UsersService():
    def __init__(self) -> None:
        self.TeamInfoDataService = TeamInfoDataService()
        self.WeekYearDataService = WeekYearDataService()

    def get_users_and_week(self) -> dict:
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()

        user_teams: List[TeamInfoData] = self.TeamInfoDataService.get_users_team_info()

        # convert data models to objects
        current_week_year: WeekYear = WeekYear(
            week=week_year.week,
            year=week_year.year
        )

        # dump objects to JSON
        week_year_json = week_year_schema.dump(current_week_year)
        user_teams_json = teams_details_schema.dump(user_teams)

        response = {
            'week_year': week_year_json,
            'user_teams': user_teams_json
        }

        return response
