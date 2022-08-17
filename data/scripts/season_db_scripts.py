import asyncio
from typing import List
from uuid import uuid4
import time

from src.constants import corrupt_player_ids, corrupt_team_ids, session
from src.data_models.PlayerInfoData import PlayerInfoData
from src.utils.calcs import calculate_pass_rating
from src.utils.helpers import _convert_stats_year
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.WeekYearData import WeekYearData


################################################
######## insert player data functions ##########
################################################
async def insert_season_def_stats_into_db(week_year_data, def_stats):

    start_time = time.time()
    print('Starting insert Season Defensive Stats script.')

    week_year = week_year_data[0]
    # Note: do not need to convert the current year here. Only using this year for a comparison
    current_year = week_year.fields['Year']

    new_players: List[SeasonDefensiveStatsData] = []

    for i, value in enumerate(def_stats):

        record = def_stats[i]

        #skip over players not in the current year
        if record.fields['Year'] != current_year:
            continue
        
        if record.fields['Player ID'] in corrupt_player_ids:
            continue

        readable_year = _convert_stats_year(record.fields['Year'])
         # skip 2013 stats
        if readable_year == 2013:
            continue
        
        new_id = str(uuid4())
        
        total_tackles = record.fields['Solo Tkls'] + record.fields['Asst. Tkls']
        half_a_sack = round(record.fields['Half A Sack'] / 2, 1)
        total_sacks = half_a_sack + record.fields['Sacks']

        player_name: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

        player_id: str = ''

        if player_name:
            player_id: str = str(record.fields['Player ID']) + player_name.first_name + player_name.last_name
        else:
            player_id = str(record.fields['Player ID'])
        
        # skip players who aren't in PlayerInfoData
        if player_id.isdigit():
          continue
        
        player_def_stats = SeasonDefensiveStatsData(
            id=new_id,
            player_id=player_id,
            long_int_ret=record.fields['Long INT Ret'],
            sacks=record.fields['Sacks'],
            year=readable_year,
            forced_fumbles=record.fields['Forced Fumbles'],
            solo_tkls=record.fields['Solo Tkls'],
            safeties=record.fields['Safties'],
            pass_def=record.fields['Pass Def.'],
            blocked_kicks=record.fields['Blocked Kicks'],
            tfl=record.fields['TFL'],
            ints_made=record.fields['INTs Made'],
            games_played=record.fields['Games Played'],
            fumbles_rec=record.fields['Fumbles Rec.'],
            half_a_sack=half_a_sack,
            asst_tkls=record.fields['Asst. Tkls'],
            def_tds=record.fields['Def. TDs'],
            fum_rec_yards=record.fields['Fum. Rec. Yards'],
            int_ret_yards=record.fields['INT Ret. Yards'],
            total_tkls=total_tackles,
            total_sacks=total_sacks
        )

        # Query table to determine if player has a record or not
        player_query: SeasonDefensiveStatsData = session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == player_def_stats.player_id,
            SeasonDefensiveStatsData.year == player_def_stats.year
        ).scalar()

        if not player_query:
            new_players.append(player_def_stats)

        else:
            player_query.long_int_ret=player_def_stats.long_int_ret
            player_query.sacks=player_def_stats.sacks
            player_query.year=player_def_stats.year
            player_query.forced_fumbles=player_def_stats.forced_fumbles
            player_query.solo_tkls=player_def_stats.solo_tkls
            player_query.safeties=player_def_stats.safeties
            player_query.pass_def=player_def_stats.pass_def
            player_query.blocked_kicks=player_def_stats.blocked_kicks
            player_query.tfl=player_def_stats.tfl
            player_query.ints_made=player_def_stats.ints_made
            player_query.games_played=player_def_stats.games_played
            player_query.fumbles_rec=player_def_stats.fumbles_rec
            player_query.half_a_sack=player_def_stats.half_a_sack
            player_query.asst_tkls=player_def_stats.asst_tkls
            player_query.def_tds=player_def_stats.def_tds
            player_query.fum_rec_yards=player_def_stats.fum_rec_yards
            player_query.int_ret_yards=player_def_stats.int_ret_yards
            player_query.total_tkls=player_def_stats.total_tkls

    try:
        session.add_all(new_players)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert Season Defensive Stats script took {(round(execution_time, 2))} seconds to complete.')


