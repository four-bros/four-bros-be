from src.constants import(
    Base,
    engine
)
from .data import (
    def_stats,
    kicking_stats,
    player_info,
    commits,
    return_stats,
    off_stats,
    week_year,
    team_info
    )
from .db_scripts import (
    insert_commits_into_db,
    insert_def_stats_into_db,
    insert_kicking_stats_into_db,
    insert_off_stats_into_db,
    insert_player_info_into_db,
    insert_return_stats_into_db,
    insert_team_info_into_db,
    insert_team_stats_into_db,
    insert_week_year_into_db
    )


def main():
    # Create all DB tables
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # Insert all data to DB tables
    insert_week_year_into_db(week_year)
    insert_team_info_into_db(team_info)
    insert_commits_into_db(commits)
    insert_player_info_into_db(player_info)
    insert_def_stats_into_db(def_stats)
    insert_off_stats_into_db(off_stats)
    insert_kicking_stats_into_db(kicking_stats)
    insert_return_stats_into_db(return_stats)
    insert_team_stats_into_db()

main()
