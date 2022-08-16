import asyncio
from typing import List
from uuid import uuid4
import time
from sqlalchemy import desc

from src.constants import session
from src.utils.helpers import _convert_stats_year
from src.data_models.GameDefensiveStatsData import GameDefensiveStatsData
from src.data_models.GameKickingStatsData import GameKickingStatsData
from src.data_models.GameOffensiveStatsData import GameOffensiveStatsData
from src.data_models.GameReturnStatsData import GameReturnStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData


async def insert_game_def_stats_into_db(week_year_data, def_stats):

	start_time = time.time()
	print('Starting insert Game Defensive Stats script.')

	week_year = week_year_data[0]
	current_week = week_year.fields['Week']
	current_year = _convert_stats_year(week_year.fields['Year'])
	all_game_def_stats: List[GameDefensiveStatsData] = []


	for i, value in enumerate(def_stats):

		def_record = def_stats[i]

		# skip over players in dictionary from other years
		if _convert_stats_year(def_record.fields['Year']) != current_year:
			continue

		player_info: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == def_record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

		if not player_info:
			continue

		player_id: str = str(def_record.fields['Player ID']) + player_info.first_name + player_info.last_name

		prior_def_stats: SeasonDefensiveStatsData = session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == player_id,
            SeasonDefensiveStatsData.year == current_year
        ).scalar()

		new_id = str(uuid4())
		half_a_sack = round(def_record.fields['Half A Sack'] / 2, 1)

		current_def_stats: SeasonDefensiveStatsData = SeasonDefensiveStatsData(
			id=new_id,
            player_id=player_id,
			total_tkls = def_record.fields['Solo Tkls'] + def_record.fields['Asst. Tkls'],
			half_a_sack = half_a_sack,
			total_sacks = half_a_sack + def_record.fields['Sacks'],
			long_int_ret = def_record.fields['Long INT Ret'],
			sacks = def_record.fields['Sacks'],
			year = current_year,
			forced_fumbles = def_record.fields['Forced Fumbles'],
			solo_tkls = def_record.fields['Solo Tkls'],
			safeties = def_record.fields['Safties'],
			pass_def = def_record.fields['Pass Def.'],
			blocked_kicks = def_record.fields['Blocked Kicks'],
			tfl = def_record.fields['TFL'],
			ints_made = def_record.fields['INTs Made'],
			games_played = def_record.fields['Games Played'],
			fumbles_rec = def_record.fields['Fumbles Rec.'],
			asst_tkls = def_record.fields['Asst. Tkls'],
			def_tds = def_record.fields['Def. TDs'],
			fum_rec_yards = def_record.fields['Fum. Rec. Yards'],
			int_ret_yards = def_record.fields['INT Ret. Yards'],
		)
        

		if prior_def_stats:

			long_int_ret = current_def_stats.long_int_ret - prior_def_stats.long_int_ret
			sacks = current_def_stats.sacks - prior_def_stats.sacks
			forced_fumbles = current_def_stats.forced_fumbles - prior_def_stats.forced_fumbles
			solo_tkls = current_def_stats.solo_tkls - prior_def_stats.solo_tkls
			safeties = current_def_stats.safeties - prior_def_stats.safeties
			pass_def = current_def_stats.pass_def - prior_def_stats.pass_def
			blocked_kicks = current_def_stats.blocked_kicks - prior_def_stats.blocked_kicks
			tfl = current_def_stats.tfl - prior_def_stats.tfl
			ints_made = current_def_stats.ints_made - prior_def_stats.ints_made
			fumbles_rec = current_def_stats.fumbles_rec - prior_def_stats.fumbles_rec
			half_a_sack = current_def_stats.half_a_sack - prior_def_stats.half_a_sack
			asst_tkls = current_def_stats.asst_tkls - prior_def_stats.asst_tkls
			def_tds = current_def_stats.def_tds - prior_def_stats.def_tds
			fum_rec_yards = current_def_stats.fum_rec_yards - prior_def_stats.fum_rec_yards
			int_ret_yards = current_def_stats.int_ret_yards - prior_def_stats.int_ret_yards
			total_tkls = current_def_stats.total_tkls - prior_def_stats.total_tkls
			total_sacks = current_def_stats.total_sacks - prior_def_stats.total_sacks

			game_stats: GameDefensiveStatsData = GameDefensiveStatsData(
				id=new_id,
                player_id=player_id,
                week=current_week,
                year=current_year,
                games_played=1,
                long_int_ret=long_int_ret,
                sacks=sacks,
                forced_fumbles=forced_fumbles,
                solo_tkls=solo_tkls,
                safeties=safeties,
                pass_def=pass_def,
                blocked_kicks=blocked_kicks,
                tfl=tfl,
                ints_made=ints_made,
                fumbles_rec=fumbles_rec,
                half_a_sack=half_a_sack,
                asst_tkls=asst_tkls,
                def_tds=def_tds,
                fum_rec_yards=fum_rec_yards,
                int_ret_yards=int_ret_yards,
                total_tkls=total_tkls,
                total_sacks=total_sacks
			)

			all_game_def_stats.append(game_stats)

		else:

			game_stats: GameDefensiveStatsData = GameDefensiveStatsData(
		        id=new_id,
		        player_id=player_id,
		        week=current_week,
		        year=current_year,
		        games_played=1,
		        long_int_ret=current_def_stats.long_int_ret,
		        sacks=current_def_stats.sacks,
		        forced_fumbles=current_def_stats.forced_fumbles,
		        solo_tkls=current_def_stats.solo_tkls,
		        safeties=current_def_stats.safeties,
		        pass_def=current_def_stats.pass_def,
		        blocked_kicks=current_def_stats.blocked_kicks,
		        tfl=current_def_stats.tfl,
		        ints_made=current_def_stats.ints_made,
		        fumbles_rec=current_def_stats.fumbles_rec,
		        half_a_sack=current_def_stats.half_a_sack,
		        asst_tkls=current_def_stats.asst_tkls,
		        def_tds=current_def_stats.def_tds,
		        fum_rec_yards=current_def_stats.fum_rec_yards,
		        int_ret_yards=current_def_stats.int_ret_yards,
		        total_tkls=current_def_stats.total_tkls,
		        total_sacks=current_def_stats.total_sacks
		    )
			
			all_game_def_stats.append(game_stats)

	try:
		session.add_all(all_game_def_stats)
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Insert Game Defensive Stats script took {(round(execution_time, 2))} seconds to complete.')	


