import ncaa_dynasty

from src.constants import(
    dynasty_file_path,
    user_teams
)


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


readable_year = ncaa_dynasty.player_year_converter(off_stats[0].fields['Year'])

position = ncaa_dynasty.position_number_to_text(player_info[0].fields['Position'])

print(off_stats[0].fields['Year'])
print(readable_year)
print(position)
