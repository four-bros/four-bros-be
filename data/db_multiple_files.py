import asyncio
import os
import ncaa_dynasty
import time

from src.constants import (
    data_dir,
    user_teams
)
from src.utils.helpers import _convert_stats_year
from db import main


start_time = time.time()


data = None
def_stats = None
kicking_stats = None
player_info = None
commits = None
return_stats = None
off_stats = None
week_year = None
team_info = None


sorted_data_dir = sorted(os.listdir(data_dir), key = lambda x: int(x.replace('OD-4Bros3_week', '')))

for file in sorted_data_dir:

    if '.DS_Store' in file:
      continue

    dynasty_file = os.path.join(data_dir, file)

    data = ncaa_dynasty.read_database(dynasty_file, user_teams)

    # List of records for each data category
    def_stats = data['Defensive Stats'].records
    kicking_stats = data['Kicking Stats'].records
    player_info = data['Player Info'].records
    commits = data['Committed Recruits'].records
    return_stats = data['Return Stats'].records
    off_stats = data['Offensive Stats'].records
    week_year = data['Week/Year'].records
    team_info = data['Team Info'].records

    current_week: int = week_year[0].fields['Week']
    current_year: int = _convert_stats_year(week_year[0].fields['Year'])

    print(f'Starting main script for week {current_week}, {current_year}')
    asyncio.run(main())

execution_time = time.time() - start_time
print(f'All insert scripts took {(round(execution_time, 1))} seconds to complete.')
