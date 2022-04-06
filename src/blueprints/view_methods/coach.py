from typing import List
from src.constants import (
    coach_stat_schema,
    session,
    users
    )
from src.data_models.CoachInfoData import CoachInfoData
from src.data_models.CoachStatsData import CoachStatsData
from src.utils.coach import _get_coach_season_records


def get_coach_records(request):

    response = {}

    for user in users:

        yearly_coach_info: List[CoachInfoData] = session.query(CoachInfoData).where(
            CoachInfoData.user == user.id
        ).order_by(CoachInfoData.year).all()

        yearly_coach_stats = session.query(CoachStatsData).where(
            CoachStatsData.user == user.id
        ).order_by(CoachStatsData.year).all()

        response[user.id] = _get_coach_season_records(yearly_coach_info, yearly_coach_stats)
    
    return response
