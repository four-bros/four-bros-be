from enum import Enum
from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import(
    declarative_base,
    sessionmaker
)

from src.responses.Stats import PlayerDefensiveStatsSchema, PlayerKickingStatsSchema, PlayerPassingStatsSchema, PlayerReceivingStatsSchema, PlayerReturnStatsSchema, PlayerRushingStatsSchema

# App constants
app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///ncaa.db"
CORS(app)


# File constants
dynasty_file_path = 'D:\Content\E00001485AECABB5\\454109B6\\00000001\OD-4Bros3'
user_teams = {'Baylor', 'Syracuse', 'Vanderbilt', 'Wyoming'}


# DB constants
db_path = "sqlite+pysqlite:///ncaa.db?check_same_thread=False"
engine = create_engine(db_path, echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Schema constants
defensive_stat_schema = PlayerDefensiveStatsSchema()
defensive_stats_schema = PlayerDefensiveStatsSchema(many=True)
kicking_stat_schema = PlayerKickingStatsSchema()
kicking_stats_schema = PlayerKickingStatsSchema(many=True)
passing_stat_schema = PlayerPassingStatsSchema()
passing_stats_schema = PlayerPassingStatsSchema(many=True)
receiving_stat_schema = PlayerReceivingStatsSchema()
receiving_stats_schema = PlayerReceivingStatsSchema(many=True)
return_stat_schema = PlayerReturnStatsSchema()
return_stats_schema = PlayerReturnStatsSchema(many=True)
rushing_stat_schema = PlayerRushingStatsSchema()
rushing_stats_schema = PlayerRushingStatsSchema(many=True)


# Request methods
class HTTPMethods(Enum):
    GET = 'GET'
    POST = 'POST'