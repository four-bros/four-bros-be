from enum import Enum
from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import(
    declarative_base,
    sessionmaker
)

# App constants
app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///ncaa.db"
CORS(app)

# File constants
dynasty_file_path = 'D:\Content\E00001485AECABB5\\454109B6\\00000001\OD-4Bros3'
user_teams = {'Syracuse', 'USC', 'Vanderbilt', 'Wyoming'}

# DB constants
db_path = "sqlite+pysqlite:///ncaa.db?check_same_thread=False"
engine = create_engine(db_path, echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Request methods
class HTTPMethods(Enum):
    GET = 'GET'
    POST = 'POST'