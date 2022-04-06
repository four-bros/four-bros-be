from typing import List

from src.constants import coach_season_record_schema
from src.data_models.CoachInfoData import CoachInfoData
from src.data_models.CoachStatsData import CoachStatsData
from src.models.Coach import CoachSeasonRecord


def _get_coach_season_records(coach_info: List[CoachInfoData], coach_stats: List[CoachStatsData]):

    coach_data = {}

    coach_data['name'] = f'{coach_info[0].first_name} {coach_info[0].last_name}'
    coach_data['wins'] = sum([year.wins for year in coach_stats])
    coach_data['losses'] = sum([year.losses for year in coach_stats])
    coach_data['titles'] = sum([1 for year in coach_stats if year.national_title])
    coach_data['season_records'] = []

    for i, value in enumerate(coach_info):
        season_record: CoachSeasonRecord = CoachSeasonRecord(
            team_id=coach_info[i].team_id,
            team_name=coach_info[i].team_name,
            year=coach_info[i].year,
            wins=coach_stats[i].wins,
            losses=coach_stats[i].losses,
            national_title=coach_stats[i].national_title
        )
        season_record_json = coach_season_record_schema.dump(season_record)

        coach_data['season_records'].append(season_record_json)

    return coach_data