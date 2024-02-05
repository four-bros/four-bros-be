from typing import List
from sqlalchemy import desc
from src.constants import session
from src.data_models.TeamInfoData import TeamInfoData

class TeamInfoDataService():
    def __init__(self) -> None:
        pass

    def get_all_teams(self) -> List[TeamInfoData]:
        return session.query(TeamInfoData).order_by(
            desc(TeamInfoData.is_user),
            TeamInfoData.team_name
        ).all()

    def get_users_team_info(self) -> List[TeamInfoData]:
        return session.query(TeamInfoData).where(TeamInfoData.is_user).order_by(
        TeamInfoData.team_name
        ).all()
    
    def get_team_info_by_id(self, team_id: int) -> List[TeamInfoData]:
        return session.query(TeamInfoData).filter(TeamInfoData.id == team_id).one()

    def get_coachs_poll_data(self) -> List[TeamInfoData]:
        return session.query(TeamInfoData).where(
            TeamInfoData.coachs_poll_points > 0
        ).order_by(
            TeamInfoData.coachs_poll_rank
        ).all()
    
    def get_media_poll_data(self) -> List[TeamInfoData]:
        return session.query(TeamInfoData).where(
            TeamInfoData.media_poll_points > 0
        ).order_by(
            TeamInfoData.media_poll_rank
        ).all()

    def get_bcs_poll_data(self) -> List[TeamInfoData]:
        return session.query(TeamInfoData).order_by(
            TeamInfoData.bcs_rank
        ).limit(10)
