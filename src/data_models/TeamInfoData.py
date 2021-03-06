from dataclasses import dataclass
from sqlalchemy import(
    Boolean,
    Column,
    Integer,
    String
)

from  src.constants import Base

@dataclass
class TeamInfoData(Base):
    __tablename__ = 'team_info'
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    team_name = Column(String(50))
    team_short_name = Column(String(50))
    nickname = Column(String(50))
    is_user = Column(Boolean)
    wins = Column(Integer)
    losses = Column(Integer)
    coachs_poll_1st_votes = Column(Integer)
    bcs_rank = Column(Integer)
    coachs_poll_rank = Column(Integer)
    coachs_poll_points = Column(Integer)
    media_poll_rank = Column(Integer)
    media_poll_points = Column(Integer)
    

    def __repr__(self):
        return f'ID: {self.id}, Name: {self.team_name}'

