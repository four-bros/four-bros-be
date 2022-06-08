from typing import List
from sqlalchemy import desc

from src.constants import(
    commits_schema,
    session,
    user_teams
)
from src.data_models.CommitsData import CommitsData
from src.data_models.WeekYearData import WeekYearData


def get_all_commits(request):

    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    commits_data: List[CommitsData] = session.query(CommitsData).where(
        CommitsData.year == week_year.year
    ).order_by(
        CommitsData.school,
        CommitsData.rank
    ).all()

    response = {}

    for team in user_teams:
        key = team.replace(' ', '_').lower()
        response[key] = commits_schema.dump([commit for commit in commits_data if commit.school == team])

    return response
