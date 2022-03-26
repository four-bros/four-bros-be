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
        
        # Convert unintelligible values to readable values
        readable_position = ncaa_dynasty.position_number_to_text(record.fields['Position'])
        readable_height = ncaa_dynasty.height_converter(record.fields['Height'])
        readable_weight = ncaa_dynasty.weight_converter(record.fields['Weight'])
        readable_year = ncaa_dynasty.player_year_converter(record.fields['Year'])
        
        is_redshirt = False if record.fields['Redshirt'] == 0 else True
        
        player = PlayerInfoData(
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

        player_query: PlayerInfoData = session.query(PlayerInfoData).where(
            PlayerInfoData.id == player.id).scalar()

        if not player_query:
            session.add(player)
            session.flush()
            
        else:
            update(PlayerInfoData).where(PlayerInfoData.id == player.id).values(
                id=player.id,
                team_id=player.team_id,
                first_name=player.first_name,
                last_name=player.last_name,
                hometown_desc=player.hometown_desc,
                play_recognition=player.play_recognition,
                press=player.press,
                power_moves=player.power_moves,
                kick_accuracy=player.kick_accuracy,
                redshirt=player.redshirt,
                player_year=player.player_year,
                jersey_number=player.jersey_number,
                throwing_power=player.throwing_power,
                throwing_accuracy=player.throwing_accuracy,
                overall=player.overall,
                agility=player.agility,
                stamina=player.stamina,
                acceleration=player.acceleration,
                pursuit=player.pursuit,
                route_running=player.route_running,
                speed=player.speed,
                trucking=player.trucking,
                ball_carrier_vision=player.ball_carrier_vision,
                catch_in_traffic=player.catch_in_traffic,
                block_shedding=player.block_shedding,
                strength=player.strength,
                catch=player.catch,
                injury=player.injury,
                tackling=player.tackling,
                pass_blocking=player.pass_blocking,
                run_blocking=player.run_blocking,
                break_tackle=player.break_tackle,
                impact_blocking=player.impact_blocking,
                jump=player.jump,
                carry=player.carry,
                stiff_arm=player.stiff_arm,
                kick_power=player.kick_power,
                awareness=player.awareness,
                release=player.release,
                position=player.position,
                spec_catch=player.spec_catch,
                elusiveness=player.elusiveness,
                height=player.height,
                spin_move=player.spin_move,
                weight=player.weight,
                hit_power=player.hit_power,
                kick_return=player.kick_return,
                man_coverage=player.man_coverage,
                zone_coverage=player.zone_coverage,
                finesse_moves=player.finesse_moves,
                juke_move=player.juke_move,
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
