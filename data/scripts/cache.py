import time
from src.blueprints.view_methods.records import (
	get_career_records,
	get_game_records,
	get_season_records
)
from src.constants import session
from src.data_models.Records import Records


async def cache_player_career_records():

	start_time = time.time()
	print('Starting career records cache.')

	career_records = get_career_records('request')

	career_record: Records = Records(
		id=1,
		record_type='player_career',
		record=career_records
	)

	career_records_query = session.query(Records).where(
		Records.record_type == 'player_career'
	).scalar()

	if not career_records_query:
		session.add(career_record)
	
	else:
		career_records_query.record=career_record.record
	
	try:
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Career records cache took {(round(execution_time, 2))} seconds to complete.')


async def cache_player_game_records():

	start_time = time.time()
	print('Starting game records cache.')

	game_records = get_game_records('request')

	game_record: Records = Records(
		id=2,
		record_type='player_game',
		record=game_records
	)

	game_records_query = session.query(Records).where(
		Records.record_type == 'player_game'
	).scalar()

	if not game_records_query:
		session.add(game_record)
	
	else:
		game_records_query.record=game_record.record
	
	try:
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Game records cache took {(round(execution_time, 2))} seconds to complete.')


async def cache_player_season_records():

	start_time = time.time()
	print('Starting season records cache.')

	season_records = get_season_records('request')

	season_record: Records = Records(
		id=3,
		record_type='player_season',
		record=season_records
	)

	season_records_query = session.query(Records).where(
		Records.record_type == 'player_season'
	).scalar()

	if not season_records_query:
		session.add(season_record)
	
	else:
		season_records_query.record=season_record.record
	
	try:
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Season records cache took {(round(execution_time, 2))} seconds to complete.')
