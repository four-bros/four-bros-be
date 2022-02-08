from typing import List

from sqlalchemy.sql.expression import desc

from constants import session

from data_models.TeamInfo import TeamInfo
from responses.Teams import TeamSchema


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)


def get_all_teams(request) -> TeamSchema:
    
    teams: List[TeamInfo] = session.query(TeamInfo).order_by(desc(TeamInfo.is_user)).all()
    teams_json = teams_schema.dump(teams)
    
    response = {
        'teams': teams_json
    }
    
    return response


def get_team_by_team_id(request, team_id) -> TeamSchema:
    
    team: TeamInfo = session.query(TeamInfo).where(TeamInfo.team_id == team_id).one()
    response: TeamSchema = team_schema.dump(team)
    
    return response