async def insert_game_kicking_stats_into_db(week_year_data, kick_stats):
	
	start_time = time.time()
	print('Starting insert Game Kicking Stats script.')

	week_year = week_year_data[0]
	current_week = week_year.fields['Week']
	current_year = _convert_stats_year(week_year.fields['Year'])
	all_game_kick_stats: List[GameKickingStatsData] = []

	for i, value in enumerate(kick_stats):

		kick_record = kick_stats[i]

		# skip over players in dictionary from other years
		if _convert_stats_year(kick_record.fields['Year']) != current_year:
			continue

		player_info: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == kick_record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

		if not player_info:
			continue

		player_id: str = str(kick_record.fields['Player ID']) + player_info.first_name + player_info.last_name

		prior_kicking_stats: SeasonKickingStatsData = session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == player_id,
            SeasonKickingStatsData.year == current_year
        ).scalar()

		new_id = str(uuid4())

		fg_pct = round(
            kick_record.fields['FG Made'] / kick_record.fields['FG Att.'] * 100\
                if kick_record.fields['FG Att.'] != 0 else 0,
            1)
		xp_pct = round(
			kick_record.fields['XP Made'] / kick_record.fields['XP Att.'] * 100\
		    if kick_record.fields['XP Att.'] != 0 else 0,
		1)
		fg_50_plus_pct = round(
			kick_record.fields['FG Made 50+'] / kick_record.fields['FG Att. 50+'] * 100\
		    if kick_record.fields['FG Att. 50+'] != 0 else 0,
		1)
		punt_avg = round(
			kick_record.fields['Total Punt Yards'] / kick_record.fields['# Punts']\
		    if kick_record.fields['# Punts'] != 0 else 0, 
		1)
		net_avg = round(
			kick_record.fields['Net Punting'] / kick_record.fields['# Punts']\
		    if kick_record.fields['# Punts'] != 0 else 0, 
		1)
		
		current_kicking_stats = SeasonKickingStatsData(
            id=new_id,
            player_id=player_id,
            fg_made_17_29=kick_record.fields['FG Made 17-29'],
            fg_att_17_29=kick_record.fields['FG Att. 17-29'],
            long_fg=kick_record.fields['Long FG'],
            ko_touchbacks=kick_record.fields['KO Touchbacks'],
            long_punt=kick_record.fields['Long Punt'],
            xp_att=kick_record.fields['XP Att.'],
            year=current_year,
            punts_blocked=kick_record.fields['Punts Blocked'],
            fg_att=kick_record.fields['FG Att.'],
            total_punt_yards=kick_record.fields['Total Punt Yards'],
            xp_blocked=kick_record.fields['XP Blocked'],
            fg_blocked=kick_record.fields['FG Blocked'],
            fg_att_40_49=kick_record.fields['FG Att. 40-49'],
            fg_made_40_49=kick_record.fields['FG Made 40-49'],
            fg_att_30_39=kick_record.fields['FG Att. 30-39'],
            fg_made_30_39=kick_record.fields['FG Att. 30-39'],
            fg_att_50_plus=kick_record.fields['FG Att. 50+'],
            fg_made_50_plus=kick_record.fields['FG Made 50+'],
            punt_touchbacks=kick_record.fields['Punt Touchbacks'],
            games_played=kick_record.fields['Games Played'],
            kickoffs=kick_record.fields['Kickoffs'],
            xp_made=kick_record.fields['XP Made'],
            net_punting=kick_record.fields['Net Punting'],
            fg_made=kick_record.fields['FG Made'],
            number_punts=kick_record.fields['# Punts'],
            inside_twenty=kick_record.fields['Inside 20'],
            fg_pct=fg_pct,
            xp_pct=xp_pct,
            fg_50_plus_pct=fg_50_plus_pct,
            punt_avg=punt_avg,
            net_avg=net_avg
        )


		if not prior_kicking_stats:
			
			game_stats: GameKickingStatsData = GameKickingStatsData(
                id=new_id,
                player_id=player_id,
                week=current_week,
                year=current_year,
                games_played=1,
                fg_made_17_29=current_kicking_stats.fg_made_17_29,
                fg_att_17_29=current_kicking_stats.fg_att_17_29,
                long_fg=current_kicking_stats.long_fg,
                ko_touchbacks=current_kicking_stats.ko_touchbacks,
                long_punt=current_kicking_stats.long_punt,
                xp_att=current_kicking_stats.xp_att,
                punts_blocked=current_kicking_stats.punts_blocked,
                fg_att=current_kicking_stats.fg_att,
                total_punt_yards=current_kicking_stats.total_punt_yards,
                xp_blocked=current_kicking_stats.xp_blocked,
                fg_blocked=current_kicking_stats.fg_blocked,
                fg_att_40_49=current_kicking_stats.fg_att_40_49,
                fg_made_40_49=current_kicking_stats.fg_made_40_49,
                fg_att_30_39=current_kicking_stats.fg_att_30_39,
                fg_made_30_39=current_kicking_stats.fg_made_30_39,
                fg_att_50_plus=current_kicking_stats.fg_att_50_plus,
                fg_made_50_plus=current_kicking_stats.fg_made_50_plus,
                punt_touchbacks=current_kicking_stats.punt_touchbacks,
                kickoffs=current_kicking_stats.kickoffs,
                xp_made=current_kicking_stats.xp_made,
                net_punting=current_kicking_stats.net_punting,
                fg_made=current_kicking_stats.fg_made,
                number_punts=current_kicking_stats.number_punts,
                inside_twenty=current_kicking_stats.inside_twenty,
                fg_pct=current_kicking_stats.fg_pct,
                xp_pct=current_kicking_stats.xp_pct,
                fg_50_plus_pct=current_kicking_stats.fg_50_plus_pct,
                punt_avg=current_kicking_stats.punt_avg
            )

			all_game_kick_stats.append(game_stats)

		else:

			fg_made_17_29 = current_kicking_stats.fg_made_17_29 - prior_kicking_stats.fg_made_17_29
			fg_att_17_29 = current_kicking_stats.fg_att_17_29 - prior_kicking_stats.fg_att_17_29
			long_fg = current_kicking_stats.long_fg - prior_kicking_stats.long_fg
			ko_touchbacks = current_kicking_stats.ko_touchbacks - prior_kicking_stats.ko_touchbacks
			long_punt = current_kicking_stats.long_punt - prior_kicking_stats.long_punt
			xp_att = current_kicking_stats.xp_att - prior_kicking_stats.xp_att
			punts_blocked = current_kicking_stats.punts_blocked - prior_kicking_stats.punts_blocked
			fg_att = current_kicking_stats.fg_att - prior_kicking_stats.fg_att
			total_punt_yards = current_kicking_stats.total_punt_yards - prior_kicking_stats.total_punt_yards
			xp_blocked = current_kicking_stats.xp_blocked - prior_kicking_stats.xp_blocked
			fg_blocked = current_kicking_stats.fg_blocked - prior_kicking_stats.fg_blocked
			fg_att_40_49 = current_kicking_stats.fg_att_40_49 - prior_kicking_stats.fg_att_40_49
			fg_made_40_49 = current_kicking_stats.fg_made_40_49 - prior_kicking_stats.fg_made_40_49
			fg_att_30_39 = current_kicking_stats.fg_att_30_39 - prior_kicking_stats.fg_att_30_39
			fg_made_30_39 = current_kicking_stats.fg_made_30_39 - prior_kicking_stats.fg_made_30_39
			fg_att_50_plus = current_kicking_stats.fg_att_50_plus - prior_kicking_stats.fg_att_50_plus
			fg_made_50_plus = current_kicking_stats.fg_made_50_plus - prior_kicking_stats.fg_made_50_plus
			punt_touchbacks = current_kicking_stats.punt_touchbacks - prior_kicking_stats.punt_touchbacks
			kickoffs = current_kicking_stats.kickoffs - prior_kicking_stats.kickoffs
			xp_made = current_kicking_stats.xp_made - prior_kicking_stats.xp_made
			net_punting = current_kicking_stats.net_punting - prior_kicking_stats.net_punting
			fg_made = current_kicking_stats.fg_made - prior_kicking_stats.fg_made
			number_punts = current_kicking_stats.number_punts - prior_kicking_stats.number_punts
			inside_twenty = current_kicking_stats.inside_twenty - prior_kicking_stats.inside_twenty
			fg_pct = round(
			    0 if fg_att == 0 else \
			        fg_made / fg_att, 1
			)
			xp_pct = round(
			    0 if xp_att == 0 else \
			        xp_made / xp_att, 1
			)
			fg_50_plus_pct = round(
			    0 if fg_att_50_plus == 0 else \
			        fg_made_50_plus / fg_att_50_plus, 1
			)
			punt_avg = round(
			    0 if number_punts == 0 else \
			        total_punt_yards / number_punts, 1
			)

			game_stats = GameKickingStatsData(
			    id=new_id,
			    player_id=player_id,
			    week=current_week,
			    year=current_year,
			    games_played=1,
			    fg_made_17_29=fg_made_17_29,
			    fg_att_17_29=fg_att_17_29,
			    long_fg=long_fg,
			    ko_touchbacks=ko_touchbacks,
			    long_punt=long_punt,
			    xp_att=xp_att,
			    punts_blocked=punts_blocked,
			    fg_att=fg_att,
			    total_punt_yards=total_punt_yards,
			    xp_blocked=xp_blocked,
			    fg_blocked=fg_blocked,
			    fg_att_40_49=fg_att_40_49,
			    fg_made_40_49=fg_made_40_49,
			    fg_att_30_39=fg_att_30_39,
			    fg_made_30_39=fg_made_30_39,
			    fg_att_50_plus=fg_att_50_plus,
			    fg_made_50_plus=fg_made_50_plus,
			    punt_touchbacks=punt_touchbacks,
			    kickoffs=kickoffs,
			    xp_made=xp_made,
			    net_punting=net_punting,
			    fg_made=fg_made,
			    number_punts=number_punts,
			    inside_twenty=inside_twenty,
			    fg_pct=fg_pct,
			    xp_pct=xp_pct,
			    fg_50_plus_pct=fg_50_plus_pct,
			    punt_avg=punt_avg
			)

			all_game_kick_stats.append(game_stats)

	try:
		session.add_all(all_game_kick_stats)
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Insert Game Kicking Stats script took {(round(execution_time, 2))} seconds to complete.')	


