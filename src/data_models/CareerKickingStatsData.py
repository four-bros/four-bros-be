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
class CareerKickingStatsData(Base):
    __tablename__ = 'career_kicking_stats'
    # __table_args__ = {'extend_existing': True}
    id = Column(String(50), primary_key=True)
    player_id = Column(String(50), ForeignKey('player_info.id'))
    year = Column(String(20))
    games_played = Column(Integer)
    fg_made = Column(Integer)
    fg_att = Column(Integer)
    fg_blocked = Column(Integer)
    fg_pct = Column(Float)
    long_fg = Column(Integer)
    xp_made = Column(Integer)
    xp_att = Column(Integer)
    xp_blocked = Column(Integer)
    xp_pct = Column(Float)
    fg_made_17_29 = Column(Integer)
    fg_att_17_29 = Column(Integer)
    fg_made_30_39 = Column(Integer)
    fg_att_30_39 = Column(Integer)
    fg_made_40_49 = Column(Integer)
    fg_att_40_49 = Column(Integer)
    fg_made_50_plus = Column(Integer)
    fg_att_50_plus = Column(Integer)
    fg_50_plus_pct = Column(Float)
    kickoffs = Column(Integer)
    ko_touchbacks = Column(Integer)
    number_punts = Column(Integer)
    total_punt_yards = Column(Integer)
    punt_avg = Column(Float)
    long_punt = Column(Integer)
    punts_blocked = Column(Integer)
    punt_touchbacks = Column(Integer)
    net_punting = Column(Integer)
    inside_twenty = Column(Integer)
    net_avg = Column(Float)
