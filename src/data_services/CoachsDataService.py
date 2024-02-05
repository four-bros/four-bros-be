from typing import List
from sqlalchemy import desc
from src.constants import session
from src.data_models.CoachInfoData import CoachInfoData
from src.data_models.CoachStatsData import CoachStatsData

class CoachsDataService():
    def __init__(self) -> None:
        pass

    def get_coach_records(self, user_id: str) -> List[CoachStatsData]:
        return session.query(CoachStatsData).where(
            CoachStatsData.user == user_id
        ).order_by(desc(CoachStatsData.year)).all()

    def get_coach_info(self, user_id: str) -> List[CoachInfoData]:
        return session.query(CoachInfoData).where(
            CoachInfoData.user == user_id
        ).order_by(desc(CoachInfoData.year)).all()