async def insert_game_off_stats_into_db(week_year_data, off_stats):

	start_time = time.time()
	print('Starting insert Game Offensive Stats script.')

	week_year = week_year_data[0]
	current_week: int = week_year.fields['Week']
	current_year: int = _convert_stats_year(week_year.fields['Year'])
	all_game_off_stats: List[GameOffensiveStatsData] = []

	for i, value in enumerate(off_stats):

		offensive_record = off_stats[i]

		# skip over players in dictionary from other years
		if _convert_stats_year(offensive_record.fields['Year']) != current_year:
			continue

		player_info: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == offensive_record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

		if not player_info:
			continue

		player_id: str = str(offensive_record.fields['Player ID']) + player_info.first_name + player_info.last_name

		prior_off_stats: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player_id,
            SeasonOffensiveStatsData.year == current_year
        ).scalar()

		new_id = str(uuid4())

		# Offensive Stats calculations
		comp_pct = round(
		    offensive_record.fields['Completions'] / offensive_record.fields['Pass Att.'] * 100\
		        if offensive_record.fields['Pass Att.'] != 0 else 0,
		        1
		    )
		pass_ypa = round(
		    offensive_record.fields['Pass. Yards'] / offensive_record.fields['Pass Att.']\
		        if offensive_record.fields['Pass Att.'] != 0 else 0,
		        1
		    )
		pass_ypg = round(
		    offensive_record.fields['Pass. Yards'] / offensive_record.fields['Games Played']\
		        if offensive_record.fields['Games Played'] != 0 else 0, 
		        1
		    )
		rush_ypc = round(
		    offensive_record.fields['Rush Yards'] / offensive_record.fields['Rush Att.']\
		        if offensive_record.fields['Rush Att.'] != 0 else 0,
		        1
		    )
		rush_ypg = round(
		    offensive_record.fields['Rush Yards'] / offensive_record.fields['Games Played']\
		        if offensive_record.fields['Games Played'] != 0 else 0,
		        1
		    )
		rec_ypc = round(
		    offensive_record.fields['Rec. Yards'] / offensive_record.fields['Receptions']\
		        if offensive_record.fields['Receptions'] != 0 else 0,
		        1
		    )
		rec_ypg = round(
		    offensive_record.fields['Rec. Yards'] / offensive_record.fields['Games Played']\
		        if offensive_record.fields['Games Played'] != 0 else 0,
		        1
		    )
		pass_rating_calc = (
		    0 if offensive_record.fields['Pass Att.'] == 0 else \
		    ((8.4 * offensive_record.fields['Pass. Yards']) + (330 * offensive_record.fields['Pass. TDs']) + \
		    (100 * offensive_record.fields['Completions']) - (200 * offensive_record.fields['INTs'])) / offensive_record.fields['Pass Att.']
		    )
		pass_rating = round(pass_rating_calc, 1)

		turnovers = offensive_record.fields['INTs'] + offensive_record.fields['Fumbles']

		# get ReturnStats for total stats purposes (yards, TDs, etc)
		return_stats: GameReturnStatsData = session.query(GameReturnStatsData).where(
		    GameReturnStatsData.player_id == player_id,
		    GameReturnStatsData.year == current_year,
			GameReturnStatsData.week == current_week
		).scalar()

		# Calculate total stats
		total_yards = 0
		total_tds = 0
		total_ypg = 0

		if return_stats:
			total_yards = sum([
		        offensive_record.fields['Pass. Yards'], offensive_record.fields['Rec. Yards'], offensive_record.fields['Rush Yards'], 
		        return_stats.kr_yds, return_stats.pr_yds]
		    )
			total_tds = sum([
				offensive_record.fields['Pass. TDs'], offensive_record.fields['Rec. TDs'], offensive_record.fields['Rush TDs'],
				return_stats.kr_tds, return_stats.pr_tds
			])
			total_ypg = round(
			    0 if offensive_record.fields['Games Played'] == 0\
		        else total_yards / offensive_record.fields['Games Played'],
			1)

		else:
			total_yards = sum([
		        offensive_record.fields['Pass. Yards'], offensive_record.fields['Rec. Yards'], offensive_record.fields['Rush Yards']
	        ])
			total_tds = sum([
			    offensive_record.fields['Pass. TDs'], offensive_record.fields['Rec. TDs'], offensive_record.fields['Rush TDs']
		    ])
			total_ypg = round(
			    0 if offensive_record.fields['Games Played'] == 0\
			        else total_yards / offensive_record.fields['Games Played'],
			    1)
		
		current_off_stats = SeasonOffensiveStatsData(
            id=new_id,
            player_id=player_id,
            pass_yards=offensive_record.fields['Pass. Yards'],
            longest_rec=offensive_record.fields['Longest Rec.'],
            longest_pass=offensive_record.fields['Longest Pass'],
            longest_run=offensive_record.fields['Longest Run'],
            year=current_year,
            receptions=offensive_record.fields['Receptions'],
            sacked=offensive_record.fields['Sacked'],
            rec_yards=offensive_record.fields['Rec. Yards'],
            rush_yards=offensive_record.fields['Rush Yards'],
            yac=offensive_record.fields['Y.A.C.'],
            pass_tds=offensive_record.fields['Pass. TDs'],
            games_played=offensive_record.fields['Games Played'],
            rec_tds=offensive_record.fields['Rec. TDs'],
            rush_tds=offensive_record.fields['Rush TDs'],
            ya_contact=offensive_record.fields['Y.A. Contact'],
            completions=offensive_record.fields['Completions'],
            ints=offensive_record.fields['INTs'],
            drops=offensive_record.fields['Drops'],
            pass_att=offensive_record.fields['Pass Att.'],
            rush_att=offensive_record.fields['Rush Att.'],
            broke_tkls=offensive_record.fields['Broke Tkls.'],
            fumbles=offensive_record.fields['Fumbles'],
            twenty_plus_yd_runs=offensive_record.fields['20+ yd. Runs'],
            pass_ypa=pass_ypa,
            pass_ypg=pass_ypg,
            rush_ypc=rush_ypc,
            rush_ypg=rush_ypg,
            rec_ypc=rec_ypc,
            rec_ypg=rec_ypg,
            pass_rating=pass_rating,
            total_yards=total_yards,
            total_tds=total_tds,
            total_ypg=total_ypg,
            turnovers=turnovers,
            comp_pct=comp_pct
        )

		if not prior_off_stats:

			game_stats: GameOffensiveStatsData = GameOffensiveStatsData(
                id = new_id,
                player_id=player_id,
                week=current_week,
                year=current_year,
                games_played=1,
                pass_yards=current_off_stats.pass_yards,
                longest_rec=current_off_stats.longest_rec,
                longest_pass=current_off_stats.longest_pass,
                longest_run=current_off_stats.longest_run,
                receptions=current_off_stats.receptions,
                sacked=current_off_stats.sacked,
                rec_yards=current_off_stats.rec_yards,
                rush_yards=current_off_stats.rush_yards,
                yac=current_off_stats.yac,
                pass_tds=current_off_stats.pass_tds,
                rec_tds=current_off_stats.rec_tds,
                rush_tds=current_off_stats.rush_tds,
                ya_contact=current_off_stats.ya_contact,
                completions=current_off_stats.completions,
                ints=current_off_stats.ints,
                drops=current_off_stats.drops,
                pass_att=current_off_stats.pass_att,
                rush_att=current_off_stats.rush_att,
                broke_tkls=current_off_stats.broke_tkls,
                fumbles=current_off_stats.fumbles,
                twenty_plus_yd_runs=current_off_stats.twenty_plus_yd_runs,
                total_yards=current_off_stats.total_yards,
                total_tds=current_off_stats.total_tds,
                pass_ypa=current_off_stats.pass_ypa,
                rush_ypc=current_off_stats.rush_ypc,
                rec_ypc=current_off_stats.rec_ypc,
                pass_rating=current_off_stats.pass_rating,
                turnovers=turnovers,
                comp_pct=current_off_stats.comp_pct
            )

			all_game_off_stats.append(game_stats)

		else:

			pass_yards = current_off_stats.pass_yards - prior_off_stats.pass_yards
			longest_rec = current_off_stats.longest_rec - prior_off_stats.longest_rec
			longest_pass = current_off_stats.longest_pass - prior_off_stats.longest_pass
			longest_run = current_off_stats.longest_run - prior_off_stats.longest_run
			receptions = current_off_stats.receptions - prior_off_stats.receptions
			sacked = current_off_stats.sacked - prior_off_stats.sacked
			rec_yards = current_off_stats.rec_yards - prior_off_stats.rec_yards
			rush_yards = current_off_stats.rush_yards - prior_off_stats.rush_yards
			yac = current_off_stats.yac - prior_off_stats.yac
			pass_tds = current_off_stats.pass_tds - prior_off_stats.pass_tds
			rec_tds = current_off_stats.rec_tds - prior_off_stats.rec_tds
			rush_tds = current_off_stats.rush_tds - prior_off_stats.rush_tds
			ya_contact = current_off_stats.ya_contact - prior_off_stats.ya_contact
			completions = current_off_stats.completions - prior_off_stats.completions
			ints = current_off_stats.ints - prior_off_stats.ints
			drops = current_off_stats.drops - prior_off_stats.drops
			pass_att = current_off_stats.pass_att - prior_off_stats.pass_att
			rush_att = current_off_stats.rush_att - prior_off_stats.rush_att
			broke_tkls = current_off_stats.broke_tkls - prior_off_stats.broke_tkls
			fumbles = current_off_stats.fumbles - prior_off_stats.fumbles
			twenty_plus_yd_runs = current_off_stats.twenty_plus_yd_runs - prior_off_stats.twenty_plus_yd_runs

			comp_pct = round(
			    completions / pass_att * 100 if pass_att > 0 else 0,
			    1
			)

			pass_ypa = round(
			    pass_yards / pass_att if pass_att > 0 else 0,
			    1
			)

			rush_ypc = round(0 if rush_att == 0 else\
			    rush_yards / rush_att,
			    1
			)
			rec_ypc = round(0 if receptions == 0 else\
			    rec_yards / receptions,
			    1
			)
			pass_rating_calc = (
			    0 if pass_att == 0 else \
			    ((8.4 * pass_yards) + (330 * pass_tds) + \
			    (100 * completions) - (200 * ints)) / pass_att
			    )
			pass_rating = round(pass_rating_calc, 1)
			total_yards = current_off_stats.total_yards - prior_off_stats.total_yards
			total_tds = current_off_stats.total_tds - prior_off_stats.total_tds
			turnovers = ints + fumbles

			if return_stats:
				total_yards = sum([pass_yards, rush_yards, rec_yards, 
			        return_stats.kr_yds, return_stats.pr_yds]
			    )
				total_tds = sum([pass_tds, rush_tds, rec_tds,
					return_stats.kr_tds, return_stats.pr_tds
				])
				total_ypg = round(
				    0 if offensive_record.fields['Games Played'] == 0\
			        else total_yards,
				1)

			else:
				total_yards = sum([pass_yards, rush_yards, rec_yards])
				total_tds = sum([pass_tds, rush_tds, rec_tds])
				total_ypg = round(0 if offensive_record.fields['Games Played'] == 0\
				        else total_yards / offensive_record.fields['Games Played'], 1)

			game_stats = GameOffensiveStatsData(
			    id=new_id,
			    player_id=player_id,
			    pass_yards=pass_yards,
			    longest_rec=longest_rec,
			    longest_pass=longest_pass,
			    longest_run=longest_run,
			    week=current_week,
			    year=current_year,
			    games_played=1,
			    receptions=receptions,
			    sacked=sacked,
			    rec_yards=rec_yards,
			    rush_yards=rush_yards,
			    yac=yac,
			    pass_tds=pass_tds,
			    rec_tds=rec_tds,
			    rush_tds=rush_tds,
			    ya_contact=ya_contact,
			    completions=completions,
			    ints=ints,
			    drops=drops,
			    pass_att=pass_att,
			    rush_att=rush_att,
			    broke_tkls=broke_tkls,
			    fumbles=fumbles,
			    twenty_plus_yd_runs=twenty_plus_yd_runs,
			    pass_ypa=pass_ypa,
			    rush_ypc=rush_ypc,
			    rec_ypc=rec_ypc,
			    pass_rating=pass_rating,
			    total_yards=total_yards,
			    total_tds=total_tds,
			    turnovers=turnovers,
			    comp_pct=comp_pct
			)

			all_game_off_stats.append(game_stats)
	
	try:
		session.add_all(all_game_off_stats)
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Insert Game Offensive Stats script took {(round(execution_time, 2))} seconds to complete.')	


