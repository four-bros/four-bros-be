from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    String,
    Boolean
)
from sqlalchemy.sql.schema import ForeignKey

from  src.constants import Base


@dataclass
class CoachStatsData(Base):
    __tablename__ = 'coach_stats'
    id = Column(String(50), primary_key=True)
    coach_id = Column(String(10)), ForeignKey('coach_info.id')
    user = Column(String(10))
    year = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    national_title = Column(Boolean)
