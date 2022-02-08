from flask.helpers import send_from_directory
from flask_cors import cross_origin

from blueprints.players import players_bp
from blueprints.stats import stats_bp
from blueprints.teams import teams_bp
from constants import app

blueprints = [
    players_bp,
    stats_bp,
    teams_bp,
]
for bp in blueprints:
    app.register_blueprint(bp, url_prefix=f'/{bp.name}')

app.route('/hellow', methods=['GET', 'POST'])
@cross_origin()
def hello():
    return 'hello'

app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)