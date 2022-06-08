from typing import List
import ncaa_dynasty

from src.constants import (
    data_dynasty_file_path,
    user_teams
)
from src.utils.helpers import _convert_stats_year


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


print(week_year[0].fields)
