from dataclasses import dataclass
from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float

from src.constants import Base


@dataclass
class SeasonDefensiveStatsData(Base):
    __tablename__ = 'season_defensive_stats'
    __table_args__ = {'extend_existing': True}
    id = Column(String(50), primary_key=True)
    player_id = Column(Integer, ForeignKey('player_info.id'))
    year = Column(String(10))
    games_played = Column(Integer)
    solo_tkls = Column(Float)
    asst_tkls = Column(Float)
    total_tkls = Column(Float)
    tfl = Column(Integer)
    sacks = Column(Float)
    half_a_sack = Column(Float)
    total_sacks = Column(Float)
    pass_def = Column(Integer)
    ints_made = Column(Integer)
    int_ret_yards = Column(Integer)
    long_int_ret = Column(Integer)
    forced_fumbles = Column(Integer)
    fumbles_rec = Column(Integer)
    fum_rec_yards = Column(Integer)
    def_tds = Column(Integer)
    safeties = Column(Integer)
    blocked_kicks = Column(Integer)
