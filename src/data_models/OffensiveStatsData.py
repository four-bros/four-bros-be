from dataclasses import dataclass
from sqlalchemy import Column, Float, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String

from constants import Base


@dataclass
class OffensiveStatsData(Base):
    __tablename__ = 'offensive_stats'
    player_id = Column(Integer, ForeignKey('player_info.id'), primary_key=True)
    pass_yards = Column(Integer)
    longest_rec = Column(Integer)
    longest_pass = Column(Integer)
    longest_run = Column(Integer)
    year = Column(String(10))
    receptions = Column(Integer)
    sacked = Column(Integer)
    rec_yards = Column(Integer)
    rush_yards = Column(Integer)
    yac = Column(Integer)
    pass_tds = Column(Integer)
    games_played = Column(Integer)
    rec_tds = Column(Integer)
    rush_tds = Column(Integer)
    ya_contact = Column(Integer)
    completions = Column(Integer)
    ints = Column(Integer)
    drops = Column(Integer)
    pass_att = Column(Integer)
    rush_att = Column(Integer)
    broke_tkls = Column(Integer)
    fumbles = Column(Integer)
    twenty_plus_yd_runs = Column(Integer)
    pass_yp_attempt = Column(Float)
    pass_yp_game = Column(Float)
    rush_yp_carry = Column(Float)
    rush_yp_game = Column(Float)
    rec_yp_catch = Column(Float)
    rec_yp_game = Column(Float)
    pass_rating = Column(Float)
    
    def __repr__(self) -> str:
        return f'ID: {self.player_id}, Passing Yds: {self.pass_yards}, Passing TDs: {self.pass_tds}'
