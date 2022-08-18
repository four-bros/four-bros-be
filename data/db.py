import asyncio
import os
import ncaa_dynasty
import time

from src.constants import data_dir, user_teams
from src.utils.helpers import _convert_stats_year
from data import (
    def_stats,
    kicking_stats,
    player_info,
    commits,
    return_stats, 
    off_stats,
    week_year,
    team_info
)
from scripts.career_db_scripts import (
    insert_career_def_stats_into_db,
    insert_career_kicking_stats_into_db,
    insert_career_off_stats_into_db,
    insert_career_return_stats_into_db
)
from scripts.coach_db_scripts import (
    insert_coach_info_into_db,
    insert_coach_stats_into_db
)
from scripts.misc_scripts import (
    insert_commits_into_db,
    insert_week_year_into_db
)
from scripts.player_db_scripts import (
    deactivate_inactive_players,
    insert_player_info_into_db,
)
from scripts.season_db_scripts import (
    insert_season_def_stats_into_db,
    insert_season_kicking_stats_into_db,
    insert_season_off_stats_into_db,
    insert_season_return_stats_into_db,
)
from scripts.team_db_scripts import (
    insert_team_info_into_db,
    insert_team_game_stats_into_db,
    insert_team_season_stats_into_db
)
from scripts.game_db_scripts import (
    insert_game_def_stats_into_db,
    insert_game_kicking_stats_into_db,
    insert_game_off_stats_into_db,
    insert_game_return_stats_into_db
)
from scripts.cache import (
    cache_player_career_records,
    cache_player_game_records,
    cache_player_season_records,
    cache_team_game_records,
    cache_team_season_records
)


# data = None
# def_stats = None
# kicking_stats = None
# player_info = None
# commits = None
# return_stats = None
# off_stats = None
# week_year = None
# team_info = None


async def main():
    ########################################################
    ############ Drop DB tables if necessary. ##############
    ############ typically only necessary if ###############
    ############ updating table structure ##################
    ########################################################
    # Base.metadata.drop_all(engine)

    ########################
    # Create all DB tables #
    ########################
    # Base.metadata.create_all(engine)

    ################################
    # Insert all data to DB tables #
    ################################

    await asyncio.gather(insert_week_year_into_db(week_year))

    await asyncio.gather(
        insert_team_info_into_db(team_info),
        insert_coach_info_into_db(week_year),
        insert_commits_into_db(week_year, commits)
    )

    await asyncio.gather(deactivate_inactive_players(week_year, player_info))
    await asyncio.gather(insert_player_info_into_db(player_info))

    await asyncio.gather(
        insert_game_return_stats_into_db(week_year, return_stats)
    )

    await asyncio.gather(
        insert_season_return_stats_into_db(week_year, return_stats),
    )

    await asyncio.gather(
        insert_game_def_stats_into_db(week_year, def_stats),
        insert_game_kicking_stats_into_db(week_year, kicking_stats),
        insert_game_off_stats_into_db(week_year, off_stats),
    )
    
    ##########################################################################
    # Note: season_return_stats needs to be run prior to offensive stats.
    # This is because total_yards, total_tds, etc. are reliant on pulling 
    # data from the season_return_stats table.
    ##########################################################################

    await asyncio.gather(
        insert_coach_stats_into_db(week_year),
        insert_season_def_stats_into_db(week_year, def_stats),
        insert_season_kicking_stats_into_db(week_year, kicking_stats),
        insert_season_off_stats_into_db(week_year, off_stats)
    )
    
    ##########################################################################
    # Note: all team_stats, career_stats and game_stats scripts need 
    # to be run after all season_stats scripts. This is because these 
    # scripts are reliant on data from all the various season_stats tables.
    ##########################################################################

    await asyncio.gather(
        insert_team_season_stats_into_db(week_year),
        insert_career_return_stats_into_db(week_year, return_stats),
        insert_career_def_stats_into_db(week_year, def_stats),
        insert_career_kicking_stats_into_db(week_year, kicking_stats),
    )

    await asyncio.gather(
      insert_team_game_stats_into_db(week_year),
      insert_career_off_stats_into_db(week_year, off_stats),
    )

    await asyncio.gather(
        cache_player_career_records(),
        cache_player_game_records(),
        cache_player_season_records(),
        cache_team_game_records(),
        cache_team_season_records()
    )


start_time = time.time()

# sorted_data_dir = sorted(os.listdir(data_dir), key = lambda x: int(x.replace('OD-4Bros3_week', '')))

# for file in sorted_data_dir:

#     if '.DS_Store' in file:
#       continue

#     dynasty_file = os.path.join(data_dir, file)

#     data = ncaa_dynasty.read_database(dynasty_file, user_teams)

#     # List of records for each data category
#     def_stats = data['Defensive Stats'].records
#     kicking_stats = data['Kicking Stats'].records
#     player_info = data['Player Info'].records
#     commits = data['Committed Recruits'].records
#     return_stats = data['Return Stats'].records
#     off_stats = data['Offensive Stats'].records
#     week_year = data['Week/Year'].records
#     team_info = data['Team Info'].records

#     current_week: int = week_year[0].fields['Week']
#     current_year: int = _convert_stats_year(week_year[0].fields['Year'])

#     print(f'Starting main script for week {current_week}, {current_year}')
#     asyncio.run(main())


current_week: int = week_year[0].fields['Week']
current_year: int = _convert_stats_year(week_year[0].fields['Year'])
print(f'Starting main script for week {current_week}, {current_year}')

asyncio.run(main())

execution_time = time.time() - start_time
print(f'All insert scripts took {(round(execution_time, 1))} seconds to complete.')
