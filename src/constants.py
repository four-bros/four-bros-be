from dotenv import load_dotenv
from typing import List
from urllib.parse import urlparse
from flask import Flask
from flask_cors import CORS
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import(
    declarative_base,
    sessionmaker
)

from src.models.Coach import CoachInfo
from src.schemas.Coach import (
    CoachSeasonRecordSchema,
    CoachStatsSchema
)
from src.schemas.Commits import CommitsSchema
from src.schemas.Players import PlayerSchema, PlayerHofSchema
from src.schemas.Stats import (
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
from src.schemas.Teams import (
    TeamSummarySchema,
    TeamRosterSchema,
    TeamDetailsSchema,
    TeamGameRecordSchema,
    TeamSeasonRecordSchema
)
from src.schemas.WeekYear import (
    WeekYearSchema
)


# App constants
app = Flask(__name__)
CORS(app)

# Environment
load_dotenv()

# DB constants
DB_URL = os.environ['DATABASE_URL']
if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

conn = psycopg2.connect(DB_URL, sslmode='require')
engine = create_engine(DB_URL, echo=False, future=True, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Mac file path
dynasty_dir_path = '/Users/sgreen4/Desktop/data/dynasty3/2043/'
dynasty_file_name = 'OD-4Bros3_week2'
dynasty_file_path = dynasty_dir_path + dynasty_file_name

# User/coach information
ben: CoachInfo = CoachInfo(
    id='ben',
    first_name='Campbell',
    last_name='Ponderosa',
    team_id=107,
    team_name='Virginia'
)
brent: CoachInfo = CoachInfo(
    id='brent',
    first_name='Magnus',
    last_name='Tiedemann',
    team_id=60,
    team_name='New Mexico'
)
dan: CoachInfo = CoachInfo(
    id='dan',
    first_name='Boggs',
    last_name='Moonbeam',
    team_id=108,
    team_name='Virginia Tech'
)
seth: CoachInfo = CoachInfo(
    id='seth',
    first_name='Peewee',
    last_name='FlyGuy',
    team_id=89,
    team_name='TCU'
)

users: List[CoachInfo] = [ben, brent, dan, seth]
user_teams = {user.team_name for user in users}
corrupt_team_ids: List[int] = [160, 161, 162, 163, 164, 300, 400, 1023]
corrupt_player_ids: List[int] = [65535, 4, 8, 2, 13]

# Schema constants
coach_season_record_schema = CoachSeasonRecordSchema()
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
player_hof_schema_single = PlayerHofSchema()
player_hof_schema_list = PlayerHofSchema(many=True)
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
team_schema = TeamSummarySchema()
teams_schema = TeamSummarySchema(many=True)
team_season_record_schema = TeamSeasonRecordSchema()
team_season_records_schema = TeamSeasonRecordSchema(many=True)
team_game_record_schema = TeamGameRecordSchema()
team_game_records_schema = TeamGameRecordSchema(many=True)
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
