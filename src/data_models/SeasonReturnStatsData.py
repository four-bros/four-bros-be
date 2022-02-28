from dataclasses import dataclass
from sqlalchemy import (
    Column,
    Float,
    Integer,
    String
)
from sqlalchemy.sql.schema import ForeignKey

from src.constants import Base


@dataclass
class SeasonReturnStatsData(Base):
    __tablename__ = 'season_return_stats'
    __table_args__ = {'extend_existing': True}
    id = Column(String(50), primary_key=True)
    player_id = Column(Integer, ForeignKey('player_info.id'))
    year = Column(String(10))
    games_played = Column(Integer)
    kick_returns = Column(Integer)
    kr_yds = Column(Integer)
    kr_avg = Column(Float)
    kr_tds = Column(Integer)
    long_kr = Column(Integer)
    punt_returns = Column(Integer)
    pr_yds = Column(Integer)
    pr_avg = Column(Float)
    pr_tds = Column(Integer)
    long_pr = Column(Integer)
