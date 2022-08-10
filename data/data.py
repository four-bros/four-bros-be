from typing import List
from collections import Counter
import ncaa_dynasty

from src.constants import (
    corrupt_team_ids,
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

defense_years: List[int] = []
kicking_years: List[int] = []
offense_years: List[int] = []
return_years: List[int] = []

for record in def_stats:
    defense_years.append(_convert_stats_year(record.fields['Year']))

for record in kicking_stats:
    kicking_years.append(_convert_stats_year(record.fields['Year']))

for record in off_stats:
    offense_years.append(_convert_stats_year(record.fields['Year']))

for record in return_stats:
    return_years.append(_convert_stats_year(record.fields['Year']))


print(f'defense years: {Counter(defense_years)}')
print('-----------------------------------------')
print(f'kicking years: {Counter(kicking_years)}')
print('-----------------------------------------')
print(f'offense years: {Counter(offense_years)}')
print('-----------------------------------------')
print(f'return years: {Counter(return_years)}')
