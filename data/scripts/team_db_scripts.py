import asyncio
from typing import List
import uuid
from sqlalchemy import desc
from uuid import uuid4
import time

from src.constants import(
    session,
    users
)
from src.utils.helpers import(
    _convert_stats_year
)
from src.models.Teams import TeamGameStats
from src.utils.player import (
    _get_player_defensive_stats,
    _get_player_kick_return_stats,
    _get_player_kicking_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_punt_return_stats,
    _get_player_rushing_stats
)
from src.utils.team_stats import (
    _compile_prior_team_game_stats
)
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamGameStatsData import TeamGameStatsData
from src.data_models.TeamSeasonStatsData import TeamSeasonStatsData
from src.data_models.WeekYearData import WeekYearData
from src.models.Stats import (
    PlayerDefensiveStats,
    PlayerKickReturnStats,
    PlayerKickingStats,
    PlayerPassingStats,
    PlayerPuntReturnStats,
    PlayerReceivingStats,
    PlayerRushingStats
)


async def insert_team_info_into_db(team_info):

    start_time = time.time()
    print('Starting insert TeamInfo script.')

    user_teams: List[str] = [user.team_name for user in users]
    
    for i, value in enumerate(team_info):
        
        record = team_info[i]
        # Skip over players from duplicate or FCS teams 
        if (
            record.fields['Team ID'] == 160 or
            record.fields['Team ID'] == 161 or
            record.fields['Team ID'] == 162 or
            record.fields['Team ID'] == 163 or
            record.fields['Team ID'] == 164 or
            record.fields['Team ID'] == 300 or
            record.fields['Team ID'] == 400 or
            record.fields['Team ID'] == 1023
        ):
            continue
        
        new_team = TeamInfoData(
            id=record.fields['Team ID'],
            team_name=record.fields['Team Name'],
            team_short_name=record.fields['Team Short Name'],
            is_user=True if record.fields['Team Name'] in user_teams else False,
            coachs_poll_1st_votes=record.fields["Coach's Poll 1st Votes"],
            nickname=record.fields['Nickname'],
            wins=record.fields['Wins'],
            bcs_rank=record.fields['BCS Rank'],
            coachs_poll_rank=record.fields["Coach's Poll Rank"],
            media_poll_rank=record.fields['Media Poll Rank'],
            losses=record.fields['Losses'],
            media_poll_points=record.fields['Media Poll Points'],
            coachs_poll_points=record.fields["Coach's Poll Points"],
        )

        team_query: TeamInfoData = session.query(TeamInfoData).where(
            TeamInfoData.id == new_team.id).scalar()
        
        if not team_query:
            session.add(new_team)

        else:
            # Update the existing team with the new data
            team_query.team_name=new_team.team_name
            team_query.team_short_name=new_team.team_short_name
            team_query.coachs_poll_1st_votes=new_team.coachs_poll_1st_votes
            team_query.nickname=new_team.nickname
            team_query.is_user = new_team.is_user
            team_query.wins=new_team.wins
            team_query.bcs_rank=new_team.bcs_rank
            team_query.coachs_poll_rank=new_team.coachs_poll_rank
            team_query.media_poll_rank=new_team.media_poll_rank
            team_query.losses=new_team.losses
            team_query.media_poll_points=new_team.media_poll_points
            team_query.coachs_poll_points=new_team.coachs_poll_points
        
    try:
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert TeamInfo script took {(round(execution_time, 2))} seconds to complete.')


