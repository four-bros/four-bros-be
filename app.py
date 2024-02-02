import redis
import json
from flask import jsonify, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from src.blueprints.coach import coach_bp
from src.blueprints.commits import commits_bp
from src.blueprints.home import home_bp
from src.blueprints.players import players_bp
from src.blueprints.rankings import rankings_bp
from src.blueprints.records import records_bp
from src.blueprints.stats import stats_bp
from src.blueprints.teams import teams_bp
from src.constants import app

cache = redis.Redis(host='redis', port=6379)

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

swagger_url = '/swagger'
swagger_api_url = '/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(swagger_url, swagger_api_url)
app.register_blueprint(swagger_ui_blueprint)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))
    
@app.route('/', methods=['GET'])
def index():
    return redirect('/swagger', code=302)

if __name__ == '__main__':
    app.run()
