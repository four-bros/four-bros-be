import time
from src.constants import (
    users,
    session
)
from src.utils.helpers import(
    _convert_stats_year
)
from src.data_models.CoachInfoData import CoachInfoData
from src.data_models.CoachStatsData import CoachStatsData
from src.data_models.TeamInfoData import TeamInfoData


async def insert_coach_info_into_db(week_year):
    start_time = time.time()
    print('Starting insert CoachInfo script.')

    week_year_data = week_year[0]
    current_year = _convert_stats_year(week_year_data.fields['Year'])

    for user in users:

        new_id =user.id + str(current_year)
        
        coach: CoachInfoData = CoachInfoData(
            id=new_id,
            user=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            team_id=user.team_id,
            team_name=user.team_name,
            year=current_year
        )

        coach_query: CoachInfoData = session.query(CoachInfoData).where(CoachInfoData.id == coach.id).scalar()

        if not coach_query:
            session.add(coach)

        else:
            coach_query.team_id = coach.team_id
            coach_query.team_name = coach.team_name
    
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert CoachInfo script took {(round(execution_time, 2))} seconds to complete.')


async def insert_coach_stats_into_db(week_year_data):

    start_time = time.time()
    print('Starting insert CoachStats script.')

    current_week: int = week_year_data[0].fields['Week']
    current_year: int = _convert_stats_year(week_year_data[0].fields['Year'])

    #TODO: If it's the week after the title game, check for who is ranked 1st in BCS.
    # Could be a potential way to automate national titles

    for user in users:
        # Get team info for user_team
        user_team_info: TeamInfoData = session.query(TeamInfoData).where(TeamInfoData.id == user.team_id).scalar()

        new_id = user.id + str(current_year)

        coach_stats:CoachStatsData = CoachStatsData(
            id=new_id,
            coach_id=user.id,
            user=user.id,
            year=current_year,
            wins=user_team_info.wins,
            losses=user_team_info.losses,
            national_title=determine_national_title(week=current_week, team_info=user_team_info)
        )

        coach_query: CoachStatsData = session.query(CoachStatsData).where(
            CoachStatsData.id == coach_stats.id,
        ).scalar()
        
        if not coach_query:
            session.add(coach_stats)

        else:
            coach_query.wins = coach_stats.wins
            coach_query.losses = coach_stats.losses
            coach_query.national_title=coach_stats.national_title

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert CoachStats script took {(round(execution_time, 2))} seconds to complete.')


def determine_national_title(week: int, team_info: TeamInfoData) -> bool:

    bcs_rank: int = team_info.bcs_rank

    if week >= 22 and bcs_rank == 1:
        return True
    else: 
        return False