async def insert_season_kicking_stats_into_db(week_year_data, kicking_stats):

    start_time = time.time()
    print('Starting insert Season Kicking Stats script.')

    week_year = week_year_data[0]
    # Note: do not need to convert the current year here. Only using this year for a comparison
    current_year = week_year.fields['Year']

    new_players: List[SeasonKickingStatsData] = []
    
    for i, value in enumerate(kicking_stats):

        record = kicking_stats[i]

        # skip over players not in the current year
        if record.fields['Year'] != current_year:
            continue

        if record.fields['Player ID'] in corrupt_player_ids:
            continue
        readable_year = _convert_stats_year(record.fields['Year'])
         # skip 2013 stats
        if readable_year == 2013:
            continue
        
        new_id = str(uuid4())

        fg_pct = round(
            record.fields['FG Made'] / record.fields['FG Att.'] * 100\
                if record.fields['FG Att.'] != 0 else 0,
            1)
        xp_pct = round(
            record.fields['XP Made'] / record.fields['XP Att.'] * 100\
                if record.fields['XP Att.'] != 0 else 0,
            1)
        fg_50_plus_pct = round(
            record.fields['FG Made 50+'] / record.fields['FG Att. 50+'] * 100\
                if record.fields['FG Att. 50+'] != 0 else 0,
            1)
        punt_avg = round(
            record.fields['Total Punt Yards'] / record.fields['# Punts']\
                if record.fields['# Punts'] != 0 else 0, 
            1)
        net_avg = round(
            record.fields['Net Punting'] / record.fields['# Punts']\
                if record.fields['# Punts'] != 0 else 0, 
            1)
        
        player_name: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

        player_id: str = ''

        if player_name:
            player_id: str = str(record.fields['Player ID']) + player_name.first_name + player_name.last_name
        else:
            player_id = str(record.fields['Player ID'])
        
        # skip players who aren't in PlayerInfoData
        if player_id.isdigit():
          continue
        
        player_kicking_stats = SeasonKickingStatsData(
            id=new_id,
            player_id=player_id,
            fg_made_17_29=record.fields['FG Made 17-29'],
            fg_att_17_29=record.fields['FG Att. 17-29'],
            long_fg=record.fields['Long FG'],
            ko_touchbacks=record.fields['KO Touchbacks'],
            long_punt=record.fields['Long Punt'],
            xp_att=record.fields['XP Att.'],
            year=readable_year,
            punts_blocked=record.fields['Punts Blocked'],
            fg_att=record.fields['FG Att.'],
            total_punt_yards=record.fields['Total Punt Yards'],
            xp_blocked=record.fields['XP Blocked'],
            fg_blocked=record.fields['FG Blocked'],
            fg_att_40_49=record.fields['FG Att. 40-49'],
            fg_made_40_49=record.fields['FG Made 40-49'],
            fg_att_30_39=record.fields['FG Att. 30-39'],
            fg_made_30_39=record.fields['FG Att. 30-39'],
            fg_att_50_plus=record.fields['FG Att. 50+'],
            fg_made_50_plus=record.fields['FG Made 50+'],
            punt_touchbacks=record.fields['Punt Touchbacks'],
            games_played=record.fields['Games Played'],
            kickoffs=record.fields['Kickoffs'],
            xp_made=record.fields['XP Made'],
            net_punting=record.fields['Net Punting'],
            fg_made=record.fields['FG Made'],
            number_punts=record.fields['# Punts'],
            inside_twenty=record.fields['Inside 20'],
            fg_pct=fg_pct,
            xp_pct=xp_pct,
            fg_50_plus_pct=fg_50_plus_pct,
            punt_avg=punt_avg,
            net_avg=net_avg
        )

        player_query: SeasonKickingStatsData = session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == player_kicking_stats.player_id,
            SeasonKickingStatsData.year == player_kicking_stats.year
        ).scalar()
        
        if not player_query:
            new_players.append(player_kicking_stats)

        else:
            player_query.fg_made_17_29=player_kicking_stats.fg_made_17_29
            player_query.fg_att_17_29=player_kicking_stats.fg_att_17_29
            player_query.long_fg=player_kicking_stats.long_fg
            player_query.ko_touchbacks=player_kicking_stats.ko_touchbacks
            player_query.long_punt=player_kicking_stats.long_punt
            player_query.xp_att=player_kicking_stats.xp_att
            player_query.year=player_kicking_stats.year
            player_query.punts_blocked=player_kicking_stats.punts_blocked
            player_query.fg_att=player_kicking_stats.fg_att
            player_query.total_punt_yards=player_kicking_stats.total_punt_yards
            player_query.xp_blocked=player_kicking_stats.xp_blocked
            player_query.fg_blocked=player_kicking_stats.fg_blocked
            player_query.fg_att_40_49=player_kicking_stats.fg_att_40_49
            player_query.fg_made_40_49=player_kicking_stats.fg_made_40_49
            player_query.fg_att_30_39=player_kicking_stats.fg_att_30_39
            player_query.fg_made_30_39=player_kicking_stats.fg_made_30_39
            player_query.fg_att_50_plus=player_kicking_stats.fg_att_50_plus
            player_query.fg_made_50_plus=player_kicking_stats.fg_made_50_plus
            player_query.punt_touchbacks=player_kicking_stats.punt_touchbacks
            player_query.games_played=player_kicking_stats.games_played
            player_query.kickoffs=player_kicking_stats.kickoffs
            player_query.xp_made=player_kicking_stats.xp_made
            player_query.net_punting=player_kicking_stats.net_punting
            player_query.fg_made=player_kicking_stats.fg_made
            player_query.number_punts=player_kicking_stats.number_punts
            player_query.inside_twenty=player_kicking_stats.inside_twenty
            player_query.net_avg=player_kicking_stats.net_avg

    try:
        session.add_all(new_players)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert Season Kicking Stats script took {(round(execution_time, 2))} seconds to complete.')


