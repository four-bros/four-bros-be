from typing import List
from sqlalchemy import desc
from src.constants import (
    session,
    week_year_schema
)
from src.data_models.WeekYearData import WeekYearData
from src.data_models.TeamInfoData import TeamInfoData
from src.models.WeekYear import WeekYear
from src.schemas.Teams import details_schema


def get_home_data():

    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    user_teams: List[TeamInfoData] = session.query(TeamInfoData).where(TeamInfoData.is_user).order_by(
      TeamInfoData.team_name
    ).all()

    # convert data models to objects
    current_week_year: WeekYear = WeekYear(
        week=week_year.week,
        year=week_year.year
    )

    # dump objects to JSON
    week_year_json = week_year_schema.dump(current_week_year)
    user_teams_json = details_schema.dump(user_teams)

    response = {
        'week_year': week_year_json,
        'user_teams': user_teams_json
    }

    return response
