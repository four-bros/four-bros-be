from dataclasses import dataclass
from sqlalchemy import (
    Column,
    Float,
    Integer,
    String
)
from sqlalchemy.sql.schema import ForeignKey

from  src.constants import Base


@dataclass
class ReturnStatsData(Base):
    __tablename__ = 'return_stats'
    __table_args__ = {'extend_existing': True}
    id = Column(String(50), primary_key=True)
    player_id = Column(Integer, ForeignKey('player_info.id'))
    kick_returns = Column(Integer)
    year = Column(Integer)
    long_kr = Column(Integer)
    punt_returns = Column(Integer)
    long_pr = Column(Integer)
    games_played = Column(Integer)
    kr_tds = Column(Integer)
    pr_tds = Column(Integer)
    kr_yds = Column(Integer)
    pr_yds = Column(Integer)
    kr_avg = Column(Float)
    pr_avg = Column(Float)
