from typing import List
from src.constants import (
    coach_stat_schema,
    session,
    users
    )
from src.data_models.CoachStatsData import CoachStatsData


def get_coach_records(request):

    response = {}

    for user in users:

        yearly_user_records: List[CoachStatsData] = session.query(CoachStatsData).where(
            CoachStatsData.user == user.id
        ).all()

        response[user.id] = [coach_stat_schema.dump(year) for year in yearly_user_records]
    
    return response
