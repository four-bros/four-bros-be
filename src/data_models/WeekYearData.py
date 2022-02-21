from dataclasses import dataclass
from sqlalchemy import Column, Integer

from  src.constants import Base


@dataclass
class WeekYearData(Base):
    __tablename__ = 'week_year'
    __table_args__ = {'extend_existing': True}
    week = Column(Integer)
    year = Column(Integer, primary_key=True)
