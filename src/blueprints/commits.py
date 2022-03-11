from flask import Blueprint, request

from src.blueprints.view_methods.commits import get_all_commits


commits_bp = Blueprint('commits', __name__)


@commits_bp.route('/', methods=['GET'])
def get_commits():
    return get_all_commits(request)
