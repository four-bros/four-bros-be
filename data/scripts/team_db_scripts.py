from typing import List
from sqlalchemy import desc
from sqlalchemy.sql.expression import update
from uuid import uuid4

from src.constants import(
    session,
    user_teams
)

from src.utils.helpers import(
    _convert_stats_year
)
from src.utils.player import (
    _get_player_defensive_stats,
    _get_player_kicking_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_return_stats,
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
from src.models.Stats import(
    PlayerDefensiveStats,
    PlayerKickingStats,
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerReturnStats,
    PlayerRushingStats
)



def insert_team_info_into_db(team_info):
    
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

        team: TeamInfoData = session.query(TeamInfoData).filter(
            TeamInfoData.id == new_team.id).scalar()
        
        if team is None:
            session.add(new_team)
            session.flush()
        else:
            update(TeamInfoData).where(TeamInfoData.id == new_team.id).values(
                id=new_team.id,
                team_name=new_team.team_name,
                team_short_name=new_team.team_short_name,
                coachs_poll_1st_votes=new_team.coachs_poll_1st_votes,
                nickname=new_team.nickname,
                wins=new_team.wins,
                bcs_rank=new_team.bcs_rank,
                coachs_poll_rank=new_team.coachs_poll_rank,
                media_poll_rank=new_team.media_poll_rank,
                losses=new_team.losses,
                media_poll_points=new_team.media_poll_points,
                coachs_poll_points=new_team.coachs_poll_points,
            )
        
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
        desc(WeekYearData.year)
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
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == week_year.year
            ).all()
        off_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.team_id == team.id,
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            SeasonOffensiveStatsData.year == week_year.year
            ).all()
        ret_data = session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == week_year.year
                ).all()
        kick_data = session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                PlayerInfoData.team_id == team.id,
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == week_year.year
            ).all()   

        # Convert data to models for data manipulation
        def_stats: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in def_data]
        kick_stats: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in kick_data]
        pass_stats: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in off_data]
        rush_stats: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in off_data]
        rec_stats: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in off_data]
        return_stats: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in ret_data]
        
        # compile all TDs and TD points
        passing_tds = sum([p.passing_stats.pass_tds for p in pass_stats])
        rushing_tds = sum([p.rushing_stats.rush_tds for p in rush_stats])
        receiving_tds = sum([p.receiving_stats.rec_tds for p in rec_stats])
        def_tds = sum([p.defensive_stats.def_tds for p in def_stats])
        kr_tds = sum([p.return_stats.kr_tds for p in return_stats])
        pr_tds = sum([p.return_stats.pr_tds for p in return_stats])
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
        kr_yds = sum([p.return_stats.kr_yds for p in return_stats])
        pr_yds = sum([p.return_stats.pr_yds for p in return_stats])
        
        new_team = TeamStatsData(
            id=team.id,
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
        team: TeamStatsData = session.query(TeamStatsData).filter(
            TeamStatsData.id == new_team.id).scalar()
        
        if team is None:
            session.add(new_team)
        else:
            update(TeamStatsData).where(TeamStatsData.id == new_team.id).values(
                id=new_team.id,
                total_points=new_team.total_points,
                ppg=new_team.ppg,
                pass_yds=new_team.pass_yds,
                pass_ypg=new_team.pass_ypg,
                pass_tds=new_team.pass_tds,
                rush_yds=new_team.rush_yds,
                rush_ypg=new_team.rush_ypg,
                rush_tds=new_team.rush_tds,
                rec_yds=new_team.rec_yds,
                rec_ypg=new_team.rec_ypg,
                rec_tds=new_team.rec_tds,
                sacks=new_team.sacks,
                ints=new_team.ints,
                ff=new_team.ff,
                fr=new_team.fr,
                pass_def=new_team.pass_def,
                safeties=new_team.safeties,
                def_tds=new_team.def_tds,
                kr_yds=new_team.kr_yds,
                kr_tds=new_team.kr_tds,
                pr_yds=new_team.pr_yds,
                pr_tds=new_team.pr_tds
            )
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
