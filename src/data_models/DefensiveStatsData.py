from dataclasses import dataclass
from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float, String

from src.constants import Base


@dataclass
class DefensiveStatsData(Base):
    __tablename__ = 'defensive_stats'
    player_id = Column(Integer, ForeignKey('player_info.id'), primary_key=True)
    long_int_ret = Column(Integer)
    sacks = Column(Float)
    year = Column(String(10))
    forced_fumbles = Column(Integer)
    solo_tkls = Column(Float)
    safeties = Column(Integer)
    pass_def = Column(Integer)
    blocked_kicks = Column(Integer)
    tfl = Column(Integer)
    ints_made = Column(Integer)
    games_played = Column(Integer)
    fumbles_rec = Column(Integer)
    half_a_sack = Column(Float)
    asst_tkls = Column(Float)
    def_tds = Column(Integer)
    fum_rec_yards = Column(Integer)
    int_ret_yards = Column(Integer)
    total_tkls = Column(Float)
