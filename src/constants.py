from typing import List
from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import(
    declarative_base,
    sessionmaker
)

from src.models.Coach import CoachInfo
from src.responses.Coach import (
    CoachInfoSchema,
    CoachStatsSchema
)
from src.responses.Commits import CommitsSchema
from src.responses.Players import PlayerSchema
from src.responses.Stats import (
    PlayerDefensiveStatsSchema,
    PlayerDetailsSchema,
    PlayerKickingStatsSchema,
    PlayerKickReturnStatsSchema,
    PlayerPassingStatsSchema,
    PlayerPuntingStatsSchema,
    PlayerPuntReturnStatsSchema,
    PlayerReceivingStatsSchema,
    PlayerKickReturnAndPuntReturnStatsSchema,
    PlayerRushingStatsSchema,
    PlayerTotalStatsSchema,
)
from src.responses.Teams import (
    TeamInfoSchema,
    TeamRosterSchema,
    TeamDetailsSchema
)
from src.responses.WeekYear import (
    WeekYearSchema
)


# App constants
app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///ncaa.db"
CORS(app)


# File constants
# Windows file path
# dynasty_file_path = 'D:\Content\E00001485AECABB5\\454109B6\\00000001\OD-4Bros3'
# Mac file path
dynasty_file_path = 'data/OD-4Bros3'
user_teams = {'Baylor', 'Ole Miss', 'Vanderbilt', 'Wyoming'}

# User/coach information
ben: CoachInfo = CoachInfo(
    id='ben',
    first_name='Campbell',
    last_name='Ponderosa',
    team_id=106,
    team_name='Vanderbilt'
)
brent: CoachInfo = CoachInfo(
    id='brent',
    first_name='Magnus',
    last_name='Tiedemann',
    team_id=73,
    team_name='Ole Miss'
)
dan: CoachInfo = CoachInfo(
    id='dan',
    first_name='Boggs',
    last_name='Moonbeam',
    team_id=11,
    team_name='Baylor'
)
seth: CoachInfo = CoachInfo(
    id='seth',
    first_name='Peewee',
    last_name='FlyGuy',
    team_id=115,
    team_name='Wyoming'
)

users: List[CoachInfo] = [ben, brent, dan, seth]


# DB constants
db_path = "sqlite+pysqlite:///ncaa.db?check_same_thread=False"
engine = create_engine(db_path, echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Schema constants
coach_stat_schema = CoachStatsSchema()
coach_stats_schema = CoachStatsSchema(many=True)
commit_schema = CommitsSchema()
commits_schema = CommitsSchema(many=True)
defensive_stat_schema = PlayerDefensiveStatsSchema()
defensive_stats_schema = PlayerDefensiveStatsSchema(many=True)
kicking_stat_schema = PlayerKickingStatsSchema()
kicking_stats_schema = PlayerKickingStatsSchema(many=True)
kick_return_stat_schema = PlayerKickReturnStatsSchema()
kick_return_stats_schema = PlayerKickReturnStatsSchema(many=True)
passing_stat_schema = PlayerPassingStatsSchema()
passing_stats_schema = PlayerPassingStatsSchema(many=True)
player_details_schema_single = PlayerDetailsSchema()
player_details_schema_list = PlayerDetailsSchema(many=True)
player_schema_single = PlayerSchema()
player_schema_list = PlayerSchema(many=True)
punt_return_stat_schema = PlayerPuntReturnStatsSchema()
punt_return_stats_schema = PlayerPuntReturnStatsSchema(many=True)
punting_stat_schema = PlayerPuntingStatsSchema()
punting_stats_schema = PlayerPuntingStatsSchema(many=True)
receiving_stat_schema = PlayerReceivingStatsSchema()
receiving_stats_schema = PlayerReceivingStatsSchema(many=True)
return_stat_schema = PlayerKickReturnAndPuntReturnStatsSchema()
return_stats_schema = PlayerKickReturnAndPuntReturnStatsSchema(many=True)
rushing_stat_schema = PlayerRushingStatsSchema()
rushing_stats_schema = PlayerRushingStatsSchema(many=True)
team_details_schema = TeamDetailsSchema(many=True)
team_schema = TeamInfoSchema()
teams_schema = TeamInfoSchema(many=True)
team_roster_schema = TeamRosterSchema(many=True)
total_stat_schema = PlayerTotalStatsSchema()
total_stats_schema = PlayerTotalStatsSchema(many=True)
week_year_schema = WeekYearSchema()


# String Enums
class Positions():
    QB = 'QB'
    RB = 'RB'
    FB = 'FB'
    WR = 'WR'
    TE = 'TE'
    LT = 'LT'
    LG = 'LG'
    C = 'C'
    RG = 'RG'
    RT = 'RT'
    RE = 'RE'
    LE = 'LE'
    DT = 'DT'
    LLB = 'LLB'
    RLB = 'RLB'
    MLB = 'MLB'
    CB = 'CB'
    FS = 'FS'
    SS = 'SS'
    K = 'K'
    P = 'P'

    offense_positions = [
        QB, RB, FB, WR, TE, LT, LG, C, RG, RT
    ]

    defense_positions = [
        RE, LE, DT, LLB, RLB, MLB, CB, FS, SS
    ]

    sp_teams_positions = [
        K, P
    ]
