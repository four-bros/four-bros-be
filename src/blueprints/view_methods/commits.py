from typing import List
from src.constants import(
    commits_schema,
    session,
    user_teams
)
from src.data_models.CommitsData import CommitsData


def get_all_commits(request):

    commits_data: List[CommitsData] = session.query(CommitsData).order_by(
        CommitsData.school,
        CommitsData.rank
    ).all()

    commits_json = commits_schema.dump(commits_data)

    response = {
        'commits': commits_json
    }

    return response
