from dataclasses import dataclass
from sqlalchemy import(
    Column,
    Integer,
    String
)
from sqlalchemy.dialects.postgresql import JSONB

from  src.constants import Base


@dataclass
class Records(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    record_type = Column(String(50))
    record = Column(JSONB)
