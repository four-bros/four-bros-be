from typing import List
from src.constants import (session)
from src.data_models.CommitsData import CommitsData

class CommitsDataService():
    def __init__(self) -> None:
        pass

    def get_all_commits(self, year: int) -> List[CommitsData]:
        return session.query(CommitsData).where(
            CommitsData.year == year
        ).order_by(
            CommitsData.school,
            CommitsData.rank
        ).all()
