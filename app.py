from flask import Blueprint
from src.blueprints.players import players_bp
from src.blueprints.stats import stats_bp
from src.blueprints.teams import teams_bp
from src.constants import app


home_bp = Blueprint('', __name__)


blueprints = [
    home_bp,
    players_bp,
    stats_bp,
    teams_bp,
]


for bp in blueprints:
    app.register_blueprint(bp, url_prefix=f'/{bp.name}')


home_bp.route('', methods=['GET'])
def index():
    response = {
        'hello': 'how are you?'
    }
    return response


if __name__ == '__main__':
    app.run(debug=True)
