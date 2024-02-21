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
            response[key] = {
                'avg_star': self._calculate_average_star_ratings(team, commits_data),
                'commits': commits_schema.dump([commit for commit in commits_data if commit.school == team]),
                'stars': self._calculate_commits_star_count(team, commits_data),
                'top_100': self._calculate_top_100_commits(team, commits_data)
            }

        return response

    def _calculate_commits_star_count(self, team: str, commits: List[CommitsData]) -> dict:
        five_stars = [commit for commit in commits if commit.school == team and commit.stars == 5]
        four_stars = [commit for commit in commits if commit.school == team and commit.stars == 4]
        three_stars = [commit for commit in commits if commit.school == team and commit.stars == 3]
        two_stars = [commit for commit in commits if commit.school == team and commit.stars == 2]
        one_stars = [commit for commit in commits if commit.school == team and commit.stars == 1]
        return {
            '5': len(five_stars),
            '4': len(four_stars),
            '3': len(three_stars),
            '2': len(two_stars),
            '1': len(one_stars),
        }
    
    def _calculate_top_100_commits(self, team: str, commits: List[CommitsData]) -> int:
        top_100_commits = [commit for commit in commits if commit.school == team and commit.rank <= 100]
        return len(top_100_commits)

    def _calculate_average_star_ratings(self, team: str, commits: List[CommitsData]) -> int:
        commits = [commit for commit in commits if commit.school == team]
        total_star_sum = 0

        for commit in commits:
            total_star_sum += commit.stars

        return round(total_star_sum / len(commits), 2)
