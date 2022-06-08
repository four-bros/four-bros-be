import asyncio
import os
import ncaa_dynasty

from src.constants import (
    Base,
    data_dir,
    data_dynasty_file_path,
    engine,
    user_teams
)
# from data import (
#     def_stats,
#     kicking_stats,
#     player_info,
#     commits,
#     return_stats, 
#     off_stats,
#     week_year,
#     team_info
# )
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
from scripts.game_db_scripts import (
    insert_game_def_stats_into_db,
    insert_game_kick_stats_into_db,
    insert_game_off_stats_into_db,
    insert_game_return_stats_into_db
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


data = None
def_stats = None
kicking_stats = None
player_info = None
commits = None
return_stats = None
off_stats = None
week_year = None
team_info = None


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
    Base.metadata.create_all(engine)

    ################################
    # Insert all data to DB tables #
    ################################

    insert_week_year_into_db(week_year),
    insert_team_info_into_db(team_info),
    insert_coach_info_into_db(),
    insert_commits_into_db(commits),
    deactivate_inactive_players(player_info),
    insert_player_info_into_db(player_info)
    
    
    ##########################################################################
    # Note: season_return_stats needs to be run prior to offensive stats.
    # This is because total_yards, total_tds, etc. are reliant on pulling 
    # data from the season_return_stats table.
    ##########################################################################

    insert_season_return_stats_into_db(return_stats)
    insert_coach_stats_into_db(),
    insert_season_def_stats_into_db(def_stats),
    insert_season_off_stats_into_db(off_stats),
    insert_season_kicking_stats_into_db(kicking_stats)
    
    ##########################################################################
    # Note: all team_stats, career_stats and game_stats scripts need 
    # to be run after all season_stats scripts. This is because these 
    # scripts are reliant on data from all the various season_stats tables.
    ##########################################################################

    await asyncio.gather(
        insert_team_season_stats_into_db(),
        insert_team_game_stats_into_db(),
        insert_career_return_stats_into_db(),
        insert_career_def_stats_into_db(),
        insert_career_kicking_stats_into_db(),
        insert_career_off_stats_into_db(),
        insert_game_def_stats_into_db(),
        insert_game_kick_stats_into_db(),
        insert_game_off_stats_into_db(),
        insert_game_return_stats_into_db()
    )

sorted_data_dir = sorted(os.listdir(data_dir), key = lambda x: int(x.replace('OD-4Bros3_week', '')))

for file in sorted_data_dir:

    data_dynasty_file_path = os.path.join(data_dir, file)

    data = ncaa_dynasty.read_database(data_dynasty_file_path, user_teams)

    # List of records for each data category
    def_stats = data['Defensive Stats'].records
    kicking_stats = data['Kicking Stats'].records
    player_info = data['Player Info'].records
    commits = data['Committed Recruits'].records
    return_stats = data['Return Stats'].records
    off_stats = data['Offensive Stats'].records
    week_year = data['Week/Year'].records
    team_info = data['Team Info'].records

    asyncio.run(main())
