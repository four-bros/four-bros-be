from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    String
)

from  src.constants import Base


@dataclass
class CoachInfoData(Base):
    __tablename__ = 'coach_info'
    id = Column(String(10), primary_key=True)
    user = Column(String(10))
    first_name = Column(String(50))
    last_name = Column(String(50))
    team_id = Column(Integer)
    team_name = Column(String(50))
