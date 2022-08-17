import time
from src.constants import session
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.GameOffensiveStatsData import GameOffensiveStatsData
from src.utils.calcs import calculate_pass_rating
from src.data_models.CareerOffensiveStatsData import CareerOffensiveStatsData


def update_career_pass_rating() -> None:

	start_time = time.time()
	print('Starting update career pass rating script')

	player_query: CareerOffensiveStatsData = session.query(CareerOffensiveStatsData).where(
            CareerOffensiveStatsData.pass_att > 0).all()
	
	print(f'There are {len(player_query)} career passers')

	for player in player_query:

		player_info: PlayerInfoData = session.query(PlayerInfoData).where(
			player.player_id == PlayerInfoData.id
		).scalar()

		pass_rating = calculate_pass_rating(
			pass_att=player.pass_att,
			pass_yds=player.pass_yards,
			pass_tds=player.pass_tds,
			completions=player.completions,
			ints=player.ints
		)

		player.pass_rating=pass_rating
	
	try:
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Update career pass ratings script took {(round(execution_time, 2))} seconds to complete.')


def update_game_pass_rating() -> None:

	start_time = time.time()
	print('Starting update game pass rating script')

	player_query: GameOffensiveStatsData = session.query(GameOffensiveStatsData).where(
            GameOffensiveStatsData.pass_att > 0).all()
	
	print(f'There are {len(player_query)} game passers')

	for player in player_query:

		player_info: PlayerInfoData = session.query(PlayerInfoData).where(
			player.player_id == PlayerInfoData.id
		).scalar()

		pass_rating = calculate_pass_rating(
			pass_att=player.pass_att,
			pass_yds=player.pass_yards,
			pass_tds=player.pass_tds,
			completions=player.completions,
			ints=player.ints
		)

		update(GameOffensiveStatsData).where(GameOffensiveStatsData.player_id == player_info.id).values(pass_rating=pass_rating)
	
	try:
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Update game pass ratings script took {(round(execution_time, 2))} seconds to complete.')


def update_season_pass_rating() -> None:

	start_time = time.time()
	print('Starting update season pass rating script')

	player_query: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.pass_att > 0).all()
	
	print(f'There are {len(player_query)} season passers')
	
	for player in player_query:

		player_info: PlayerInfoData = session.query(PlayerInfoData).where(
			player.player_id == PlayerInfoData.id
		).scalar()

		pass_rating = calculate_pass_rating(
			pass_att=player.pass_att,
			pass_yds=player.pass_yards,
			pass_tds=player.pass_tds,
			completions=player.completions,
			ints=player.ints
		)

		player.pass_rating=pass_rating
	
	try:
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Update season pass ratings script took {(round(execution_time, 2))} seconds to complete.')


# update_career_pass_rating()
# update_game_pass_rating()
# update_season_pass_rating()