async def insert_season_off_stats_into_db(week_year_data, off_stats):

    start_time = time.time()
    print('Starting insert Season Offensive Stats script.')

    week_year = week_year_data[0]
    # Note: do not need to convert the current year here. Only using this year for a comparison
    current_year = week_year.fields['Year']

    new_players: List[SeasonOffensiveStatsData] = []

    for i, value in enumerate(off_stats):

        record = off_stats[i]

        # skip over players not in the current year
        if record.fields['Year'] != current_year:
            continue

        if record.fields['Player ID'] in corrupt_player_ids:
            continue

        readable_year = _convert_stats_year(record.fields['Year'])
         # skip 2013 stats
        if readable_year == 2013:
            continue
        
        new_id = str(uuid4())

        player_info: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

        if not player_info:
            continue

        player_id: str = str(record.fields['Player ID']) + player_info.first_name + player_info.last_name

        comp_pct = round(
            record.fields['Completions'] / record.fields['Pass Att.'] * 100\
                if record.fields['Pass Att.'] != 0 else 0,
                1
            )
        pass_ypa = round(
            record.fields['Pass. Yards'] / record.fields['Pass Att.']\
                if record.fields['Pass Att.'] != 0 else 0,
                1
            )
        pass_ypg = round(
            record.fields['Pass. Yards'] / record.fields['Games Played']\
                if record.fields['Games Played'] != 0 else 0, 
                1
            )
        rush_ypc = round(
            record.fields['Rush Yards'] / record.fields['Rush Att.']\
                if record.fields['Rush Att.'] != 0 else 0,
                1
            )
        rush_ypg = round(
            record.fields['Rush Yards'] / record.fields['Games Played']\
                if record.fields['Games Played'] != 0 else 0,
                1
            )
        rec_ypc = round(
            record.fields['Rec. Yards'] / record.fields['Receptions']\
                if record.fields['Receptions'] != 0 else 0,
                1
            )
        rec_ypg = round(
            record.fields['Rec. Yards'] / record.fields['Games Played']\
                if record.fields['Games Played'] != 0 else 0,
                1
            )

        pass_rating = calculate_pass_rating(
            pass_att=record.fields['Pass Att.'],
            pass_yds=record.fields['Pass. Yards'],
            pass_tds=record.fields['Pass. TDs'],
            completions=record.fields['Completions'],
            ints=record.fields['INTs']
        )

        turnovers = record.fields['INTs'] + record.fields['Fumbles']

        # get ReturnStats for total stats purposes (yards, TDs, etc)
        return_stats: SeasonReturnStatsData = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player_id,
            SeasonReturnStatsData.year == readable_year
        ).scalar()

        # Calculate total stats
        total_yards = 0
        total_tds = 0
        total_ypg = 0

        if return_stats:
            total_yards = sum([
                record.fields['Pass. Yards'], record.fields['Rec. Yards'], record.fields['Rush Yards'], 
                return_stats.kr_yds, return_stats.pr_yds]
            )
            total_tds = sum([
                record.fields['Pass. TDs'], record.fields['Rec. TDs'], record.fields['Rush TDs'],
                return_stats.kr_tds, return_stats.pr_tds
            ])
            total_ypg = round(
                0 if record.fields['Games Played'] == 0\
                    else total_yards / record.fields['Games Played'],
                1)
        else:
            total_yards = sum([
                record.fields['Pass. Yards'], record.fields['Rec. Yards'], record.fields['Rush Yards']
                ])
            total_tds = sum([
                record.fields['Pass. TDs'], record.fields['Rec. TDs'], record.fields['Rush TDs']
                ])
            total_ypg = round(
                0 if record.fields['Games Played'] == 0\
                    else total_yards / record.fields['Games Played'],
                1)
        
        player_name: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == record.fields['Player ID'],
            PlayerInfoData.is_active == True,
        ).scalar()

        player_id: str = ''

        if player_name:
            player_id: str = str(record.fields['Player ID']) + player_name.first_name + player_name.last_name
        else:
            player_id = str(record.fields['Player ID'])
        
        # skip players who aren't in PlayerInfoData
        if player_id.isdigit():
          continue

        player_off_stats = SeasonOffensiveStatsData(
            id=new_id,
            player_id=player_id,
            pass_yards=record.fields['Pass. Yards'],
            longest_rec=record.fields['Longest Rec.'],
            longest_pass=record.fields['Longest Pass'],
            longest_run=record.fields['Longest Run'],
            year=readable_year,
            receptions=record.fields['Receptions'],
            sacked=record.fields['Sacked'],
            rec_yards=record.fields['Rec. Yards'],
            rush_yards=record.fields['Rush Yards'],
            yac=record.fields['Y.A.C.'],
            pass_tds=record.fields['Pass. TDs'],
            games_played=record.fields['Games Played'],
            rec_tds=record.fields['Rec. TDs'],
            rush_tds=record.fields['Rush TDs'],
            ya_contact=record.fields['Y.A. Contact'],
            completions=record.fields['Completions'],
            ints=record.fields['INTs'],
            drops=record.fields['Drops'],
            pass_att=record.fields['Pass Att.'],
            rush_att=record.fields['Rush Att.'],
            broke_tkls=record.fields['Broke Tkls.'],
            fumbles=record.fields['Fumbles'],
            twenty_plus_yd_runs=record.fields['20+ yd. Runs'],
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
        
        player_query: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player_off_stats.player_id,
            SeasonOffensiveStatsData.year == player_off_stats.year
        ).scalar()

        if not player_query:
            new_players.append(player_off_stats)

        else:

            player_query.pass_yards=player_off_stats.pass_yards
            player_query.longest_rec=player_off_stats.longest_rec
            player_query.longest_pass=player_off_stats.longest_pass
            player_query.longest_run=player_off_stats.longest_run
            player_query.year=player_off_stats.year
            player_query.receptions=player_off_stats.receptions
            player_query.sacked=player_off_stats.sacked
            player_query.rec_yards=player_off_stats.rec_yards
            player_query.rush_yards=player_off_stats.rush_yards
            player_query.yac=player_off_stats.yac
            player_query.pass_tds=player_off_stats.pass_tds
            player_query.games_played=player_off_stats.games_played
            player_query.rec_tds=player_off_stats.rec_tds
            player_query.rush_tds=player_off_stats.rush_tds
            player_query.ya_contact=player_off_stats.ya_contact
            player_query.completions=player_off_stats.completions
            player_query.ints=player_off_stats.ints
            player_query.drops=player_off_stats.drops
            player_query.pass_att=player_off_stats.pass_att
            player_query.rush_att=player_off_stats.rush_att
            player_query.broke_tkls=player_off_stats.broke_tkls
            player_query.fumbles=player_off_stats.fumbles
            player_query.twenty_plus_yd_runs=player_off_stats.twenty_plus_yd_runs
            player_query.pass_ypa=player_off_stats.pass_ypa
            player_query.pass_ypg=player_off_stats.pass_ypg
            player_query.rush_ypc=player_off_stats.rush_ypc
            player_query.rush_ypg=player_off_stats.rush_ypg
            player_query.rec_ypc=player_off_stats.rec_ypc
            player_query.rec_ypg=player_off_stats.rec_ypg
            player_query.total_yards=player_off_stats.total_yards
            player_query.total_tds=player_off_stats.total_tds
            player_query.total_ypg=player_off_stats.total_ypg
            player_query.turnovers=player_off_stats.turnovers
            player_query.comp_pct=player_off_stats.comp_pct
            player_query.pass_rating=player_off_stats.pass_rating

    try:
        session.add_all(new_players)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert Season Offensive Stats script took {(round(execution_time, 2))} seconds to complete.')


