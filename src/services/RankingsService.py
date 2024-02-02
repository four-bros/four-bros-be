from typing import List
from src.data_services.TeamInfoDataService import TeamInfoDataService
from src.data_services.WeekYearDataService import WeekYearDataService
from src.data_models.TeamInfoData import TeamInfoData
from src.schemas.Teams import teams_details_schema

class RankingsService():
    def __init__(self) -> None:
        self.TeamInfoDataService = TeamInfoDataService()
        self.WeekYearDataService = WeekYearDataService()

    def get_all_rankings(self):
        coachs_poll_data: List[TeamInfoData] = self.TeamInfoDataService.get_coachs_poll_data()
        media_poll_data: List[TeamInfoData] = self.TeamInfoDataService.get_media_poll_data()
        bcs_data: List[TeamInfoData] = self.TeamInfoDataService.get_bcs_poll_data()

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
