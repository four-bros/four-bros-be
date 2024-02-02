from sqlalchemy import desc
from src.constants import (session)
from src.data_models.WeekYearData import WeekYearData

class WeekYearDataService():
    def __init__(self) -> None:
        pass

    def get_week_year(self) -> WeekYearData:
        return session.query(WeekYearData).order_by(
            desc(WeekYearData.year),
            desc(WeekYearData.week)
        ).first()
