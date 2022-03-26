# NCAA 14 Dynasty File Reader Python Module

## What is this?
This python module is able to read raw NCAA dynasty files saved from NCAA 14 on Xbox360 and output certain data like player stats, team info, etc.

## Installation
Move/copy the `ncaa_dynasty.cp39-win_amd64.pyd` to the site-packages folder of your python environment. It should be something like `$ROOT/Lib/site-packages`

## How to use the module
The module is called `ncaa_dynasty` and after importing the module the first step is to read in a dynasty file
```python
import ncaa_dynasty
# OD-4Bros3 is the path to the dynasty file saved from the game
# Team1-4 are the teams to get committed recruits for.
data = ncaa_dynasty.read_database("OD-4Bros3", {"Team 1", "Team2", "Team3", "Team4"})
```
Data is a dictionary of table names -> tables and records.
```python
In [1]: data.keys()                                                                                                                                                                        
Out[1]: dict_keys(['Player Info', 'Week/Year', 'Kicking Stats', 'Offensive Stats', 'Defensive Stats', 'Team Info', 'Return Stats', 'Committed Recruits'])
```

To get player information look at the `Player Info` table. Each player is in a record of the table. You can call the `json()` method on a record, or the table, to get a json representation of the player. You can also access a python `dict` representation of the record by looking at the read-only `fields` attribute of the record This is how you would access tables/records for all the tables.
```python
player_info = data['Player Info']
In [1]: player_info.records[0].json()                                                                                                                                                      
Out[1]: '{"Games Played" : 0, "Spin Move" : 20, "Finesse Moves" : 20, "Zone Coverage" : 31, "Man Coverage" : 24, "Ball Carrier Vision" : 29, "Kick Return" : 40, "Weight" : 169, "Spec Catch" : 20, "Catch" : 40, "Catch In Traffic" : 34, "Height" : 75, "Press" : 22, "Redshirt" : 2, "Speed" : 72, "Juke Move" : 19, "Team ID" : 1023, "Player ID" : 8922, "Hit Power" : 36, "Acceleration" : 89, "Block Shedding" : 38, "Injury" : 89, "Hometown Desc" : 12816, "Year" : 3, "Trucking" : 18, "Last Name" : "Salyer", "Overall" : 93, "Position" : 7, "Throwing Power" : 40, "Stamina" : 69, "Power Moves" : 29, "Run Blocking" : 92, "Kick Accuracy" : 40, "Pursuit" : 34, "First Name" : "Jacob", "Agility" : 78, "Route Running" : 37, "Throwing Accuracy" : 40, "Strength" : 89, "Tackling" : 40, "Jump" : 40, "Jersey #" : 66, "Pass Blocking" : 86, "Elusiveness" : 23, "Play Recognition" : 34, "Break Tackle" : 40, "Impact Blocking" : 90, "Carry" : 40, "Release" : 27, "Stiff Arm" : 18, "Kick Power" : 40, "Awareness" : 76} '
In [1]: player_info.records[0].fields                                                                                                                                                      
Out[1]: 
{'Games Played': 0,
 'Spin Move': 20,
 'Finesse Moves': 20,
 'Zone Coverage': 31,
 'Man Coverage': 24,
 'Ball Carrier Vision': 29,
 'Kick Return': 40,
 'Weight': 169,
 'Spec Catch': 20,
 'Catch': 40,
 'Catch In Traffic': 34,
 'Height': 75,
 'Press': 22,
 'Redshirt': 2,
 'Speed': 72,
 'Juke Move': 19,
 'Team ID': 1023,
 'Player ID': 8922,
 'Hit Power': 36,
 'Acceleration': 89,
 'Block Shedding': 38,
 'Injury': 89,
 'Hometown Desc': 12816,
 'Year': 3,
 'Trucking': 18,
 'Last Name': 'Salyer',
 'Overall': 93,
 'Position': 7,
 'Throwing Power': 40,
 'Stamina': 69,
 'Power Moves': 29,
 'Run Blocking': 92,
 'Kick Accuracy': 40,
 'Pursuit': 34,
 'First Name': 'Jacob',
 'Agility': 78,
 'Route Running': 37,
 'Throwing Accuracy': 40,
 'Strength': 89,
 'Tackling': 40,
 'Jump': 40,
 'Jersey #': 66,
 'Pass Blocking': 86,
 'Elusiveness': 23,
 'Play Recognition': 34,
 'Break Tackle': 40,
 'Impact Blocking': 90,
 'Carry': 40,
 'Release': 27,
 'Stiff Arm': 18,
 'Kick Power': 40,
 'Awareness': 76}

```

## Conversion functions
Some of the stats for players, like position, are stored as numbers and need to be converted to be understood. The ncaa_dynasty python module has several converter functions for this purpose, they are
* `position_number_to_text` - Converts a position number to text e.g., 0 -> 'QB'
* `height_converter` - Coverts a player's height in inches to feet + inches
* `weight_converter` - Converts a player's weight number to lbs
* `player_year_converter` - Converts a player's year number to text e.g., 0 -> 'Fr'

## Changelog
* 0.0.1 - First version
* 0.0.2 - Fixed improper signed int conversion