################################################
######### insert team stats function ###########
################################################
async def insert_team_season_stats_into_db(week_year_data):

    start_time = time.time()
    print('Starting insert Team Season Stats script.')

    all_teams_info: List[TeamInfoData] = session.query(TeamInfoData).all()
    # Query the year to filter out irrelevant years
    week_year = week_year_data[0]
    current_week: int = week_year.fields['Week']
    current_year: int = _convert_stats_year(week_year.fields['Year'])

    previous_week_year: TeamGameStatsData = session.query(TeamGameStatsData).order_by(
        desc(TeamGameStatsData.year),
        desc(TeamGameStatsData.week)
    ).first()

    # Safety check to prevent duplicate week/year entry into TeamGameStats table
    if previous_week_year and current_week == previous_week_year.week and current_year == previous_week_year.year:
        return

    for team in all_teams_info:
        # Skip over players from duplicate teams
        if (
            team.id == 160 or
            team.id == 161 or
            team.id == 162 or
            team.id == 163 or
            team.id == 164 or
            team.id == 300 or
            team.id == 400 or
            team.id == 1023
        ):
            continue

        # Grab all player data for each team
        def_data = session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.is_active == True,
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == current_year
            ).all()
        off_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.team_id == team.id,
            PlayerInfoData.is_active == True,
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            SeasonOffensiveStatsData.year == current_year
            ).all()
        ret_data = session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.is_active == True,
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == current_year
                ).all()
        kick_data = session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.is_active == True,
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == current_year
            ).all()
        
        # Skip over teams without data
        if not def_data and not off_data and not kick_data and not ret_data:
            continue

        # Create year specific id for primary key
        primary_key = f'{current_year}-{team.id}'

        # Convert data to models for data manipulation
        def_stats: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in def_data]
        kick_stats: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in kick_data]
        pass_stats: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in off_data]
        rush_stats: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in off_data]
        rec_stats: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in off_data]
        kick_return_stats: List[PlayerKickReturnStats] = [_get_player_kick_return_stats(player) for player in ret_data]
        punt_return_stats: List[PlayerPuntReturnStats] = [_get_player_punt_return_stats(player) for player in ret_data]
        
        # compile all TD points
        passing_tds = sum([p.passing_stats.pass_tds for p in pass_stats])
        rushing_tds = sum([p.rushing_stats.rush_tds for p in rush_stats])
        receiving_tds = sum([p.receiving_stats.rec_tds for p in rec_stats])
        def_tds = sum([p.defensive_stats.def_tds for p in def_stats])
        kr_tds = sum([p.kick_return_stats.kr_tds for p in kick_return_stats])
        pr_tds = sum([p.punt_return_stats.pr_tds for p in punt_return_stats])
        td_points = sum([passing_tds, rushing_tds, def_tds, kr_tds, pr_tds]) * 6
        
        # compile all FGs and XP points
        fgs = sum([p.kicking_stats.fg_made for p in kick_stats])
        xps = sum([p.kicking_stats.xp_made for p in kick_stats])
        kick_points = sum([fgs * 3, xps])
        
        # calculate total points, ppg
        games_played = team.wins + team.losses
        total_points = sum([td_points, kick_points])
        ppg = round(total_points / games_played if games_played != 0 else 0, 1)
        
        # calculate various offensive stats
        completions = sum([p.passing_stats.completions for p in pass_stats])
        pass_att = sum([p.passing_stats.pass_att for p in pass_stats])
        comp_pct = round(
                completions / pass_att * 100 if pass_att > 0 else 0,
                1
            )
        pass_yards = sum([p.passing_stats.pass_yards for p in pass_stats])
        pass_ypa = round(pass_yards / pass_att, 1)
        pass_ypg = round(pass_yards / games_played, 1)
        rush_att = sum([p.rushing_stats.rush_att for p in rush_stats])
        rush_yards = sum([p.rushing_stats.rush_yards for p in rush_stats])
        rush_ypc = round(rush_yards / rush_att, 1)
        rush_ypg = round(rush_yards / games_played, 1)
        receptions = sum([p.receiving_stats.receptions for p in rec_stats])
        rec_yards = sum([p.receiving_stats.rec_yards for p in rec_stats])
        rec_ypc = round(rec_yards / receptions, 1)
        rec_ypg = round(rec_yards / games_played, 1)
        off_yards = pass_yards + rush_yards
        off_ypg = round(off_yards / games_played, 1)
        ints = sum([p.passing_stats.ints for p in pass_stats])
        sacked = sum([p.passing_stats.sacked for p in pass_stats])
        fumbles = sum([p.rushing_stats.fumbles for p in rush_stats])
        drops = sum([p.receiving_stats.drops for p in rec_stats])
        off_turnovers = ints + fumbles
        
        # calculate defensive stat totals
        sacks = sum([p.defensive_stats.sacks for p in def_stats])
        tfl = sum([p.defensive_stats.tfl for p in def_stats])
        ints_made = sum([p.defensive_stats.ints_made for p in def_stats])
        ff = sum([p.defensive_stats.forced_fumbles for p in def_stats])
        fr = sum([p.defensive_stats.fumbles_rec for p in def_stats])
        def_turnovers = sum([ints_made, fr])
        pass_def = sum([p.defensive_stats.pass_def for p in def_stats])
        safeties = sum([p.defensive_stats.safeties for p in def_stats])
        blocked_kicks = sum([p.defensive_stats.blocked_kicks for p in def_stats])
        to_margin = def_turnovers - off_turnovers
        
        # calculate KR and PR yards
        kr_yds = sum([p.kick_return_stats.kr_yds for p in kick_return_stats])
        pr_yds = sum([p.punt_return_stats.pr_yds for p in punt_return_stats])

        # Calculate total yards
        total_yards = sum([off_yards, kr_yds, pr_yds])
        total_ypg = round(total_yards / games_played, 1)
        
        team_stats = TeamSeasonStatsData(
            id=primary_key,
            team_id=team.id,
            year=current_year,
            games_played=games_played,
            total_points=total_points,
            ppg=ppg,
            completions=completions,
            pass_att=pass_att,
            comp_pct=comp_pct,
            pass_yds=pass_yards,
            pass_ypa=pass_ypa,
            pass_ypg=pass_ypg,
            pass_tds=passing_tds,
            ints=ints,
            sacked=sacked,
            rush_att=rush_att,
            rush_yds=rush_yards,
            rush_tds=rushing_tds,
            rush_ypc=rush_ypc,
            fumbles=fumbles,
            rush_ypg=rush_ypg,
            receptions=receptions,
            rec_yds=rec_yards,
            rec_ypc=rec_ypc,
            rec_ypg=rec_ypg,
            rec_tds=receiving_tds,
            drops=drops,
            off_yards=off_yards,
            off_ypg=off_ypg,
            total_yards=total_yards,
            total_ypg=total_ypg,
            off_turnovers=off_turnovers,
            sacks=sacks,
            tfl=tfl,
            ints_made=ints_made,
            ff=ff,
            fr=fr,
            def_turnovers=def_turnovers,
            to_margin=to_margin,
            pass_def=pass_def,
            safeties=safeties,
            blocked_kicks=blocked_kicks,
            def_tds=def_tds,
            kr_yds=kr_yds,
            kr_tds=kr_tds,
            pr_yds=pr_yds,
            pr_tds=pr_tds
        )

        # query DB to see if team_stat exists
        team_query: TeamSeasonStatsData = session.query(TeamSeasonStatsData).filter(
            TeamSeasonStatsData.id == team_stats.id).scalar()
        
        if not team_query:
            session.add(team_stats)

        else:
            team_query.games_played=team_stats.games_played
            team_query.total_points=team_stats.total_points
            team_query.ppg=team_stats.ppg
            team_query.completions=team_stats.completions
            team_query.pass_att=team_stats.pass_att
            team_query.comp_pct=team_stats.comp_pct
            team_query.pass_yds=team_stats.pass_yds
            team_query.pass_ypa=team_stats.pass_ypa
            team_query.pass_ypg=team_stats.pass_ypg
            team_query.pass_tds=team_stats.pass_tds
            team_query.ints=team_stats.ints
            team_query.sacked=team_stats.sacked
            team_query.rush_att=team_stats.rush_att
            team_query.rush_yds=team_stats.rush_yds
            team_query.rush_ypc=team_stats.rush_ypc
            team_query.rush_ypg=team_stats.rush_ypg
            team_query.rush_tds=team_stats.rush_tds
            team_query.fumbles=team_stats.fumbles
            team_query.receptions=team_stats.receptions
            team_query.rec_yds=team_stats.rec_yds
            team_query.rec_ypc=team_stats.rec_ypc
            team_query.rec_ypg=team_stats.rec_ypg
            team_query.rec_tds=team_stats.rec_tds
            team_query.drops=team_stats.drops
            team_query.off_yards=team_stats.off_yards
            team_query.off_ypg=team_stats.off_ypg
            team_query.total_yards=team_stats.total_yards
            team_query.total_ypg=team_stats.total_ypg
            team_query.off_turnovers=team_stats.off_turnovers
            team_query.sacks=team_stats.sacks
            team_query.tfl=team_stats.tfl
            team_query.ints_made=team_stats.ints_made
            team_query.ff=team_stats.ff
            team_query.fr=team_stats.fr
            team_query.def_turnovers=team_stats.def_turnovers
            team_query.to_margin=team_stats.to_margin
            team_query.pass_def=team_stats.pass_def
            team_query.safeties=team_stats.safeties
            team_query.blocked_kicks=team_stats.blocked_kicks
            team_query.def_tds=team_stats.def_tds
            team_query.kr_yds=team_stats.kr_yds
            team_query.kr_tds=team_stats.kr_tds
            team_query.pr_yds=team_stats.pr_yds
            team_query.pr_tds=team_stats.pr_tds

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert Team Season Stats script took {(round(execution_time, 2))} seconds to complete.')


