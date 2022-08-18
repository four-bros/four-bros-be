import time
from typing import List
from uuid import uuid4

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

		player.pass_rating=pass_rating
	
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


def update_ky_ky_data():

	kyle_data: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
		SeasonOffensiveStatsData.player_id == '7172KyleBlake',
		SeasonOffensiveStatsData.year == 2026
	).scalar()

	ky_ky_data: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
		SeasonOffensiveStatsData.player_id == '7172Ky KyBlake',
		SeasonOffensiveStatsData.year == 2026
	).scalar()

	new_id = str(uuid4())

	longest_rec = max([ky_ky_data.longest_rec, kyle_data.longest_rec])
	longest_run = max([ky_ky_data.longest_run, kyle_data.longest_run])
	receptions = ky_ky_data.receptions - kyle_data.receptions
	rec_yards = ky_ky_data.rec_yards - kyle_data.rec_yards
	rush_yards = ky_ky_data.rush_yards - kyle_data.rush_yards
	yac = ky_ky_data.yac - kyle_data.yac
	rec_tds = ky_ky_data.rec_tds - kyle_data.rec_tds
	rush_tds = ky_ky_data.rush_tds - kyle_data.rush_tds
	ya_contact = ky_ky_data.ya_contact - kyle_data.ya_contact
	drops = ky_ky_data.drops - kyle_data.drops
	rush_att = ky_ky_data.rush_att - kyle_data.rush_att
	broke_tkls = ky_ky_data.broke_tkls - kyle_data.broke_tkls
	fumbles = ky_ky_data.fumbles - kyle_data.fumbles
	twenty_plus_yd_runs = ky_ky_data.twenty_plus_yd_runs - kyle_data.twenty_plus_yd_runs
	total_yards = ky_ky_data.total_yards - kyle_data.total_yards
	total_tds = ky_ky_data.total_tds - kyle_data.total_tds
	rush_ypc = round(rush_yards / rush_att, 1)
	rec_ypc = round(rec_yards / receptions, 1)
	turnovers = ky_ky_data.turnovers - kyle_data.turnovers


	ky_ky_game_data: GameOffensiveStatsData = GameOffensiveStatsData(
		id=new_id,
		player_id=ky_ky_data.player_id,
		week=22,
		year=2026,
		pass_yards=0,
        longest_rec=longest_rec,
        longest_pass=0,
        longest_run=longest_run,
        receptions=receptions,
        sacked=0,
        rec_yards=rec_yards,
        rush_yards=rush_yards,
        yac=yac,
        pass_tds=0,
        rec_tds=rec_tds,
        rush_tds=rush_tds,
        ya_contact=ya_contact,
        completions=0,
        ints=0,
        drops=drops,
        pass_att=0,
        rush_att=rush_att,
        broke_tkls=broke_tkls,
        fumbles=fumbles,
        twenty_plus_yd_runs=twenty_plus_yd_runs,
        total_yards=total_yards,
        total_tds=total_tds,
        pass_ypa=0,
        rush_ypc=rush_ypc,
        rec_ypc=rec_ypc,
        pass_rating=0,
        turnovers=turnovers,
        comp_pct=0
	)

	try:
		session.add(ky_ky_game_data)
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()


def add_game_data_from_old_player():

	kyle_data: GameOffensiveStatsData = session.query(GameOffensiveStatsData).where(
		GameOffensiveStatsData.player_id == '7172KyleBlake',
		GameOffensiveStatsData.year == 2025
	).all()

	ky_ky_games: List[GameOffensiveStatsData] = []

	for game in kyle_data:

		new_id = str(uuid4())

		ky_ky_game_data: GameOffensiveStatsData = GameOffensiveStatsData(
			id=new_id,
			player_id='7172Ky KyBlake',
			week=game.week,
			year=game.year,
			pass_yards=game.pass_yards,
	        longest_rec=game.longest_rec,
	        longest_pass=game.longest_pass,
	        longest_run=game.longest_run,
	        receptions=game.receptions,
	        sacked=game.sacked,
	        rec_yards=game.rec_yards,
	        rush_yards=game.rush_yards,
	        yac=game.yac,
	        pass_tds=game.pass_tds,
	        rec_tds=game.rec_tds,
	        rush_tds=game.rush_tds,
	        ya_contact=game.ya_contact,
	        completions=game.completions,
	        ints=game.ints,
	        drops=game.drops,
	        pass_att=game.pass_att,
	        rush_att=game.rush_att,
	        broke_tkls=game.broke_tkls,
	        fumbles=game.fumbles,
	        twenty_plus_yd_runs=game.twenty_plus_yd_runs,
	        total_yards=game.total_yards,
	        total_tds=game.total_tds,
	        pass_ypa=game.pass_ypa,
	        rush_ypc=game.rush_ypc,
	        rec_ypc=game.rec_ypc,
	        pass_rating=game.pass_rating,
	        turnovers=game.turnovers,
	        comp_pct=game.comp_pct
		)

		ky_ky_games.append(ky_ky_game_data)

	try:
		session.add_all(ky_ky_games)
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()


def add_season_data_from_old_player():

	rickey_williams_data: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
		SeasonOffensiveStatsData.player_id == '835RickeyWilliams',
		SeasonOffensiveStatsData.year == 2033
	).scalar()


	new_id = str(uuid4())

	scoot_season_data: SeasonOffensiveStatsData = SeasonOffensiveStatsData(
		id=new_id,
		player_id='835ScootWilliams',
		year=rickey_williams_data.year,
		games_played=rickey_williams_data.games_played,
		pass_yards=rickey_williams_data.pass_yards,
        longest_rec=rickey_williams_data.longest_rec,
        longest_pass=rickey_williams_data.longest_pass,
        longest_run=rickey_williams_data.longest_run,
        receptions=rickey_williams_data.receptions,
        sacked=rickey_williams_data.sacked,
        rec_yards=rickey_williams_data.rec_yards,
        rush_yards=rickey_williams_data.rush_yards,
        yac=rickey_williams_data.yac,
        pass_tds=rickey_williams_data.pass_tds,
        rec_tds=rickey_williams_data.rec_tds,
        rush_tds=rickey_williams_data.rush_tds,
        ya_contact=rickey_williams_data.ya_contact,
        completions=rickey_williams_data.completions,
        ints=rickey_williams_data.ints,
        drops=rickey_williams_data.drops,
        pass_att=rickey_williams_data.pass_att,
        rush_att=rickey_williams_data.rush_att,
        broke_tkls=rickey_williams_data.broke_tkls,
        fumbles=rickey_williams_data.fumbles,
        twenty_plus_yd_runs=rickey_williams_data.twenty_plus_yd_runs,
        total_yards=rickey_williams_data.total_yards,
        total_tds=rickey_williams_data.total_tds,
        pass_ypa=rickey_williams_data.pass_ypa,
        rush_ypc=rickey_williams_data.rush_ypc,
        rec_ypc=rickey_williams_data.rec_ypc,
        pass_rating=rickey_williams_data.pass_rating,
        turnovers=rickey_williams_data.turnovers,
        comp_pct=rickey_williams_data.comp_pct,
		pass_ypg=rickey_williams_data.pass_ypg,
		rush_ypg=rickey_williams_data.rush_ypg,
		rec_ypg=rickey_williams_data.rec_ypg,
		total_ypg=rickey_williams_data.total_ypg
	)

	try:
		session.add(scoot_season_data)
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()


# update_career_pass_rating()
# update_game_pass_rating()
# update_season_pass_rating()
add_game_data_from_old_player()
