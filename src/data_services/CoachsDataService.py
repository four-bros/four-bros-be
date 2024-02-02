from typing import List
from sqlalchemy import desc
from src.constants import (
    session,
    users
    )
from src.data_models.CoachInfoData import CoachInfoData
from src.data_models.CoachStatsData import CoachStatsData
from src.utils.coach import _get_coach_season_records

class CoachsDataService():
    def get_coach_records() -> List[CoachInfoData]:
        return session.query(CoachInfoData).where(
            CoachInfoData.user.in_(users)
        ).order_by(desc(CoachInfoData.year)).all()

    def get_coach_info() -> List[CoachInfoData]:
        return session.query(CoachInfoData).where(
            CoachInfoData.user.in_(users)
        ).order_by(desc(CoachInfoData.year)).all()
