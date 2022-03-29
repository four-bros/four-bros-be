import ncaa_dynasty

from src.constants import (
    dynasty_file_path,
    user_teams
)
from src.utils.helpers import _convert_stats_year


data = ncaa_dynasty.read_database(dynasty_file_path, user_teams)

# List of records for each data category
def_stats = data['Defensive Stats'].records
kicking_stats = data['Kicking Stats'].records
player_info = data['Player Info'].records
commits = data['Committed Recruits'].records
return_stats = data['Return Stats'].records
off_stats = data['Offensive Stats'].records
week_year = data['Week/Year'].records
team_info = data['Team Info'].records


year = _convert_stats_year(week_year[0].fields['Year'])

print(f"Week: {week_year[0].fields['Week']}")
print(f"Year: {year}")


# for player in player_info:
#     if player.fields['Team ID'] == 115:
#         player_name = player.fields['First Name'] + ' ' + player.fields['Last Name']
#         player_id = player.fields['Player ID']
#         print(f'{player_name}: {player_id}')
