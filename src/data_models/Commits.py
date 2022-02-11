from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    String
)

from src.constants import Base


@dataclass
class Commits(Base):
    __tablename__ = 'commits'
    stars = Column(Integer)
    name = Column(String(50), primary_key=True)
    position = Column(String(50))
    rank = Column(Integer)
    school = Column(String(50))
