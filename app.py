from flask_cors import cross_origin

from src.blueprints.players import players_bp
from src.blueprints.stats import stats_bp
from src.blueprints.teams import teams_bp
from src.constants import app

blueprints = [
    players_bp,
    stats_bp,
    teams_bp,
]
for bp in blueprints:
    app.register_blueprint(bp, url_prefix=f'/{bp.name}')

app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run()