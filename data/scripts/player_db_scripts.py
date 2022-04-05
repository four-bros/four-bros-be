from typing import List
from sqlalchemy import desc
from uuid import uuid4

import ncaa_dynasty
from src.constants import session
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.WeekYearData import WeekYearData

def deactivate_inactive_players(player_info):

    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    if week_year.week == 1:
        # Compile a list of active player IDs
        active_player_ids: List[str] = []

        for i, value in enumerate(player_info):
            record = player_info[i]
            player_id = str(record.fields['Player ID']) + record.fields['First Name'] + record.fields['Last Name']
            active_player_ids.append(player_id)
        
        print(active_player_ids[0:10])
        
        # Get all players in DB to determine if they are active or not
        all_players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

        for player in all_players:
            if player.id not in active_player_ids:
                player.is_active = False

        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


def insert_player_info_into_db(player_info):

    for i, value in enumerate(player_info):
        
        record = player_info[i]
        # Skip over players from duplicate teams
        # Skip over players from duplicate or FCS teams 
        if (
            record.fields['Team ID'] == 160 or
            record.fields['Team ID'] == 161 or
            record.fields['Team ID'] == 162 or
            record.fields['Team ID'] == 163 or
            record.fields['Team ID'] == 164 or
            record.fields['Team ID'] == 300 or
            record.fields['Team ID'] == 400 or
            record.fields['Team ID'] == 1023
        ):
            continue
        
        # Convert unintelligible values to readable values
        readable_position = ncaa_dynasty.position_number_to_text(record.fields['Position'])
        readable_height = ncaa_dynasty.height_converter(record.fields['Height'])
        readable_weight = ncaa_dynasty.weight_converter(record.fields['Weight'])
        readable_year = ncaa_dynasty.player_year_converter(record.fields['Year'])
        
        is_redshirt = False if record.fields['Redshirt'] == 0 else True

        player_id: str = str(record.fields['Player ID']) + record.fields['First Name'] + record.fields['Last Name']
        
        player = PlayerInfoData(
            id=player_id,
            roster_id=record.fields['Player ID'],
            team_id=record.fields['Team ID'],
            first_name=record.fields['First Name'],
            last_name=record.fields['Last Name'],
            hometown_desc=record.fields['Hometown Desc'],
            play_recognition=record.fields['Play Recognition'],
            press=record.fields['Press'],
            power_moves=record.fields['Power Moves'],
            kick_accuracy=record.fields['Kick Accuracy'],
            redshirt=is_redshirt,
            player_year=readable_year,
            jersey_number=record.fields['Jersey #'],
            throwing_power=record.fields['Throwing Power'],
            throwing_accuracy=record.fields['Throwing Accuracy'],
            overall=record.fields['Overall'],
            agility=record.fields['Agility'],
            stamina=record.fields['Stamina'],
            acceleration=record.fields['Acceleration'],
            pursuit=record.fields['Pursuit'],
            route_running=record.fields['Route Running'],
            speed=record.fields['Speed'],
            trucking=record.fields['Trucking'],
            ball_carrier_vision=record.fields['Ball Carrier Vision'],
            catch_in_traffic=record.fields['Catch In Traffic'],
            block_shedding=record.fields['Block Shedding'],
            strength=record.fields['Strength'],
            catch=record.fields['Catch'],
            injury=record.fields['Injury'],
            tackling=record.fields['Tackling'],
            pass_blocking=record.fields['Pass Blocking'],
            run_blocking=record.fields['Run Blocking'],
            break_tackle=record.fields['Break Tackle'],
            impact_blocking=record.fields['Impact Blocking'],
            jump=record.fields['Jump'],
            carry=record.fields['Carry'],
            stiff_arm=record.fields['Stiff Arm'],
            kick_power=record.fields['Kick Power'],
            awareness=record.fields['Awareness'],
            release=record.fields['Release'],
            position=readable_position,
            spec_catch=record.fields['Spec Catch'],
            elusiveness=record.fields['Elusiveness'],
            height=readable_height,
            spin_move=record.fields['Spin Move'],
            weight=readable_weight,
            hit_power=record.fields['Hit Power'],
            kick_return=record.fields['Kick Return'],
            man_coverage=record.fields['Man Coverage'],
            zone_coverage=record.fields['Zone Coverage'],
            finesse_moves=record.fields['Finesse Moves'],
            juke_move=record.fields['Juke Move'],
            is_active=True
        )

        player_query: PlayerInfoData = session.query(PlayerInfoData).where(
                PlayerInfoData.id == player.id
            ).scalar()

        if not player_query:
            session.add(player)
            
        else:
            player_query.first_name=player.first_name
            player_query.last_name=player.last_name
            player_query.position=player.position
            player_query.hometown_desc=player.hometown_desc
            player_query.play_recognition=player.play_recognition
            player_query.press=player.press
            player_query.power_moves=player.power_moves
            player_query.kick_accuracy=player.kick_accuracy
            player_query.redshirt=player.redshirt
            player_query.player_year=player.player_year
            player_query.jersey_number=player.jersey_number
            player_query.throwing_power=player.throwing_power
            player_query.throwing_accuracy=player.throwing_accuracy
            player_query.overall=player.overall
            player_query.agility=player.agility
            player_query.stamina=player.stamina
            player_query.acceleration=player.acceleration
            player_query.pursuit=player.pursuit
            player_query.route_running=player.route_running
            player_query.speed=player.speed
            player_query.trucking=player.trucking
            player_query.ball_carrier_vision=player.ball_carrier_vision
            player_query.catch_in_traffic=player.catch_in_traffic
            player_query.block_shedding=player.block_shedding
            player_query.strength=player.strength
            player_query.catch=player.catch
            player_query.injury=player.injury
            player_query.tackling=player.tackling
            player_query.pass_blocking=player.pass_blocking
            player_query.run_blocking=player.run_blocking
            player_query.break_tackle=player.break_tackle
            player_query.impact_blocking=player.impact_blocking
            player_query.jump=player.jump
            player_query.carry=player.carry
            player_query.stiff_arm=player.stiff_arm
            player_query.kick_power=player.kick_power
            player_query.awareness=player.awareness
            player_query.release=player.release
            player_query.spec_catch=player.spec_catch
            player_query.elusiveness=player.elusiveness
            player_query.height=player.height
            player_query.spin_move=player.spin_move
            player_query.weight=player.weight
            player_query.hit_power=player.hit_power
            player_query.kick_return=player.kick_return
            player_query.man_coverage=player.man_coverage
            player_query.zone_coverage=player.zone_coverage
            player_query.finesse_moves=player.finesse_moves
            player_query.juke_move=player.juke_move
            player_query.is_active=player.is_active

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
