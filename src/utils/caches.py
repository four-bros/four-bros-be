from src.constants import session
from src.data_models.Records import Records


def _get_player_career_records_cache():

	player_career_records_data: Records = session.query(Records).where(
		Records.record_type == 'player_career'
	).scalar()

	return player_career_records_data.record


def _get_player_game_records_cache():

	player_game_records_data: Records = session.query(Records).where(
		Records.record_type == 'player_game'
	).scalar()

	return player_game_records_data.record


def _get_player_season_records_cache():

	player_season_records_data: Records = session.query(Records).where(
		Records.record_type == 'player_season'
	).scalar()

	return player_season_records_data.record
