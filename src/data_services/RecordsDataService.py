from src.constants import session
from src.data_models.Records import Records


class RecordsDataService():
    def __init__(self) -> None:
        pass

    def get_player_of_the_week_cache(self):
        player_career_records_data: Records = session.query(Records).where(
            Records.record_type == 'player_of_the_week'
        ).scalar()

        return player_career_records_data.record

    def get_player_game_records_cache(self):
        player_game_records_data: Records = session.query(Records).where(
            Records.record_type == 'player_game'
        ).scalar()

        return player_game_records_data.record

    def get_player_season_records_cache(self):
        player_season_records_data: Records = session.query(Records).where(
            Records.record_type == 'player_season'
        ).scalar()

        return player_season_records_data.record

    def get_team_game_records_cache(self):
        team_game_records_data: Records = session.query(Records).where(
            Records.record_type == 'team_game'
        ).scalar()

        return team_game_records_data.record

    def get_team_season_records_cache(self):
        team_season_records_data: Records = session.query(Records).where(
            Records.record_type == 'team_season'
        ).scalar()

        return team_season_records_data.record
