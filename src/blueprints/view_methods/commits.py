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

    response = {}

    for team in user_teams:
        response[team] = commits_schema.dump([commit for commit in commits_data if commit.school == team])

    return response
