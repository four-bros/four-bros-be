from dataclasses import dataclass
from sqlalchemy import(
    Column,
    ForeignKey,
    Integer,
    Float,
    String
)

from  src.constants import Base

@dataclass
class TeamStatsData(Base):
    __tablename__ = 'team_stats'
    # __table_args__ = {'extend_existing': True}
    id = Column(String(50), primary_key=True)
    team_id = Column(Integer, ForeignKey('team_info.id'))
    year = Column(Integer)
    games_played = Column(Integer)
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
    total_yards = Column(Integer)
    total_ypg = Column(Float)
    sacks = Column(Integer)
    ints = Column(Integer)
    ff = Column(Integer)
    fr = Column(Integer)
    turnovers = Column(Integer)
    pass_def = Column(Integer)
    safeties = Column(Integer)
    def_tds = Column(Integer)
    kr_yds = Column(Integer)
    kr_tds = Column(Integer)
    pr_yds = Column(Integer)
    pr_tds = Column(Integer)
    