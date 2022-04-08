from typing import List
from sqlalchemy import desc
from uuid import uuid4

from src.constants import(
    session,
    users
)
from src.utils.player import (
    _get_player_defensive_stats,
    _get_player_kick_return_stats,
    _get_player_kicking_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_punt_return_stats,
    _get_player_rushing_stats
)
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamStatsData import TeamStatsData
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



def insert_team_info_into_db(team_info):

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


################################################
######### insert team stats function ###########
################################################
def insert_team_stats_into_db():

    all_teams_info: List[TeamInfoData] = session.query(TeamInfoData).all()
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

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
                SeasonDefensiveStatsData.year == week_year.year
            ).all()
        off_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.team_id == team.id,
            PlayerInfoData.is_active == True,
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            SeasonOffensiveStatsData.year == week_year.year
            ).all()
        ret_data = session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.is_active == True,
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == week_year.year
                ).all()
        kick_data = session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.is_active == True,
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == week_year.year
            ).all()   

        # Create year specific id for primary key
        primary_key = f'{week_year.year}-{team.id}'

        # Convert data to models for data manipulation
        def_stats: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in def_data]
        kick_stats: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in kick_data]
        pass_stats: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in off_data]
        rush_stats: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in off_data]
        rec_stats: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in off_data]
        kick_return_stats: List[PlayerKickReturnStats] = [_get_player_kick_return_stats(player) for player in ret_data]
        punt_return_stats: List[PlayerPuntReturnStats] = [_get_player_punt_return_stats(player) for player in ret_data]
        
        # compile all TDs and TD points
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
        ppg = round(total_points / games_played, 1)
        
        # calculate pass, rush, rec. total yards and YPG
        pass_yards = sum([p.passing_stats.pass_yards for p in pass_stats])
        pass_ypg = round(pass_yards / games_played, 1)
        rush_yards = sum([p.rushing_stats.rush_yards for p in rush_stats])
        rush_ypg = round(rush_yards / games_played, 1)
        rec_yards = sum([p.receiving_stats.rec_yards for p in rec_stats])
        rec_ypg = round(rec_yards / games_played, 1)
        total_yards = pass_yards + rush_yards
        total_ypg = round(total_yards / games_played, 1)
        
        # calculate defensive stat totals
        sacks = sum([p.defensive_stats.sacks for p in def_stats])
        ints = sum([p.defensive_stats.ints_made for p in def_stats])
        ff = sum([p.defensive_stats.forced_fumbles for p in def_stats])
        fr = sum([p.defensive_stats.fumbles_rec for p in def_stats])
        turnovers = sum([ints, fr])
        pass_def = sum([p.defensive_stats.pass_def for p in def_stats])
        safeties = sum([p.defensive_stats.safeties for p in def_stats])
        
        # calculate KR and PR yards
        kr_yds = sum([p.kick_return_stats.kr_yds for p in kick_return_stats])
        pr_yds = sum([p.punt_return_stats.pr_yds for p in punt_return_stats])
        
        team_stats = TeamStatsData(
            id=primary_key,
            team_id=team.id,
            year=week_year.year,
            games_played=games_played,
            total_points=total_points,
            ppg=ppg,
            pass_yds=pass_yards,
            pass_ypg=pass_ypg,
            pass_tds=passing_tds,
            rush_yds=rush_yards,
            rush_tds=rushing_tds,
            rush_ypg=rush_ypg,
            rec_yds=rec_yards,
            rec_ypg=rec_ypg,
            rec_tds=receiving_tds,
            total_yards=total_yards,
            total_ypg=total_ypg,
            sacks=sacks,
            ints=ints,
            ff=ff,
            fr=fr,
            turnovers=turnovers,
            pass_def=pass_def,
            safeties=safeties,
            def_tds=def_tds,
            kr_yds=kr_yds,
            kr_tds=kr_tds,
            pr_yds=pr_yds,
            pr_tds=pr_tds
        )

        # query DB to see if team_stat exists
        team_query: TeamStatsData = session.query(TeamStatsData).filter(
            TeamStatsData.id == team_stats.id).scalar()
        
        if not team_query:
            session.add(team_stats)

        else:
            team_query.games_played=team_stats.games_played
            team_query.total_points=team_stats.total_points
            team_query.ppg=team_stats.ppg
            team_query.pass_yds=team_stats.pass_yds
            team_query.pass_ypg=team_stats.pass_ypg
            team_query.pass_tds=team_stats.pass_tds
            team_query.rush_yds=team_stats.rush_yds
            team_query.rush_ypg=team_stats.rush_ypg
            team_query.rush_tds=team_stats.rush_tds
            team_query.rec_yds=team_stats.rec_yds
            team_query.rec_ypg=team_stats.rec_ypg
            team_query.rec_tds=team_stats.rec_tds
            team_query.total_yards=team_stats.total_yards
            team_query.total_ypg=team_stats.total_ypg
            team_query.sacks=team_stats.sacks
            team_query.ints=team_stats.ints
            team_query.ff=team_stats.ff
            team_query.fr=team_stats.fr
            team_query.turnovers=team_stats.turnovers
            team_query.pass_def=team_stats.pass_def
            team_query.safeties=team_stats.safeties
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