async def insert_season_return_stats_into_db(week_year_data, return_stats):

    start_time = time.time()
    print('Starting insert Season Return Stats script.')

    week_year = week_year_data[0]
    # Note: do not need to convert the current year here. Only using this year for a comparison
    current_year = week_year.fields['Year']
    
    new_players: List[SeasonReturnStatsData] = []
    
    for i, value in enumerate(return_stats):

        record = return_stats[i]

        # skip over players not in the current year
        if record.fields['Year'] != current_year:
            continue

        # skip bad data
        if record.fields['Player ID'] in corrupt_player_ids:
            continue
        readable_year = _convert_stats_year(record.fields['Year'])
         # skip 2013 stats
        if readable_year == 2013:
            continue
        
        new_id = str(uuid4())
        
        kr_avg = round(
            record.fields['KR Yds.'] / record.fields['Kick Returns']\
                if record.fields['Kick Returns'] != 0 else 0,
            1
            )
        pr_avg = round(
            record.fields['PR Yds.'] / record.fields['Punt Returns']\
                if record.fields['Punt Returns'] != 0 else 0,
            1
            )

        player_name: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.roster_id == record.fields['Player ID'],
            PlayerInfoData.is_active == True
        ).scalar()

        player_id: str = ''

        if player_name:
            player_id: str = str(record.fields['Player ID']) + player_name.first_name + player_name.last_name
        else:
            player_id = str(record.fields['Player ID'])
        
        # skip players who aren't in PlayerInfoData
        if player_id.isdigit():
          continue
        
        player_return_stats = SeasonReturnStatsData(
            id=new_id,
            player_id=player_id,
            kick_returns=record.fields['Kick Returns'],
            year=readable_year,
            long_kr=record.fields['Long KR'],
            punt_returns=record.fields['Punt Returns'],
            long_pr=record.fields['Long PR'],
            games_played=record.fields['Games Played'],
            kr_tds=record.fields['KR TDs'],
            pr_tds=record.fields['PR TDs'],
            kr_yds=record.fields['KR Yds.'],
            pr_yds=record.fields['PR Yds.'],
            kr_avg=kr_avg,
            pr_avg=pr_avg
        )

        player_query: SeasonReturnStatsData = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player_return_stats.player_id,
            SeasonReturnStatsData.year == player_return_stats.year
        ).scalar()
        
        if not player_query:
            new_players.append(player_return_stats)
            
        else:
            player_query.kick_returns=player_return_stats.kick_returns
            player_query.year=player_return_stats.year
            player_query.long_kr=player_return_stats.long_kr
            player_query.punt_returns=player_return_stats.punt_returns
            player_query.long_pr=player_return_stats.long_pr
            player_query.games_played=player_return_stats.games_played
            player_query.kr_tds=player_return_stats.kr_tds
            player_query.pr_tds=player_return_stats.pr_tds
            player_query.kr_yds=player_return_stats.kr_yds
            player_query.pr_yds=player_return_stats.pr_yds
            player_query.kr_avg=player_return_stats.kr_avg
            player_query.pr_avg=player_return_stats.pr_avg

    try:
        session.add_all(new_players)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert Season Return Stats script took {(round(execution_time, 2))} seconds to complete.')
