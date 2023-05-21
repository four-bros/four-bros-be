from typing import List
from src.constants import session
from src.data_models.TeamInfoData import TeamInfoData
from src.schemas.Teams import teams_details_schema

def get_all_rankings():
    coachs_poll_data: List[TeamInfoData] = session.query(TeamInfoData).where(
        TeamInfoData.coachs_poll_points > 0
    ).order_by(
        TeamInfoData.coachs_poll_rank
    ).all()

    media_poll_data: List[TeamInfoData] = session.query(TeamInfoData).where(
        TeamInfoData.media_poll_points > 0
    ).order_by(
        TeamInfoData.media_poll_rank
    ).all()

    bcs_data: List[TeamInfoData] = session.query(TeamInfoData).order_by(
        TeamInfoData.bcs_rank
    ).limit(10)

    # convert data to json
    coachs_poll = teams_details_schema.dump(coachs_poll_data)
    medial_poll = teams_details_schema.dump(media_poll_data)
    bcs_poll = teams_details_schema.dump(bcs_data)

    response = {
        'coachs_poll': coachs_poll,
        'media_poll': medial_poll,
        'bcs': bcs_poll
    }

    return response
