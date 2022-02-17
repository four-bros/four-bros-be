from dataclasses import dataclass
from sqlalchemy import Column, Float, Integer
from sqlalchemy.sql.schema import ForeignKey

from constants import Base


@dataclass
class ReturnStats(Base):
    __tablename__ = 'return_stats'
    player_id = Column(Integer, ForeignKey('player_info.id'), primary_key=True)
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
