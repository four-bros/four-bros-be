from typing import List
from src.constants import session
from src.data_models.TeamInfoData import TeamInfoData

class TeamInfoDataService():
    def get_users_team_info() -> List[TeamInfoData]:
        return session.query(TeamInfoData).where(TeamInfoData.is_user).order_by(
        TeamInfoData.team_name
        ).all()