async def insert_game_return_stats_into_db(week_year_data, return_stats):

	start_time = time.time()
	print('Starting insert Game Return Stats script.')

	week_year = week_year_data[0]
	current_week = week_year.fields['Week']
	current_year = _convert_stats_year(week_year.fields['Year'])
	all_game_return_stats: List[GameOffensiveStatsData] = []

	for i, value in enumerate(return_stats):

		return_record = return_stats[i]

		# skip over players in dictionary from other years
		if _convert_stats_year(return_record.fields['Year']) != current_year:
			continue

		player_info: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == return_record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

		if not player_info:
			continue

		player_id: str = str(return_record.fields['Player ID']) + player_info.first_name + player_info.last_name

		prior_return_stats: SeasonReturnStatsData = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player_id,
            SeasonReturnStatsData.year == current_year
        ).scalar()

		new_id = str(uuid4())

		kr_avg = round(
		    return_record.fields['KR Yds.'] / return_record.fields['Kick Returns']\
		        if return_record.fields['Kick Returns'] != 0 else 0,
		    1
		)
		pr_avg = round(
		    return_record.fields['PR Yds.'] / return_record.fields['Punt Returns']\
		        if return_record.fields['Punt Returns'] != 0 else 0,
		    1
		)

		current_return_stats = SeasonReturnStatsData(
            id=new_id,
            player_id=player_id,
            kick_returns=return_record.fields['Kick Returns'],
            year=current_year,
            long_kr=return_record.fields['Long KR'],
            punt_returns=return_record.fields['Punt Returns'],
            long_pr=return_record.fields['Long PR'],
            games_played=return_record.fields['Games Played'],
            kr_tds=return_record.fields['KR TDs'],
            pr_tds=return_record.fields['PR TDs'],
            kr_yds=return_record.fields['KR Yds.'],
            pr_yds=return_record.fields['PR Yds.'],
            kr_avg=kr_avg,
            pr_avg=pr_avg
        )


		if not prior_return_stats:

			game_stats: GameReturnStatsData = GameReturnStatsData(
                id=new_id,
                player_id=player_id,
                week=current_week,
                year=current_year,
                games_played=1,
                kick_returns=current_return_stats.kick_returns,
                long_kr=current_return_stats.long_kr,
                punt_returns=current_return_stats.punt_returns,
                long_pr=current_return_stats.long_pr,
                kr_tds=current_return_stats.kr_tds,
                pr_tds=current_return_stats.pr_tds,
                kr_yds=current_return_stats.kr_yds,
                pr_yds=current_return_stats.pr_yds,
                kr_avg=current_return_stats.kr_avg,
                pr_avg=current_return_stats.pr_avg
            )

			all_game_return_stats.append(game_stats)
		
		else:

			kick_returns = current_return_stats.kick_returns - prior_return_stats.kick_returns
			long_kr = max([current_return_stats.long_kr, prior_return_stats.long_kr])
			punt_returns = current_return_stats.punt_returns - prior_return_stats.punt_returns
			long_pr = max([current_return_stats.long_pr, prior_return_stats.long_pr])
			kr_tds = current_return_stats.kr_tds - prior_return_stats.kr_tds
			pr_tds = current_return_stats.pr_tds - prior_return_stats.pr_tds
			kr_yds = current_return_stats.kr_yds - prior_return_stats.kr_yds
			pr_yds = current_return_stats.pr_yds - prior_return_stats.pr_yds
			kr_avg = 0 if kick_returns == 0 else round(kr_yds / kick_returns, 1)
			pr_avg = 0 if punt_returns == 0 else round(pr_yds / punt_returns, 1)

			game_stats = GameReturnStatsData(
			    id=new_id,
			    player_id=player_id,
			    week=current_week,
			    year=current_year,
			    games_played=1,
			    kick_returns=kick_returns,
			    long_kr=long_kr,
			    punt_returns=punt_returns,
			    long_pr=long_pr,
			    kr_tds=kr_tds,
			    pr_tds=pr_tds,
			    kr_yds=kr_yds,
			    pr_yds=pr_yds,
			    kr_avg=kr_avg,
			    pr_avg=pr_avg
			)

			all_game_return_stats.append(game_stats)

	try:
		session.add_all(all_game_return_stats)
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
		execution_time = time.time() - start_time
		print(f'Insert Game Return Stats script took {(round(execution_time, 2))} seconds to complete.')	
