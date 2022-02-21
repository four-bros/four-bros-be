from typing import List
import ncaa_dynasty
from sqlalchemy.sql.expression import update

from src.constants import(
    session,
    user_teams
)

from helpers import(
    _convert_stats_year,
    _get_player_defensive_stats,
    _get_player_kicking_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_return_stats,
    _get_player_rushing_stats
)
from data_models.CommitsData import CommitsData
from data_models.DefensiveStatsData import DefensiveStatsData
from data_models.KickingStatsData import KickingStatsData
from data_models.OffensiveStatsData import OffensiveStatsData
from data_models.PlayerInfoData import PlayerInfoData
from data_models.ReturnStatsData import ReturnStatsData
from data_models.TeamInfoData import TeamInfoData
from data_models.TeamStatsData import TeamStatsData
from data_models.WeekYearData import WeekYearData
from models.Stats import(
    PlayerDefensiveStats,
    PlayerKickingStats,
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerReturnStats,
    PlayerRushingStats
)


################################################
######## insert player data functions ##########
################################################
def insert_commits_into_db(commits):
    
    for i, value in enumerate(commits):
        record = commits[i]
        
        new_commit = CommitsData(
            stars=record.fields['Stars'],
            name=record.fields['Name'],
            position=record.fields['Position'],
            rank=record.fields['Rank'],
            school=record.fields['School']
        )
        session.flush()

        commit = session.query(CommitsData).where(
            CommitsData.name == new_commit.name).scalar()
        
        if commit is None:
            session.add(new_commit)
            session.flush()
            
        else:
            update(CommitsData).where(CommitsData.name == new_commit.name).values(
                stars=new_commit.stars,
                name=new_commit.name,
                position=new_commit.position,
                rank=new_commit.rank,
                school=new_commit.school
            )
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_def_stats_into_db(def_stats):

    for i, value in enumerate(def_stats):
        

        record = def_stats[i]
        
        readable_year = _convert_stats_year(record.fields['Year'])
        
        total_tackles = record.fields['Solo Tkls'] + record.fields['Asst. Tkls']
        
        new_player = DefensiveStatsData(
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
            total_tkls=total_tackles
        )


        # Query table to determine if player has a record or not
        player: DefensiveStatsData = session.query(DefensiveStatsData).filter(
            DefensiveStatsData.player_id == new_player.player_id).scalar()

        if player is None:
            session.add(new_player)
            session.flush()
        else:
            update(DefensiveStatsData).where(DefensiveStatsData.player_id == new_player.player_id).values(
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


def insert_kicking_stats_into_db(kicking_stats):
    
    for i, value in enumerate(kicking_stats):
        record = kicking_stats[i]
        
        readable_year = _convert_stats_year(record.fields['Year'])
        
        new_player = KickingStatsData(
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
            inside_twenty=record.fields['Inside 20']
        )

        player = session.query(KickingStatsData).filter(
            KickingStatsData.player_id == new_player.player_id
        ).scalar()
        
        if player is None:
            session.add(new_player)
            session.flush()
        else:
            update(KickingStatsData).where(KickingStatsData.player_id == new_player.player_id).values(
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


def insert_off_stats_into_db(off_stats):
    
    for i, value in enumerate(off_stats):
        record = off_stats[i]
        
        readable_year = _convert_stats_year(record.fields['Year'])
        
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
        
        new_player = OffensiveStatsData(
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
            pass_rating=pass_rating
        )
        

        player: OffensiveStatsData = session.query(OffensiveStatsData).filter(
            OffensiveStatsData.player_id == new_player.player_id).scalar()

        if player is None:
            session.add(new_player)
            session.flush()
        else:
            update(OffensiveStatsData).where(OffensiveStatsData.player_id == new_player.player_id).values(
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
                rec_yp_game=new_player.rec_yp_game
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

        if player is None:
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


def insert_return_stats_into_db(return_stats):
    
    for i, value in enumerate(return_stats):
        record = return_stats[i]
        
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
        
        new_player = ReturnStatsData(
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
        

        player = session.query(ReturnStatsData).filter(ReturnStatsData.player_id == new_player.player_id).scalar()
        
        if player is None:
            session.add(new_player)
            session.flush()
            
        else:
            update(ReturnStatsData).where(ReturnStatsData.player_id == new_player.player_id).values(
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


def insert_team_info_into_db(team_info):
    
    for i, value in enumerate(team_info):
        
        record = team_info[i]
        # Skip over players from duplicate teams
        if (
            record.fields['Team ID'] == 300 or
            record.fields['Team ID'] == 400 or
            record.fields['Team ID'] == 1023
        ):
            continue
        
        new_team = TeamInfoData(
            id=record.fields['Team ID'],
            team_name=record.fields['Team Name'],
            team_short_name=record.fields['Team Short Name'],
            is_user=True if record.fields['Team Name'] in user_teams else False,
            coachs_poll_1st_votes=record.fields["Coach's Poll 1st Votes"],
            nickname=record.fields['Nickname'],
            wins=record.fields['Wins'],
            bcs_rank=record.fields['BCS Rank'],
            coachs_poll_rank=record.fields["Coach's Poll Rank"],
            media_poll_rank=record.fields['Media Poll Rank'],
            losses=record.fields['Losses'],
            media_poll_points=record.fields['Media Poll Points'],
            coachs_poll_points=record.fields["Coach's Poll Points"],
        )

        team: TeamInfoData = session.query(TeamInfoData).filter(
            TeamInfoData.id == new_team.id).scalar()
        
        if team is None:
            session.add(new_team)
            session.flush()
        else:
            update(TeamInfoData).where(TeamInfoData.id == new_team.id).values(
                id=new_team.id,
                team_name=new_team.team_name,
                team_short_name=new_team.team_short_name,
                coachs_poll_1st_votes=new_team.coachs_poll_1st_votes,
                nickname=new_team.nickname,
                wins=new_team.wins,
                bcs_rank=new_team.bcs_rank,
                coachs_poll_rank=new_team.coachs_poll_rank,
                media_poll_rank=new_team.media_poll_rank,
                losses=new_team.losses,
                media_poll_points=new_team.media_poll_points,
                coachs_poll_points=new_team.coachs_poll_points,
            )
        
        try:
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()


def insert_week_year_into_db(week_year):
    
    record = week_year[0]
    
    readable_year = _convert_stats_year(record.fields['Year'])
    
    new_week_year = WeekYearData(
        week=record.fields['Week'],
        year=readable_year
    )

    week_year_query: WeekYearData = session.query(WeekYearData).filter(
        WeekYearData.week == new_week_year.week,
        WeekYearData.year == new_week_year.year
    ).scalar()
    
    if week_year_query is None:
        session.add(new_week_year)
        session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


################################################
######### insert team stats function ###########
################################################
def insert_team_stats_into_db():

    all_teams_info: List[TeamInfoData] = session.query(TeamInfoData).all()
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()

    for team in all_teams_info:
        # Skip over players from duplicate teams
        if (
            team.id == 300 or
            team.id == 400 or
            team.id == 1023
        ):
            continue

        # Grab all player data for each team
        def_data = session.query(PlayerInfoData, DefensiveStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.id == DefensiveStatsData.player_id,
                DefensiveStatsData.year == week_year.year
            ).all()
        off_data = session.query(PlayerInfoData, OffensiveStatsData).filter(
            PlayerInfoData.team_id == team.id,
            PlayerInfoData.id == OffensiveStatsData.player_id,
            OffensiveStatsData.year == week_year.year,
            # filter out incorrect data
            OffensiveStatsData.rush_yards < 16000
            ).all()
        ret_data = session.query(PlayerInfoData, ReturnStatsData).filter(
                PlayerInfoData.team_id == team.id,
                PlayerInfoData.id == ReturnStatsData.player_id,
                ReturnStatsData.year == week_year.year
                ).all()
        kick_data = session.query(PlayerInfoData, KickingStatsData).filter(
                PlayerInfoData.team_id == team.id,
                KickingStatsData.player_id == PlayerInfoData.id,
                KickingStatsData.year == week_year.year
            ).all()   

        # Convert data to models for data manipulation
        def_stats: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in def_data]
        kick_stats: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in kick_data]
        pass_stats: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in off_data]
        rush_stats: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in off_data]
        rec_stats: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in off_data]
        return_stats: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in ret_data]
        
        # compile all TDs and TD points
        passing_tds = sum([p.passing_stats.pass_tds for p in pass_stats])
        rushing_tds = sum([p.rushing_stats.rush_tds for p in rush_stats])
        receiving_tds = sum([p.receiving_stats.rec_tds for p in rec_stats])
        def_tds = sum([p.defensive_stats.def_tds for p in def_stats])
        kr_tds = sum([p.return_stats.kr_tds for p in return_stats])
        pr_tds = sum([p.return_stats.pr_tds for p in return_stats])
        td_points = sum([passing_tds, rushing_tds, def_tds, kr_tds, pr_tds]) * 6
        
        # compile all FGs and XP points
        fgs = sum([p.kicking_stats.fg_made for p in kick_stats])
        xps = sum([p.kicking_stats.xp_made for p in kick_stats])
        kick_points = sum([fgs * 3, xps])
        
        # calculate total points, ppg
        def_stats_sorted_by_gp: List[PlayerDefensiveStats] = sorted(def_stats, key=lambda p: p.defensive_stats.games_played, reverse=True)
        games_played = 1
        if len(def_stats_sorted_by_gp) > 0:
            games_played = def_stats_sorted_by_gp[0].defensive_stats.games_played
        if games_played is 0:
            games_played += 1
        total_points = sum([td_points, kick_points])
        ppg = round(total_points / games_played, 1)
        
        # calculate pass, rush, rec. total yards and YPG
        pass_yards = sum([p.passing_stats.pass_yards for p in pass_stats])
        pass_ypg = round(pass_yards / games_played, 1)
        rush_yards = sum([p.rushing_stats.rush_yards for p in rush_stats])
        rush_ypg = round(rush_yards / games_played, 1)
        rec_yards = sum([p.receiving_stats.rec_yards for p in rec_stats])
        rec_ypg = round(rec_yards / games_played, 1)
        
        # calculate defensive stat totals
        sacks = sum([p.defensive_stats.sacks for p in def_stats])
        ints = sum([p.defensive_stats.ints_made for p in def_stats])
        ff = sum([p.defensive_stats.forced_fumbles for p in def_stats])
        fr = sum([p.defensive_stats.fumbles_rec for p in def_stats])
        pass_def = sum([p.defensive_stats.pass_def for p in def_stats])
        safeties = sum([p.defensive_stats.safeties for p in def_stats])
        
        # calculate KR and PR yards
        kr_yds = sum([p.return_stats.kr_yds for p in return_stats])
        pr_yds = sum([p.return_stats.pr_yds for p in return_stats])
        
        new_team = TeamStatsData(
            id=team.id,
            total_points=total_points,
            ppg=ppg,
            pass_yds=pass_yards,
            pass_ypg=pass_ypg,
            pass_tds=passing_tds,
            rush_yds=rush_yards,
            rush_tds=rushing_tds,
            rush_ypg=rush_ypg,
            rec_yds=rec_yards,
            rec_ypg=rec_ypg,
            rec_tds=receiving_tds,
            sacks=sacks,
            ints=ints,
            ff=ff,
            fr=fr,
            pass_def=pass_def,
            safeties=safeties,
            def_tds=def_tds,
            kr_yds=kr_yds,
            kr_tds=kr_tds,
            pr_yds=pr_yds,
            pr_tds=pr_tds
        )

        # query DB to see if team_stat exists
        team: TeamStatsData = session.query(TeamStatsData).filter(
            TeamStatsData.id == new_team.id).scalar()
        
        if team is None:
            session.add(new_team)
        else:
            update(TeamStatsData).where(TeamStatsData.id == new_team.id).values(
                id=new_team.id,
                total_points=new_team.total_points,
                ppg=new_team.ppg,
                pass_yds=new_team.pass_yds,
                pass_ypg=new_team.pass_ypg,
                pass_tds=new_team.pass_tds,
                rush_yds=new_team.rush_yds,
                rush_ypg=new_team.rush_ypg,
                rush_tds=new_team.rush_tds,
                rec_yds=new_team.rec_yds,
                rec_ypg=new_team.rec_ypg,
                rec_tds=new_team.rec_tds,
                sacks=new_team.sacks,
                ints=new_team.ints,
                ff=new_team.ff,
                fr=new_team.fr,
                pass_def=new_team.pass_def,
                safeties=new_team.safeties,
                def_tds=new_team.def_tds,
                kr_yds=new_team.kr_yds,
                kr_tds=new_team.kr_tds,
                pr_yds=new_team.pr_yds,
                pr_tds=new_team.pr_tds
            )
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
