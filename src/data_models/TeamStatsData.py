from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    Float
)

from src.constants import Base

@dataclass
class TeamStatsData(Base):
    __tablename__ = 'team_stats'
    id = Column(Integer, primary_key=True)
    total_points = Column(Integer)
    ppg = Column(Float)
    pass_yds = Column(Integer)
    pass_ypg = Column(Float)
    pass_tds = Column(Integer)
    rush_yds = Column(Integer)
    rush_ypg = Column(Float)
    rush_tds = Column(Integer)
    rec_yds = Column(Integer)
    rec_ypg = Column(Float)
    rec_tds = Column(Integer)
    sacks = Column(Integer)
    ints = Column(Integer)
    ff = Column(Integer)
    fr = Column(Integer)
    pass_def = Column(Integer)
    safeties = Column(Integer)
    def_tds = Column(Integer)
    kr_yds = Column(Integer)
    kr_tds = Column(Integer)
    pr_yds = Column(Integer)
    pr_tds = Column(Integer)
    