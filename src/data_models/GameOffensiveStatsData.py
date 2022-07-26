from dataclasses import dataclass
from sqlalchemy import (
    Column,
    Integer,
    Float,
    String
)
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String

from  src.constants import Base


@dataclass
class GameOffensiveStatsData(Base):
    __tablename__ = 'game_offensive_stats'
    # __table_args__ = {'extend_existing': True}
    id = Column(String(50), primary_key=True)
    player_id = Column(String(50), ForeignKey('player_info.id'))
    week = Column(Integer)
    year = Column(Integer)
    games_played = Column(Integer)
    completions = Column(Integer)
    pass_att = Column(Integer)
    pass_yards = Column(Integer)
    pass_tds = Column(Integer)
    ints = Column(Integer)
    pass_ypa = Column(Float)
    pass_ypg = Column(Float)
    longest_pass = Column(Integer)
    pass_rating = Column(Float)
    sacked = Column(Integer)
    rush_att = Column(Integer)
    rush_yards = Column(Integer)
    rush_tds = Column(Integer)
    rush_ypc = Column(Float)
    rush_ypg = Column(Float)
    longest_run = Column(Integer)
    broke_tkls = Column(Integer)
    ya_contact = Column(Integer)
    fumbles = Column(Integer)
    twenty_plus_yd_runs = Column(Integer)
    receptions = Column(Integer)
    rec_yards = Column(Integer)
    rec_tds = Column(Integer)
    rec_ypc = Column(Float)
    rec_ypg = Column(Float)
    yac = Column(Integer)
    longest_rec = Column(Integer)
    drops = Column(Integer)
    total_yards = Column(Integer)
    total_ypg = Column(Float)
    total_tds = Column(Integer)
    turnovers = Column(Integer)
    comp_pct = Column(Float)

    
    def __repr__(self) -> str:
        return f'ID: {self.player_id}, Passing Yds: {self.pass_yards}, Passing TDs: {self.pass_tds}'
