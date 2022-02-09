from dataclasses import dataclass
from sqlalchemy import Column, Integer

from constants import Base


@dataclass
class WeekYear(Base):
    __tablename__ = 'week_year'
    week = Column(Integer)
    year = Column(Integer, primary_key=True)
