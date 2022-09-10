from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    String
)

from  src.constants import Base


@dataclass
class HallOfFame(Base):
	__tablename__ = 'hall_of_fame'
	id = Column(Integer, primary_key = True)
	player_id = Column(String(50))
