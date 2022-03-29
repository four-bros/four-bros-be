from dataclasses import dataclass
from sqlalchemy import (
    Column,
    Integer,
    String
)

from  src.constants import Base


@dataclass
class WeekYearData(Base):
    __tablename__ = 'week_year'
    # __table_args__ = {'extend_existing': True}
    id = Column(String(50), primary_key=True)
    week = Column(Integer)
    year = Column(Integer)
