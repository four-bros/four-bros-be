from sqlalchemy import desc
from src.constants import (session)
from src.data_models.WeekYearData import WeekYearData

class WeekYearDataService():
    def get_week_year() -> WeekYearData:
        return session.query(WeekYearData).order_by(
            desc(WeekYearData.year),
            desc(WeekYearData.week)
        ).first()
