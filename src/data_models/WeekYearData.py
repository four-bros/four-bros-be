from dataclasses import dataclass
from sqlalchemy import Column, Integer

from src.constants import Base


@dataclass
class WeekYearData(Base):
    __tablename__ = 'week_year'
    week = Column(Integer)
    year = Column(Integer, primary_key=True)