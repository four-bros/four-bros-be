from typing import List
import redis
from src.blueprints.coach import coach_bp
from src.blueprints.commits import commits_bp
from src.blueprints.home import home_bp
from src.blueprints.players import players_bp
from src.blueprints.rankings import rankings_bp
from src.blueprints.records import records_bp
from src.blueprints.stats import stats_bp
from src.blueprints.teams import teams_bp
from src.constants import app

blueprints = [
    coach_bp,
    commits_bp,
    home_bp,
    players_bp,
    rankings_bp,
    records_bp,
    stats_bp,
    teams_bp,
]

# register the various endpoints
for bp in blueprints:
    app.register_blueprint(bp, url_prefix=f'/{bp.name}')

cache = redis.Redis(host='redis', port=6379)


@app.route('/', methods=['GET'])
def index():
    records_endpoints: List[str] = [
        'career',
        'game',
        'season'
    ]

    players_endpoints: List[str] = [
        '<player_id>'
    ]

    teams_endpoints: List[str] = [
        '/',
        '<team_id>',
        '<team_id>/stats'
    ]

    backend_endpoints = {
        'coach': '/',
        'commits': '/',
        'home': '/',
        'players': players_endpoints,
        'rankings': '/',
        'records': records_endpoints,
        'stats': 'season/leaders',
        'teams': teams_endpoints,
    }

    response = {
        'backend_endpoints': backend_endpoints
    }

    return response


if __name__ == '__main__':
    app.run()
