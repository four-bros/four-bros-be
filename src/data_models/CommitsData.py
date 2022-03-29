from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    String
)

from  src.constants import Base


@dataclass
class CommitsData(Base):
    __tablename__ = 'commits'
    # __table_args__ = {'extend_existing': True}
    stars = Column(Integer)
    name = Column(String(50), primary_key=True)
    position = Column(String(50))
    rank = Column(Integer)
    school = Column(String(50))
    week = Column(Integer)
    year = Column(Integer)
