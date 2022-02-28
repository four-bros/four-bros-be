import ncaa_dynasty
from sqlalchemy.sql.expression import update
from uuid import uuid4

from src.constants import session

from src.utils.helpers import(
    _convert_stats_year
)
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.WeekYearData import WeekYearData


################################################
######## insert player data functions ##########
################################################
def insert_season_def_stats_into_db(def_stats):

    week_year: WeekYearData = session.query(WeekYearData).first()
    current_year = week_year.year

    for i, value in enumerate(def_stats):

        record = def_stats[i]
        
        readable_year = _convert_stats_year(record.fields['Year'])
        
        total_tackles = record.fields['Solo Tkls'] + record.fields['Asst. Tkls']
        total_sacks = record.fields['Half A Sack'] + record.fields['Sacks']

        new_id = str(uuid4())
        
        new_player = SeasonDefensiveStatsData(
            id=new_id,
            player_id=record.fields['Player ID'],
            long_int_ret=record.fields['Long INT Ret'],
            sacks=record.fields['Sacks'],
            year=readable_year,
            forced_fumbles=record.fields['Forced Fumbles'],
            solo_tkls=record.fields['Solo Tkls'],
            safeties=record.fields['Safties'],
            pass_def=record.fields['Pass Def.'],
            blocked_kicks=record.fields['Blocked Kicks'],
            tfl=record.fields['TFL'],
            ints_made=record.fields['INTs Made'],
            games_played=record.fields['Games Played'],
            fumbles_rec=record.fields['Fumbles Rec.'],
            half_a_sack=record.fields['Half A Sack'],
            asst_tkls=record.fields['Asst. Tkls'],
            def_tds=record.fields['Def. TDs'],
            fum_rec_yards=record.fields['Fum. Rec. Yards'],
            int_ret_yards=record.fields['INT Ret. Yards'],
            total_tkls=total_tackles,
            total_sacks=total_sacks
        )

        # Query table to determine if player has a record or not
        player: SeasonDefensiveStatsData = session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == new_player.player_id,
            SeasonDefensiveStatsData.year == current_year
        ).scalar()

        if not player:
            session.add(new_player)
            session.flush()
        else:
            update(SeasonDefensiveStatsData).where(SeasonDefensiveStatsData.player_id == new_player.player_id).values(
                player_id=new_player.player_id,
                long_int_ret=new_player.long_int_ret,
                sacks=new_player.sacks,
                year=new_player.year,
                forced_fumbles=new_player.forced_fumbles,
                solo_tkls=new_player.solo_tkls,
                safeties=new_player.safeties,
                pass_def=new_player.pass_def,
                blocked_kicks=new_player.blocked_kicks,
                tfl=new_player.tfl,
                ints_made=new_player.ints_made,
                games_played=new_player.games_played,
                fumbles_rec=new_player.fumbles_rec,
                half_a_sack=new_player.half_a_sack,
                asst_tkls=new_player.asst_tkls,
                def_tds=new_player.def_tds,
                fum_rec_yards=new_player.fum_rec_yards,
                int_ret_yards=new_player.int_ret_yards,
                total_tkls=new_player.total_tkls
            )
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_season_kicking_stats_into_db(kicking_stats):

    week_year: WeekYearData = session.query(WeekYearData).first()
    current_year = week_year.year
    
    for i, value in enumerate(kicking_stats):

        record = kicking_stats[i]
        new_id = str(uuid4())
        readable_year = _convert_stats_year(record.fields['Year'])
        fg_pct = round(
            record.fields['FG Made'] / record.fields['FG Att.'] * 100\
                if record.fields['FG Att.'] != 0 else 0,
            1)
        xp_pct = round(
            record.fields['XP Made'] / record.fields['XP Att.'] * 100\
                if record.fields['XP Att.'] != 0 else 0,
            1)
        fg_50_plus_pct = round(
            record.fields['FG Made 50+'] / record.fields['FG Att. 50+'] * 100\
                if record.fields['FG Att. 50+'] != 0 else 0,
            1)
        punt_avg = round(
            record.fields['Total Punt Yards'] / record.fields['# Punts']\
                if record.fields['# Punts'] != 0 else 0, 
            1)
        
        new_player = SeasonKickingStatsData(
            id=new_id,
            player_id=record.fields['Player ID'],
            fg_made_17_29=record.fields['FG Made 17-29'],
            fg_att_17_29=record.fields['FG Att. 17-29'],
            long_fg=record.fields['Long FG'],
            ko_touchbacks=record.fields['KO Touchbacks'],
            long_punt=record.fields['Long Punt'],
            xp_att=record.fields['XP Att.'],
            year=readable_year,
            punts_blocked=record.fields['Punts Blocked'],
            fg_att=record.fields['FG Att.'],
            total_punt_yards=record.fields['Total Punt Yards'],
            xp_blocked=record.fields['XP Blocked'],
            fg_blocked=record.fields['FG Blocked'],
            fg_att_40_49=record.fields['FG Att. 40-49'],
            fg_made_40_49=record.fields['FG Made 40-49'],
            fg_att_30_39=record.fields['FG Att. 30-39'],
            fg_made_30_39=record.fields['FG Att. 30-39'],
            fg_att_50_plus=record.fields['FG Att. 50+'],
            fg_made_50_plus=record.fields['FG Made 50+'],
            punt_touchbacks=record.fields['Punt Touchbacks'],
            games_played=record.fields['Games Played'],
            kickoffs=record.fields['Kickoffs'],
            xp_made=record.fields['XP Made'],
            net_punting=record.fields['Net Punting'],
            fg_made=record.fields['FG Made'],
            number_punts=record.fields['# Punts'],
            inside_twenty=record.fields['Inside 20'],
            fg_pct=fg_pct,
            xp_pct=xp_pct,
            fg_50_plus_pct=fg_50_plus_pct,
            punt_avg=punt_avg
        )

        player: SeasonKickingStatsData = session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == new_player.player_id,
            SeasonKickingStatsData.year == current_year
        ).scalar()
        
        if not player:
            session.add(new_player)
            session.flush()
        else:
            update(SeasonKickingStatsData).where(SeasonKickingStatsData.player_id == new_player.player_id).values(
                player_id=new_player.player_id,
                fg_made_17_29=new_player.fg_made_17_29,
                fg_att_17_29=new_player.fg_att_17_29,
                long_fg=new_player.long_fg,
                ko_touchdowns=new_player.ko_touchbacks,
                long_punt=new_player.long_punt,
                xp_att=new_player.xp_att,
                year=new_player.year,
                punts_blocked=new_player.punts_blocked,
                fg_att=new_player.fg_att,
                total_punt_yards=new_player.total_punt_yards,
                xp_blocked=new_player.xp_blocked,
                fg_blocked=new_player.fg_blocked,
                fg_att_40_49=new_player.fg_att_40_49,
                fg_made_40_49=new_player.fg_made_40_49,
                fg_att_30_39=new_player.fg_att_30_39,
                fg_made_30_39=new_player.fg_made_30_39,
                fg_att_50_plus=new_player.fg_att_50_plus,
                fg_made_50_plus=new_player.fg_made_50_plus,
                punt_touchbacks=new_player.punt_touchbacks,
                games_played=new_player.games_played,
                kickoffs=new_player.kickoffs,
                xp_made=new_player.xp_made,
                net_punting=new_player.net_punting,
                fg_made=new_player.fg_made,
                number_punts=new_player.number_punts,
                inside_twenty=new_player.inside_twenty
            )
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_season_off_stats_into_db(off_stats):

    week_year: WeekYearData = session.query(WeekYearData).first()
    current_year = week_year.year

    for i, value in enumerate(off_stats):
        record = off_stats[i]
        
        readable_year = _convert_stats_year(record.fields['Year'])

        new_id = str(uuid4())
        
        pass_yp_attempt = round(
            record.fields['Pass. Yards'] / record.fields['Pass Att.']\
                if record.fields['Pass Att.'] != 0 else 0,
                1
            )
        pass_yp_game = round(
            record.fields['Pass. Yards'] / record.fields['Games Played']\
                if record.fields['Games Played'] != 0 else 0, 
                1
            )
        rush_yp_carry = round(
            record.fields['Rush Yards'] / record.fields['Rush Att.']\
                if record.fields['Rush Att.'] != 0 else 0,
                1
            )
        rush_yp_game = round(
            record.fields['Rush Yards'] / record.fields['Games Played']\
                if record.fields['Games Played'] != 0 else 0,
                1
            )
        rec_yp_catch = round(
            record.fields['Rec. Yards'] / record.fields['Receptions']\
                if record.fields['Receptions'] != 0 else 0,
                1
            )
        rec_yp_game = round(
            record.fields['Rec. Yards'] / record.fields['Games Played']\
                if record.fields['Games Played'] != 0 else 0,
                1
            )
        pass_rating_calc = (
            0 if record.fields['Pass Att.'] == 0 else \
            ((8.4 * record.fields['Pass. Yards']) + (330 * record.fields['Pass. TDs']) + \
            (100 * record.fields['Completions']) - (200 * record.fields['INTs'])) / record.fields['Pass Att.']
            )
        pass_rating = round(pass_rating_calc, 1)

        # get ReturnStats for total stats purposes (yards, TDs, etc)
        return_stats: SeasonReturnStatsData = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == record.fields['Player ID'],
            SeasonReturnStatsData.year == current_year
        ).scalar()

        # Calculate total stats
        total_yards = 0
        total_tds = 0
        total_ypg = 0

        if return_stats:
            total_yards = sum([
                record.fields['Pass. Yards'], record.fields['Rec. Yards'], record.fields['Rush Yards'], 
                return_stats.kr_yds, return_stats.pr_yds]
            )
            total_tds = sum([
                record.fields['Pass. TDs'], record.fields['Rec. TDs'], record.fields['Rush TDs'],
                return_stats.kr_tds, return_stats.pr_tds
            ])
            total_ypg = round(
                0 if record.fields['Games Played'] == 0\
                    else total_yards / record.fields['Games Played'],
                1)
        else:
            total_yards = sum([
                record.fields['Pass. Yards'], record.fields['Rec. Yards'], record.fields['Rush Yards']
                ])
            total_tds = sum([
                record.fields['Pass. TDs'], record.fields['Rec. TDs'], record.fields['Rush TDs']
                ])
            total_ypg = round(
                0 if record.fields['Games Played'] == 0\
                    else total_yards / record.fields['Games Played'],
                1)

        new_player = SeasonOffensiveStatsData(
            id=new_id,
            player_id=record.fields['Player ID'],
            pass_yards=record.fields['Pass. Yards'],
            longest_rec=record.fields['Longest Rec.'],
            longest_pass=record.fields['Longest Pass'],
            longest_run=record.fields['Longest Run'],
            year=readable_year,
            receptions=record.fields['Receptions'],
            sacked=record.fields['Sacked'],
            rec_yards=record.fields['Rec. Yards'],
            rush_yards=record.fields['Rush Yards'],
            yac=record.fields['Y.A.C.'],
            pass_tds=record.fields['Pass. TDs'],
            games_played=record.fields['Games Played'],
            rec_tds=record.fields['Rec. TDs'],
            rush_tds=record.fields['Rush TDs'],
            ya_contact=record.fields['Y.A. Contact'],
            completions=record.fields['Completions'],
            ints=record.fields['INTs'],
            drops=record.fields['Drops'],
            pass_att=record.fields['Pass Att.'],
            rush_att=record.fields['Rush Att.'],
            broke_tkls=record.fields['Broke Tkls.'],
            fumbles=record.fields['Fumbles'],
            twenty_plus_yd_runs=record.fields['20+ yd. Runs'],
            pass_yp_attempt=pass_yp_attempt,
            pass_yp_game=pass_yp_game,
            rush_yp_carry=rush_yp_carry,
            rush_yp_game=rush_yp_game,
            rec_yp_catch=rec_yp_catch,
            rec_yp_game=rec_yp_game,
            pass_rating=pass_rating,
            total_yards=total_yards,
            total_tds=total_tds,
            total_ypg=total_ypg
        )
        

        player: SeasonOffensiveStatsData = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == new_player.player_id,
            SeasonOffensiveStatsData.year == current_year
        ).scalar()

        if not player:
            session.add(new_player)
            session.flush()
        else:
            update(SeasonOffensiveStatsData).where(SeasonOffensiveStatsData.player_id == new_player.player_id).values(
                player_id=new_player.player_id,
                pass_yards=new_player.pass_yards,
                longest_rec=new_player.longest_rec,
                longest_pass=new_player.longest_pass,
                longest_run=new_player.longest_run,
                year=new_player.year,
                receptions=new_player.receptions,
                sacked=new_player.sacked,
                rec_yards=new_player.rec_yards,
                rush_yards=new_player.rush_yards,
                yac=new_player.yac,
                pass_tds=new_player.pass_tds,
                games_played=new_player.games_played,
                rec_tds=new_player.rec_tds,
                rush_tds=new_player.rush_tds,
                ya_contact=new_player.ya_contact,
                completions=new_player.completions,
                ints=new_player.ints,
                drops=new_player.drops,
                pass_att=new_player.pass_att,
                rush_att=new_player.rush_att,
                broke_tkls=new_player.broke_tkls,
                fumbles=new_player.fumbles,
                twenty_plus_yd_runs=new_player.twenty_plus_yd_runs,
                pass_yp_attempt=new_player.pass_yp_attempt,
                pass_yp_game=new_player.pass_yp_game,
                rush_yp_carry=new_player.rush_yp_carry,
                rush_yp_game=new_player.rush_yp_game,
                rec_yp_catch=new_player.rec_yp_catch,
                rec_yp_game=new_player.rec_yp_game,
                total_yards=new_player.total_yards,
                total_tds=new_player.total_tds,
                total_ypg=new_player.total_ypg
            )
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
        if (
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


def insert_season_return_stats_into_db(return_stats):

    week_year: WeekYearData = session.query(WeekYearData).first()
    current_year = week_year.year
    
    for i, value in enumerate(return_stats):
        record = return_stats[i]

        new_id = str(uuid4())
        readable_year = _convert_stats_year(record.fields['Year'])
        kr_avg = round(
            record.fields['KR Yds.'] / record.fields['Kick Returns']\
                if record.fields['Kick Returns'] != 0 else 0,
            1
            )
        pr_avg = round(
            record.fields['PR Yds.'] / record.fields['Punt Returns']\
                if record.fields['Punt Returns'] != 0 else 0,
            1
            )
        
        new_player = SeasonReturnStatsData(
            id=new_id,
            player_id=record.fields['Player ID'],
            kick_returns=record.fields['Kick Returns'],
            year=readable_year,
            long_kr=record.fields['Long KR'],
            punt_returns=record.fields['Punt Returns'],
            long_pr=record.fields['Long PR'],
            games_played=record.fields['Games Played'],
            kr_tds=record.fields['KR TDs'],
            pr_tds=record.fields['PR TDs'],
            kr_yds=record.fields['KR Yds.'],
            pr_yds=record.fields['PR Yds.'],
            kr_avg=kr_avg,
            pr_avg=pr_avg
        )
        

        player: SeasonReturnStatsData = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == new_player.player_id,
            SeasonReturnStatsData.year == current_year
        ).scalar()
        
        if not player:
            session.add(new_player)
            session.flush()
            
        else:
            update(SeasonReturnStatsData).where(SeasonReturnStatsData.player_id == new_player.player_id).values(
                player_id=new_player.player_id,
                kick_returns=new_player.kick_returns,
                year=new_player.year,
                long_kr=new_player.long_kr,
                punt_returns=new_player.punt_returns,
                long_pr=new_player.long_pr,
                games_played=new_player.games_played,
                kr_tds=new_player.kr_tds,
                pr_tds=new_player.pr_tds,
                kr_yds=new_player.kr_yds,
                pr_yds=new_player.pr_yds,
                kr_avg=new_player.kr_avg,
                pr_avg=new_player.pr_avg
            )
            session.flush()

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()