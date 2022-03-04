from sqlalchemy import desc
from sqlalchemy.sql.expression import update
from uuid import uuid4

import ncaa_dynasty
from src.constants import session
from src.utils.helpers import(
    _convert_stats_year
)
from src.data_models.CommitsData import CommitsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.WeekYearData import WeekYearData


def insert_commits_into_db(commits):

    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()
    
    for i, value in enumerate(commits):
        record = commits[i]
        
        new_commit = CommitsData(
            stars=record.fields['Stars'],
            name=record.fields['Name'],
            position=record.fields['Position'],
            rank=record.fields['Rank'],
            school=record.fields['School'],
            week=week_year.week,
            year=week_year.year
        )

        commit = session.query(CommitsData).where(
            CommitsData.name == new_commit.name).scalar()
        
        if commit is None:
            session.add(new_commit)
            session.flush()
            
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
        
        # Convert unintelligble values to readable values
        readable_position = ncaa_dynasty.position_number_to_text(record.fields['Position'])
        readable_height = ncaa_dynasty.height_converter(record.fields['Height'])
        readable_weight = ncaa_dynasty.weight_converter(record.fields['Weight'])
        readable_year = ncaa_dynasty.player_year_converter(record.fields['Year'])
        
        is_redshirt = False if record.fields['Redshirt'] == 0 else True
        
        new_player = PlayerInfoData(
            id=record.fields['Player ID'],
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
        )

        player: PlayerInfoData = session.query(PlayerInfoData).filter(
            PlayerInfoData.id == new_player.id).scalar()

        if not player:
            session.add(new_player)
            session.flush()
            
        else:
            update(PlayerInfoData).where(PlayerInfoData.id == new_player.id).values(
                player_id=new_player.id,
                team_id=new_player.team_id,
                first_name=new_player.first_name,
                last_name=new_player.last_name,
                hometown_desc=new_player.hometown_desc,
                play_recognition=new_player.play_recognition,
                press=new_player.press,
                power_moves=new_player.power_moves,
                kick_accuracy=new_player.kick_accuracy,
                redshirt=new_player.redshirt,
                player_year=new_player.player_year,
                jersey_number=new_player.jersey_number,
                throwing_power=new_player.throwing_power,
                throwing_accuracy=new_player.throwing_accuracy,
                overall=new_player.overall,
                agility=new_player.agility,
                stamina=new_player.stamina,
                acceleration=new_player.acceleration,
                pursuit=new_player.pursuit,
                route_running=new_player.route_running,
                speed=new_player.speed,
                trucking=new_player.trucking,
                ball_carrier_vision=new_player.ball_carrier_vision,
                catch_in_traffic=new_player.catch_in_traffic,
                block_shedding=new_player.block_shedding,
                strength=new_player.strength,
                catch=new_player.catch,
                injury=new_player.injury,
                tackling=new_player.tackling,
                pass_blocking=new_player.pass_blocking,
                run_blocking=new_player.run_blocking,
                break_tackle=new_player.break_tackle,
                impact_blocking=new_player.impact_blocking,
                jump=new_player.jump,
                carry=new_player.carry,
                stiff_arm=new_player.stiff_arm,
                kick_power=new_player.kick_power,
                awareness=new_player.awareness,
                release=new_player.release,
                position=new_player.position,
                spec_catch=new_player.spec_catch,
                elusiveness=new_player.elusiveness,
                height=new_player.height,
                spin_move=new_player.spin_move,
                weight=new_player.weight,
                hit_power=new_player.hit_power,
                kick_return=new_player.kick_return,
                man_coverage=new_player.man_coverage,
                zone_coverage=new_player.zone_coverage,
                finesse_moves=new_player.finesse_moves,
                juke_move=new_player.juke_move,
            )
            session.flush()

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_week_year_into_db(week_year):
    
    record = week_year[0]
    
    readable_year = _convert_stats_year(record.fields['Year'])

    new_id = str(uuid4())
    
    new_week_year = WeekYearData(
        id=new_id,
        week=record.fields['Week'],
        year=readable_year
    )

    week_year_query: WeekYearData = session.query(WeekYearData).filter(
        WeekYearData.week == new_week_year.week,
        WeekYearData.year == new_week_year.year
    ).scalar()
    
    if not week_year_query:
        session.add(new_week_year)
        session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
