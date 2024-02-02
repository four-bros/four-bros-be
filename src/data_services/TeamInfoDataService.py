from typing import List
from src.constants import session
from src.data_models.TeamInfoData import TeamInfoData

class TeamInfoDataService():
    def __init__(self) -> None:
        pass

    def get_users_team_info(self) -> List[TeamInfoData]:
        return session.query(TeamInfoData).where(TeamInfoData.is_user).order_by(
        TeamInfoData.team_name
        ).all()
    
    def get_team_info_by_id(self, team_id: int) -> List[TeamInfoData]:
        return session.query(TeamInfoData).filter(TeamInfoData.id == team_id).one()
