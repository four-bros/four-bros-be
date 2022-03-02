from typing import List
from uuid import uuid4

from sqlalchemy import desc

from src.constants import session
from src.data_models.GameDefensiveStatsData import GameDefensiveStatsData
from src.data_models.GameKickingStatsData import GameKickingStatsData
from src.data_models.GameOffensiveStatsData import GameOffensiveStatsData
from src.data_models.GameReturnStatsData import GameReturnStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.WeekYearData import WeekYearData
from src.models.Stats import (
    DefensiveStats,
    KickingStats,
    PassingStats,
    ReceivingStats,
    ReturnStats,
    RushingStats,
    TotalStats
)
from src.utils.career_stats import (
    _compile_career_defensive_stats,
    _compile_career_kicking_stats,
    _compile_career_passing_stats,
    _compile_career_receiving_stats,
    _compile_career_return_stats,
    _compile_career_rushing_stats,
    _compile_career_total_stats,
)
from src.utils.season_stats import (
    _get_defensive_stats,
    _get_kicking_stats,
    _get_passing_stats,
    _get_receiving_stats,
    _get_return_stats,
    _get_rushing_stats,
    _get_total_stats
)


def insert_game_def_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()
    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    for player in players:

        def_stats_data: List[SeasonDefensiveStatsData] = session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == player.id,
            SeasonDefensiveStatsData.year == week_year.year
        ).scalar()

        # Skip over players that don't have kicking stats
        if not def_stats_data:
            continue

        season_defense_stats: DefensiveStats = _get_defensive_stats(def_stats_data)
        
        new_id = str(uuid4())

        # Check for prior week offensive stats
        prior_def_stats_data: GameDefensiveStatsData = session.query(GameDefensiveStatsData).where(
            GameDefensiveStatsData.player_id == player.id,
            GameDefensiveStatsData.year == week_year.year
            
        ).all()

        if not prior_def_stats_data and def_stats_data:

            game_stats: GameDefensiveStatsData = GameDefensiveStatsData(
                id=new_id,
                player_id=player.id,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                long_int_ret=season_defense_stats.long_int_ret,
                sacks=season_defense_stats.sacks,
                forced_fumbles=season_defense_stats.forced_fumbles,
                solo_tkls=season_defense_stats.solo_tkls,
                safeties=season_defense_stats.safeties,
                pass_def=season_defense_stats.pass_def,
                blocked_kicks=season_defense_stats.blocked_kicks,
                tfl=season_defense_stats.tfl,
                ints_made=season_defense_stats.ints_made,
                fumbles_rec=season_defense_stats.fumbles_rec,
                half_a_sack=season_defense_stats.half_a_sack,
                asst_tkls=season_defense_stats.asst_tkls,
                def_tds=season_defense_stats.def_tds,
                fum_rec_yards=season_defense_stats.fum_rec_yards,
                int_ret_yards=season_defense_stats.int_ret_yards,
                total_tkls=season_defense_stats.total_tkls,
                total_sacks=season_defense_stats.total_sacks
            )
            session.add(game_stats)
            session.flush()

        else:

            prior_def_stats: DefensiveStats = _compile_career_defensive_stats(prior_def_stats_data)

            long_int_ret = season_defense_stats.long_int_ret - prior_def_stats.long_int_ret
            sacks = season_defense_stats.sacks - prior_def_stats.sacks
            forced_fumbles = season_defense_stats.forced_fumbles - prior_def_stats.forced_fumbles
            solo_tkls = season_defense_stats.solo_tkls - prior_def_stats.solo_tkls
            safeties = season_defense_stats.safeties - prior_def_stats.safeties
            pass_def = season_defense_stats.pass_def - prior_def_stats.pass_def
            blocked_kicks = season_defense_stats.blocked_kicks - prior_def_stats.blocked_kicks
            tfl = season_defense_stats.tfl - prior_def_stats.tfl
            ints_made = season_defense_stats.ints_made - prior_def_stats.ints_made
            fumbles_rec = season_defense_stats.fumbles_rec - prior_def_stats.fumbles_rec
            half_a_sack = season_defense_stats.half_a_sack - prior_def_stats.half_a_sack
            asst_tkls = season_defense_stats.asst_tkls - prior_def_stats.asst_tkls
            def_tds = season_defense_stats.def_tds - prior_def_stats.def_tds
            fum_rec_yards = season_defense_stats.fum_rec_yards - prior_def_stats.fum_rec_yards
            int_ret_yards = season_defense_stats.int_ret_yards - prior_def_stats.int_ret_yards
            total_tkls = season_defense_stats.total_tkls - prior_def_stats.total_tkls
            total_sacks = season_defense_stats.total_sacks- prior_def_stats.total_sacks

            game_stats = GameDefensiveStatsData(
                id=new_id,
                player_id=player.id,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                long_int_ret=long_int_ret,
                sacks=sacks,
                forced_fumbles=forced_fumbles,
                solo_tkls=solo_tkls,
                safeties=safeties,
                pass_def=pass_def,
                blocked_kicks=blocked_kicks,
                tfl=tfl,
                ints_made=ints_made,
                fumbles_rec=fumbles_rec,
                half_a_sack=half_a_sack,
                asst_tkls=asst_tkls,
                def_tds=def_tds,
                fum_rec_yards=fum_rec_yards,
                int_ret_yards=int_ret_yards,
                total_tkls=total_tkls,
                total_sacks=total_sacks
            )

            session.add(game_stats)
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_game_kick_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()
    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    for player in players:

        kicking_stats_data: List[SeasonKickingStatsData] = session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == player.id,
            SeasonKickingStatsData.year == week_year.year
        ).scalar()

        # Skip over players that don't have kicking stats
        if not kicking_stats_data:
            continue

        season_kicking_stats: KickingStats = _get_kicking_stats(kicking_stats_data)
        
        new_id = str(uuid4())

        # Check for prior week offensive stats
        prior_kick_stats_data: GameKickingStatsData = session.query(GameKickingStatsData).where(
            GameKickingStatsData.player_id == player.id,
            GameKickingStatsData.year == week_year.year
        ).all()

        if not prior_kick_stats_data and kicking_stats_data:

            game_stats: GameKickingStatsData = GameKickingStatsData(
                id=new_id,
                player_id=player.id,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                fg_made_17_29=season_kicking_stats.fg_made_17_29,
                fg_att_17_29=season_kicking_stats.fg_att_17_29,
                long_fg=season_kicking_stats.long_fg,
                ko_touchbacks=season_kicking_stats.ko_touchbacks,
                long_punt=season_kicking_stats.long_punt,
                xp_att=season_kicking_stats.xp_att,
                punts_blocked=season_kicking_stats.punts_blocked,
                fg_att=season_kicking_stats.fg_att,
                total_punt_yards=season_kicking_stats.total_punt_yards,
                xp_blocked=season_kicking_stats.xp_blocked,
                fg_blocked=season_kicking_stats.fg_blocked,
                fg_att_40_49=season_kicking_stats.fg_att_40_49,
                fg_made_40_49=season_kicking_stats.fg_made_40_49,
                fg_att_30_39=season_kicking_stats.fg_att_30_39,
                fg_made_30_39=season_kicking_stats.fg_made_30_39,
                fg_att_50_plus=season_kicking_stats.fg_att_50_plus,
                fg_made_50_plus=season_kicking_stats.fg_made_50_plus,
                punt_touchbacks=season_kicking_stats.punt_touchbacks,
                kickoffs=season_kicking_stats.kickoffs,
                xp_made=season_kicking_stats.xp_made,
                net_punting=season_kicking_stats.net_punting,
                fg_made=season_kicking_stats.fg_made,
                number_punts=season_kicking_stats.number_punts,
                inside_twenty=season_kicking_stats.inside_twenty,
                fg_pct=season_kicking_stats.fg_pct,
                xp_pct=season_kicking_stats.xp_pct,
                fg_50_plus_pct=season_kicking_stats.fg_50_plus_pct,
                punt_avg=season_kicking_stats.punt_avg
            )
            session.add(game_stats)
            session.flush()

        else:

            prior_kick_stats: KickingStats = _compile_career_kicking_stats(prior_kick_stats_data)

            fg_made_17_29 = season_kicking_stats.fg_made_17_29 - prior_kick_stats.fg_made_17_29
            fg_att_17_29 = season_kicking_stats.fg_att_17_29 - prior_kick_stats.fg_att_17_29
            long_fg = season_kicking_stats.long_fg - prior_kick_stats.long_fg
            ko_touchbacks = season_kicking_stats.ko_touchbacks - prior_kick_stats.ko_touchbacks
            long_punt = season_kicking_stats.long_punt - prior_kick_stats.long_punt
            xp_att = season_kicking_stats.xp_att - prior_kick_stats.xp_att
            punts_blocked = season_kicking_stats.punts_blocked - prior_kick_stats.punts_blocked
            fg_att = season_kicking_stats.fg_att - prior_kick_stats.fg_att
            total_punt_yards = season_kicking_stats.total_punt_yards - prior_kick_stats.total_punt_yards
            xp_blocked = season_kicking_stats.xp_blocked - prior_kick_stats.xp_blocked
            fg_blocked = season_kicking_stats.fg_blocked - prior_kick_stats.fg_blocked
            fg_att_40_49 = season_kicking_stats.fg_att_40_49 - prior_kick_stats.fg_att_40_49
            fg_made_40_49 = season_kicking_stats.fg_made_40_49 - prior_kick_stats.fg_made_40_49
            fg_att_30_39 = season_kicking_stats.fg_att_30_39 - prior_kick_stats.fg_att_30_39
            fg_made_30_39 = season_kicking_stats.fg_made_30_39 - prior_kick_stats.fg_made_30_39
            fg_att_50_plus = season_kicking_stats.fg_att_50_plus - prior_kick_stats.fg_att_50_plus
            fg_made_50_plus = season_kicking_stats.fg_made_50_plus - prior_kick_stats.fg_made_50_plus
            punt_touchbacks = season_kicking_stats.punt_touchbacks - prior_kick_stats.punt_touchbacks
            kickoffs = season_kicking_stats.kickoffs - prior_kick_stats.kickoffs
            xp_made = season_kicking_stats.xp_made - prior_kick_stats.xp_made
            net_punting = season_kicking_stats.net_punting - prior_kick_stats.net_punting
            fg_made = season_kicking_stats.fg_made - prior_kick_stats.fg_made
            number_punts = season_kicking_stats.number_punts - prior_kick_stats.number_punts
            inside_twenty = season_kicking_stats.inside_twenty - prior_kick_stats.inside_twenty
            fg_pct = round(
                0 if fg_att == 0 else \
                    fg_made / fg_att, 1
            )
            xp_pct = round(
                0 if xp_att == 0 else \
                    xp_made / xp_att, 1
            )
            fg_50_plus_pct = round(
                0 if fg_att_50_plus == 0 else \
                    fg_made_50_plus / fg_att_50_plus, 1
            )
            punt_avg = round(
                0 if number_punts == 0 else \
                    total_punt_yards / number_punts, 1
            )

            game_stats = GameKickingStatsData(
                id=new_id,
                player_id=player.id,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                fg_made_17_29=fg_made_17_29,
                fg_att_17_29=fg_att_17_29,
                long_fg=long_fg,
                ko_touchbacks=ko_touchbacks,
                long_punt=long_punt,
                xp_att=xp_att,
                punts_blocked=punts_blocked,
                fg_att=fg_att,
                total_punt_yards=total_punt_yards,
                xp_blocked=xp_blocked,
                fg_blocked=fg_blocked,
                fg_att_40_49=fg_att_40_49,
                fg_made_40_49=fg_made_40_49,
                fg_att_30_39=fg_att_30_39,
                fg_made_30_39=fg_made_30_39,
                fg_att_50_plus=fg_att_50_plus,
                fg_made_50_plus=fg_made_50_plus,
                punt_touchbacks=punt_touchbacks,
                kickoffs=kickoffs,
                xp_made=xp_made,
                net_punting=net_punting,
                fg_made=fg_made,
                number_punts=number_punts,
                inside_twenty=inside_twenty,
                fg_pct=fg_pct,
                xp_pct=xp_pct,
                fg_50_plus_pct=fg_50_plus_pct,
                punt_avg=punt_avg
            )

            session.add(game_stats)
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_game_off_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()
    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    for player in players:

        off_stats_data: List[SeasonOffensiveStatsData] = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player.id,
            SeasonOffensiveStatsData.year == week_year.year
        ).scalar()

        # Skip over players that don't have kicking stats
        if not off_stats_data:
            continue

        season_pass_stats: PassingStats = _get_passing_stats(off_stats_data)
        season_rec_stats: ReceivingStats = _get_receiving_stats(off_stats_data)
        season_rush_stats: RushingStats = _get_rushing_stats(off_stats_data)
        season_total_stats: TotalStats = _get_total_stats(off_stats_data)
        
        new_id = str(uuid4())

        # Check for prior week offensive stats
        prior_off_stats_data: GameOffensiveStatsData = session.query(GameOffensiveStatsData).where(
            GameOffensiveStatsData.player_id == player.id,
            GameOffensiveStatsData.year == week_year.year
        ).all()

        if not prior_off_stats_data and off_stats_data:

            game_stats: GameOffensiveStatsData = GameOffensiveStatsData(
                id = new_id,
                player_id=player.id,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                pass_yards=season_pass_stats.pass_yards,
                longest_rec=season_rec_stats.longest_rec,
                longest_pass=season_pass_stats.longest_pass,
                longest_run=season_rush_stats.longest_run,
                receptions=season_rec_stats.receptions,
                sacked=season_pass_stats.sacked,
                rec_yards=season_rec_stats.rec_yards,
                rush_yards=season_rush_stats.rush_yards,
                yac=season_rec_stats.yac,
                pass_tds=season_pass_stats.pass_tds,
                rec_tds=season_rec_stats.rec_tds,
                rush_tds=season_rush_stats.rush_tds,
                ya_contact=season_rush_stats.ya_contact,
                completions=season_pass_stats.completions,
                ints=season_pass_stats.ints,
                drops=season_rec_stats.drops,
                pass_att=season_pass_stats.pass_att,
                rush_att=season_rush_stats.rush_att,
                broke_tkls=season_rush_stats.broke_tkls,
                fumbles=season_rush_stats.fumbles,
                twenty_plus_yd_runs=season_rush_stats.twenty_plus_yd_runs,
                total_yards=season_total_stats.total_yards,
                total_tds=season_total_stats.total_tds,
                total_ypg=season_total_stats.total_yards,
                pass_yp_attempt=season_pass_stats.pass_yp_attempt,
                pass_yp_game=season_pass_stats.pass_yards,
                rush_yp_carry=season_rush_stats.rush_yp_carry,
                rush_yp_game=season_rush_stats.rush_yards,
                rec_yp_catch=season_rec_stats.rec_yp_catch,
                rec_yp_game=season_rec_stats.rec_yards,
                pass_rating=season_pass_stats.pass_rating
            )
            session.add(game_stats)
            session.flush()

        else:

            prior_pass_stats: PassingStats = _compile_career_passing_stats(prior_off_stats_data)
            prior_rec_stats: ReceivingStats = _compile_career_receiving_stats(prior_off_stats_data)
            prior_rush_stats: RushingStats = _compile_career_rushing_stats(prior_off_stats_data)
            prior_total_stats: TotalStats = _compile_career_total_stats(prior_off_stats_data)

            pass_yards = season_pass_stats.pass_yards - prior_pass_stats.pass_yards
            longest_rec = season_rec_stats.longest_rec - prior_rec_stats.longest_rec
            longest_pass = season_pass_stats.longest_pass - prior_pass_stats.longest_pass
            longest_run = season_rush_stats.longest_run - prior_rush_stats.longest_run
            receptions = season_rec_stats.receptions - prior_rec_stats.receptions
            sacked = season_pass_stats.sacked - prior_pass_stats.sacked
            rec_yards = season_rec_stats.rec_yards - prior_rec_stats.rec_yards
            rush_yards = season_rush_stats.rush_yards - prior_rush_stats.rush_yards
            yac = season_rec_stats.yac - prior_rec_stats.yac
            pass_tds = season_pass_stats.pass_tds - prior_pass_stats.pass_tds
            rec_tds = season_rec_stats.rec_tds - prior_rec_stats.rec_tds
            rush_tds = season_rush_stats.rush_tds - prior_rush_stats.rush_tds
            ya_contact = season_rush_stats.ya_contact - prior_rush_stats.ya_contact
            completions = season_pass_stats.completions - prior_pass_stats.completions
            ints = season_pass_stats.ints - prior_pass_stats.ints
            drops = season_rec_stats.drops - prior_rec_stats.drops
            pass_att = season_pass_stats.pass_att - prior_pass_stats.pass_att
            rush_att = season_rush_stats.rush_att - prior_rush_stats.rush_att
            broke_tkls = season_rush_stats.broke_tkls - prior_rush_stats.broke_tkls
            fumbles = season_rush_stats.fumbles - prior_rush_stats.fumbles
            twenty_plus_yd_runs = season_rush_stats.twenty_plus_yd_runs - prior_rush_stats.twenty_plus_yd_runs

            pass_yp_attempt = season_pass_stats.pass_yp_attempt - prior_pass_stats.pass_yp_attempt

            rush_yp_carry = round(0 if rush_att == 0 else\
                rush_yards / rush_att,
                1
            )
            rec_yp_catch = round(0 if receptions == 0 else\
                rec_yards / receptions,
                1
            )
            pass_rating_calc = (
                0 if pass_att == 0 else \
                ((8.4 * pass_yards) + (330 * pass_tds) + \
                (100 * completions) - (200 * ints)) / pass_att
                )
            pass_rating = round(pass_rating_calc, 1)
            total_yards = season_total_stats.total_yards - prior_total_stats.total_yards
            total_tds = season_total_stats.total_tds - prior_total_stats.total_tds

            game_stats = GameOffensiveStatsData(
                id=new_id,
                player_id=player.id,
                pass_yards=pass_yards,
                longest_rec=longest_rec,
                longest_pass=longest_pass,
                longest_run=longest_run,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                receptions=receptions,
                sacked=sacked,
                rec_yards=rec_yards,
                rush_yards=rush_yards,
                yac=yac,
                pass_tds=pass_tds,
                rec_tds=rec_tds,
                rush_tds=rush_tds,
                ya_contact=ya_contact,
                completions=completions,
                ints=ints,
                drops=drops,
                pass_att=pass_att,
                rush_att=rush_att,
                broke_tkls=broke_tkls,
                fumbles=fumbles,
                twenty_plus_yd_runs=twenty_plus_yd_runs,
                pass_yp_attempt=pass_yp_attempt,
                pass_yp_game=pass_yards,
                rush_yp_carry=rush_yp_carry,
                rush_yp_game=rush_yards,
                rec_yp_catch=rec_yp_catch,
                rec_yp_game=rec_yards,
                pass_rating=pass_rating,
                total_yards=total_yards,
                total_tds=total_tds,
                total_ypg=total_yards
            )

            session.add(game_stats)
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_game_return_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()
    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()

    for player in players:

        return_stats_data: List[SeasonReturnStatsData] = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player.id,
            SeasonReturnStatsData.year == week_year.year
        ).scalar()

        # Skip over players that don't have kicking stats
        if not return_stats_data:
            continue

        season_return_stats: ReturnStats = _get_return_stats(return_stats_data)
        
        new_id = str(uuid4())

        # Check for prior week offensive stats
        prior_return_stats_data: GameReturnStatsData = session.query(GameReturnStatsData).where(
            GameReturnStatsData.player_id == player.id,
            GameReturnStatsData.year == week_year.year
            
        ).all()

        if not prior_return_stats_data and return_stats_data:

            game_stats: GameReturnStatsData = GameReturnStatsData(
                id=new_id,
                player_id=player.id,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                kick_returns=season_return_stats.kick_returns,
                long_kr=season_return_stats.long_kr,
                punt_returns=season_return_stats.punt_returns,
                long_pr=season_return_stats.long_pr,
                kr_tds=season_return_stats.kr_tds,
                pr_tds=season_return_stats.pr_tds,
                kr_yds=season_return_stats.kr_yds,
                pr_yds=season_return_stats.pr_yds,
                kr_avg=season_return_stats.kr_avg,
                pr_avg=season_return_stats.pr_avg
            )
            session.add(game_stats)
            session.flush()

        else:

            prior_kick_stats: ReturnStats = _compile_career_return_stats(prior_return_stats_data)

            kick_returns = season_return_stats.kick_returns - prior_kick_stats.kick_returns
            long_kr = season_return_stats.long_kr - prior_kick_stats.long_kr
            punt_returns = season_return_stats.punt_returns - prior_kick_stats.punt_returns
            long_pr = season_return_stats.long_pr - prior_kick_stats.long_pr
            kr_tds = season_return_stats.kr_tds - prior_kick_stats.kr_tds
            pr_tds = season_return_stats.pr_tds - prior_kick_stats.pr_tds
            kr_yds = season_return_stats.kr_yds - prior_kick_stats.kr_yds
            pr_yds = season_return_stats.pr_yds - prior_kick_stats.pr_yds
            kr_avg = season_return_stats.kr_avg - prior_kick_stats.kr_avg
            pr_avg = season_return_stats.pr_avg - prior_kick_stats.pr_avg

            game_stats = GameReturnStatsData(
                id=new_id,
                player_id=player.id,
                week=week_year.week,
                year=week_year.year,
                games_played=1,
                kick_returns=kick_returns,
                long_kr=long_kr,
                punt_returns=punt_returns,
                long_pr=long_pr,
                kr_tds=kr_tds,
                pr_tds=pr_tds,
                kr_yds=kr_yds,
                pr_yds=pr_yds,
                kr_avg=kr_avg,
                pr_avg=pr_avg
            )

            session.add(game_stats)
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