async def insert_team_game_stats_into_db(week_year_data):

    start_time = time.time()
    print('Starting insert Team Game Stats script.')

    week_year = week_year_data[0]
    current_week: int = week_year.fields['Week']
    current_year: int = _convert_stats_year(week_year.fields['Year'])
    
    teams_data: List[TeamInfoData] = session.query(TeamInfoData).all()

    for team in teams_data:

        team_season_stats: TeamSeasonStatsData = session.query(TeamSeasonStatsData).where(
            TeamSeasonStatsData.team_id == team.id,
            TeamSeasonStatsData.year == current_year
        ).scalar()

        # skip over teams that don't have team stats yet
        if not team_season_stats:
            continue

        # Check for prior game stats for team
        prior_team_game_stats: List[TeamGameStatsData] = session.query(TeamGameStatsData).where(
            TeamGameStatsData.team_id == team.id,
            TeamGameStatsData.year == current_year
        ).all()

        new_id = str(uuid4())

        if not prior_team_game_stats and team_season_stats:
            team_game_stats: TeamGameStatsData = TeamGameStatsData(
                    id=new_id,
                    team_id=team.id,
                    week=current_week,
                    year=current_year,
                    total_points=team_season_stats.total_points,
                    completions=team_season_stats.completions,
                    pass_att=team_season_stats.pass_att,
                    comp_pct=team_season_stats.comp_pct,
                    pass_yds=team_season_stats.pass_yds,
                    pass_ypa=team_season_stats.pass_ypa,
                    pass_tds=team_season_stats.pass_tds,
                    ints=team_season_stats.ints,
                    sacked=team_season_stats.sacked,
                    rush_att=team_season_stats.rush_att,
                    rush_yds=team_season_stats.rush_yds,
                    rush_ypc=team_season_stats.rush_ypc,
                    rush_tds=team_season_stats.rush_tds,
                    fumbles=team_season_stats.fumbles,
                    receptions=team_season_stats.receptions,
                    rec_yds=team_season_stats.rec_yds,
                    rec_ypc=team_season_stats.rec_ypc,
                    rec_tds=team_season_stats.rec_tds,
                    drops=team_season_stats.drops,
                    off_yards=team_season_stats.off_yards,
                    total_yards=team_season_stats.total_yards,
                    off_turnovers=team_season_stats.off_turnovers,
                    sacks=team_season_stats.sacks,
                    tfl=team_season_stats.tfl,
                    ints_made=team_season_stats.ints_made,
                    ff=team_season_stats.ff,
                    fr=team_season_stats.fr,
                    def_turnovers=team_season_stats.def_turnovers,
                    to_margin=team_season_stats.to_margin,
                    pass_def=team_season_stats.pass_def,
                    blocked_kicks=team_season_stats.blocked_kicks,
                    safeties=team_season_stats.safeties,
                    def_tds=team_season_stats.def_tds,
                    kr_yds=team_season_stats.kr_yds,
                    kr_tds=team_season_stats.kr_tds,
                    pr_yds=team_season_stats.pr_yds,
                    pr_tds=team_season_stats.pr_tds
            )
            session.add(team_game_stats)
        
        else:
            # Compile all prior game stats for the team
            prior_team_game_stats: TeamGameStats = _compile_prior_team_game_stats(prior_team_game_stats) 

            # Calculate previous game stats by subtracting all prior game stats from current season totals 
            total_points = team_season_stats.total_points - prior_team_game_stats.total_points
            completions = team_season_stats.completions - prior_team_game_stats.completions
            pass_att = team_season_stats.pass_att - prior_team_game_stats.pass_att
            comp_pct = round(
                completions / pass_att * 100 if pass_att > 0 else 0,
                1
            )
            pass_yds = team_season_stats.pass_yds - prior_team_game_stats.pass_yds
            pass_ypa = round(
                pass_yds / pass_att if pass_att > 0 else 0,
                1
            )
            pass_tds = team_season_stats.pass_tds - prior_team_game_stats.pass_tds
            ints = team_season_stats.ints - prior_team_game_stats.ints
            sacked = team_season_stats.sacked - prior_team_game_stats.sacked
            rush_att = team_season_stats.rush_att - prior_team_game_stats.rush_att
            rush_yds = team_season_stats.rush_yds - prior_team_game_stats.rush_yds
            rush_ypc = round(
                rush_yds / rush_att if rush_att > 0 else 0,
                1
            )
            rush_tds = team_season_stats.rush_tds - prior_team_game_stats.rush_tds
            fumbles = team_season_stats.fumbles - prior_team_game_stats.fumbles
            receptions = team_season_stats.receptions - prior_team_game_stats.receptions
            rec_yds = team_season_stats.rec_yds - prior_team_game_stats.rec_yds
            rec_ypc = round(
                rec_yds / receptions if receptions > 0 else 0,
                1
            )
            rec_tds = team_season_stats.rec_tds - prior_team_game_stats.rec_tds
            drops = team_season_stats.drops - prior_team_game_stats.drops
            off_yards = team_season_stats.off_yards - prior_team_game_stats.off_yards
            total_yards = team_season_stats.total_yards - prior_team_game_stats.total_yards
            off_turnovers = team_season_stats.off_turnovers - prior_team_game_stats.off_turnovers
            sacks = team_season_stats.sacks - prior_team_game_stats.sacks
            tfl = team_season_stats.tfl - prior_team_game_stats.tfl
            ints_made = team_season_stats.ints_made - prior_team_game_stats.ints_made
            ff = team_season_stats.ff - prior_team_game_stats.ff
            fr = team_season_stats.fr - prior_team_game_stats.fr
            def_turnovers = team_season_stats.def_turnovers - prior_team_game_stats.def_turnovers
            to_margin = team_season_stats.to_margin - prior_team_game_stats.to_margin
            pass_def = team_season_stats.pass_def - prior_team_game_stats.pass_def
            blocked_kicks = team_season_stats.blocked_kicks - prior_team_game_stats.blocked_kicks
            safeties = team_season_stats.safeties - prior_team_game_stats.safeties
            def_tds = team_season_stats.def_tds - prior_team_game_stats.def_tds
            kr_yds = team_season_stats.kr_yds - prior_team_game_stats.kr_yds
            kr_tds = team_season_stats.kr_tds - prior_team_game_stats.kr_tds
            pr_yds = team_season_stats.pr_yds - prior_team_game_stats.pr_yds
            pr_tds = team_season_stats.pr_tds - prior_team_game_stats.pr_tds

            team_game_stats: TeamGameStatsData = TeamGameStatsData(
                id=new_id,
                team_id=team.id,
                week=current_week,
                year=current_year,
                total_points=total_points,
                completions=completions,
                pass_att=pass_att,
                comp_pct=comp_pct,
                pass_yds=pass_yds,
                pass_ypa=pass_ypa,
                pass_tds=pass_tds,
                ints=ints,
                sacked=sacked,
                rush_att=rush_att,
                rush_yds=rush_yds,
                rush_ypc=rush_ypc,
                rush_tds=rush_tds,
                fumbles=fumbles,
                receptions=receptions,
                rec_yds=rec_yds,
                rec_ypc=rec_ypc,
                rec_tds=rec_tds,
                drops=drops,
                off_yards=off_yards,
                total_yards=total_yards,
                off_turnovers=off_turnovers,
                sacks=sacks,
                tfl=tfl,
                ints_made=ints_made,
                ff=ff,
                fr=fr,
                def_turnovers=def_turnovers,
                to_margin=to_margin,
                pass_def=pass_def,
                blocked_kicks=blocked_kicks,
                safeties=safeties,
                def_tds=def_tds,
                kr_yds=kr_yds,
                kr_tds=kr_tds,
                pr_yds=pr_yds,
                pr_tds=pr_tds
            )

            session.add(team_game_stats)

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert Team Game Stats script took {(round(execution_time, 2))} seconds to complete.')
