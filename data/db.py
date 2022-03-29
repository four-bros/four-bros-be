from src.constants import (
    Base,
    engine
)
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
from scripts.game_db_scripts import (
    insert_game_def_stats_into_db,
    insert_game_kick_stats_into_db,
    insert_game_off_stats_into_db,
    insert_game_return_stats_into_db
)
from scripts.misc_scripts import (
    insert_commits_into_db,
    insert_player_info_into_db,
    insert_week_year_into_db
)
from scripts.season_db_scripts import (
    insert_season_def_stats_into_db,
    insert_season_kicking_stats_into_db,
    insert_season_off_stats_into_db,
    insert_season_return_stats_into_db,
)
from scripts.team_db_scripts import (
    insert_team_info_into_db,
    insert_team_stats_into_db
)


def main():
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
    insert_week_year_into_db(week_year)
    insert_team_info_into_db(team_info)
    insert_commits_into_db(commits)
    insert_player_info_into_db(player_info)
    # Note: season_return_stats needs to be run prior to offensive stats.
    # This is because total_yards, total_tds, etc. are reliant on pulling data
    # from the season_return_stats table.
    insert_season_return_stats_into_db(return_stats)
    insert_season_def_stats_into_db(def_stats)
    insert_season_off_stats_into_db(off_stats)
    insert_season_kicking_stats_into_db(kicking_stats)
    # Note: the team_stats needs to be run after all season_stats scripts.
    # This is because the team stats table is reliant on data from 
    # all the various season_stats tables.
    insert_team_stats_into_db()
    # Note: all career_stats scripts need to be run after 
    # all season_stats scripts. This is because the team_stats table 
    # is reliant on data from all the various season_stats tables.
    insert_career_return_stats_into_db()
    insert_career_def_stats_into_db()
    insert_career_kicking_stats_into_db()
    insert_career_off_stats_into_db()
    # Note: all game_stats scripts need to be run after 
    # all season_stats scripts. This is because the game stats tables
    # are reliant on data from all the various season_stats tables.
    insert_game_def_stats_into_db()
    insert_game_kick_stats_into_db()
    insert_game_off_stats_into_db()
    insert_game_return_stats_into_db()


main()
