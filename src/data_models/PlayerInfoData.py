from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    String,
    Boolean
)
from sqlalchemy.sql.schema import ForeignKey

from src.constants import Base


@dataclass
class PlayerInfoData(Base):
    __tablename__ = 'player_info'
    id = Column(String(50), primary_key=True)
    roster_id = Column(Integer)
    team_id = Column(Integer, ForeignKey('team_info.id'))
    first_name = Column(String(50))
    last_name = Column(String(50))
    player_year = Column(String(10))
    redshirt = Column(Boolean)
    jersey_number = Column(Integer)
    position = Column(String(4))
    hometown_desc = Column(Integer)
    overall = Column(Integer)
    play_recognition = Column(Integer)
    press = Column(Integer)
    power_moves = Column(Integer)
    kick_accuracy = Column(Integer)
    throwing_power = Column(Integer)
    throwing_accuracy = Column(Integer)
    agility = Column(Integer)
    stamina = Column(Integer)
    acceleration = Column(Integer)
    pursuit = Column(Integer)
    route_running = Column(Integer)
    speed = Column(Integer)
    trucking = Column(Integer)
    ball_carrier_vision = Column(Integer)
    catch_in_traffic = Column(Integer)
    block_shedding = Column(Integer)
    strength = Column(Integer)
    catch = Column(Integer)
    injury = Column(Integer)
    tackling = Column(Integer)
    pass_blocking = Column(Integer)
    run_blocking = Column(Integer)
    break_tackle = Column(Integer)
    impact_blocking = Column(Integer)
    jump = Column(Integer)
    carry = Column(Integer)
    stiff_arm = Column(Integer)
    kick_power = Column(Integer)
    awareness = Column(Integer)
    release = Column(Integer)
    spec_catch = Column(Integer)
    elusiveness = Column(Integer)
    height = Column(String(10))
    spin_move = Column(Integer)
    weight = Column(Integer)
    hit_power = Column(Integer)
    kick_return = Column(Integer)
    man_coverage = Column(Integer)
    zone_coverage = Column(Integer)
    finesse_moves = Column(Integer)
    juke_move = Column(Integer)
    is_active = Column(Boolean)


    def __repr__(self):
        return f'ID: {self.id}, Name: {self.first_name} {self.last_name}'
