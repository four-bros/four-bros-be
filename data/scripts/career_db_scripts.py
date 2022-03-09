from typing import List
from sqlalchemy.sql.expression import update
from uuid import uuid4

from src.constants import session
from src.data_models.CareerDefensiveStatsData import CareerDefensiveStatsData
from src.data_models.CareerKickingStatsData import CareerKickingStatsData
from src.data_models.CareerOffensiveStatsData import CareerOffensiveStatsData
from src.data_models.CareerReturnStatsData import CareerReturnStatsData
from src.models.Stats import (
    DefensiveStats,
    KickingAndPuntingStats,
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
    _compile_career_total_stats
)
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData


def insert_career_def_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        defensive_stats_data: List[SeasonDefensiveStatsData] = session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have defensive stats
        if not defensive_stats_data:
            continue

        career_defensive_stats: DefensiveStats = _compile_career_defensive_stats(defensive_stats_data)
        
        new_id = str(uuid4())
        
        player_career_def_stats = CareerDefensiveStatsData(
            id=new_id,
            player_id=player.id,
            long_int_ret=career_defensive_stats.long_int_ret,
            sacks=career_defensive_stats.sacks,
            year=None,
            forced_fumbles=career_defensive_stats.forced_fumbles,
            solo_tkls=career_defensive_stats.solo_tkls,
            safeties=career_defensive_stats.safeties,
            pass_def=career_defensive_stats.pass_def,
            blocked_kicks=career_defensive_stats.blocked_kicks,
            tfl=career_defensive_stats.tfl,
            ints_made=career_defensive_stats.ints_made,
            games_played=career_defensive_stats.games_played,
            fumbles_rec=career_defensive_stats.fumbles_rec,
            half_a_sack=career_defensive_stats.half_a_sack,
            asst_tkls=career_defensive_stats.asst_tkls,
            def_tds=career_defensive_stats.def_tds,
            fum_rec_yards=career_defensive_stats.fum_rec_yards,
            int_ret_yards=career_defensive_stats.int_ret_yards,
            total_tkls=career_defensive_stats.total_tkls,
            total_sacks=career_defensive_stats.total_sacks
        )


        # Query table to determine if player has a record or not
        player_query: CareerDefensiveStatsData = session.query(CareerDefensiveStatsData).where(
            CareerDefensiveStatsData.player_id == player_career_def_stats.player_id).scalar()

        if not player_query:
            session.add(player_career_def_stats)
            session.flush()
        else:
            update(CareerDefensiveStatsData).where(CareerDefensiveStatsData.player_id == player_career_def_stats.player_id).values(
                player_id=player_career_def_stats.player_id,
                long_int_ret=player_career_def_stats.long_int_ret,
                sacks=player_career_def_stats.sacks,
                year=player_career_def_stats.year,
                forced_fumbles=player_career_def_stats.forced_fumbles,
                solo_tkls=player_career_def_stats.solo_tkls,
                safeties=player_career_def_stats.safeties,
                pass_def=player_career_def_stats.pass_def,
                blocked_kicks=player_career_def_stats.blocked_kicks,
                tfl=player_career_def_stats.tfl,
                ints_made=player_career_def_stats.ints_made,
                games_played=player_career_def_stats.games_played,
                fumbles_rec=player_career_def_stats.fumbles_rec,
                half_a_sack=player_career_def_stats.half_a_sack,
                asst_tkls=player_career_def_stats.asst_tkls,
                def_tds=player_career_def_stats.def_tds,
                fum_rec_yards=player_career_def_stats.fum_rec_yards,
                int_ret_yards=player_career_def_stats.int_ret_yards,
                total_tkls=player_career_def_stats.total_tkls
            )
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_career_kicking_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        kicking_stats_data: List[SeasonKickingStatsData] = session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have kicking stats
        if not kicking_stats_data:
            continue

        career_kicking_stats: KickingAndPuntingStats = _compile_career_kicking_stats(kicking_stats_data)
        
        new_id = str(uuid4())

        player_career_kick_stats = CareerKickingStatsData(
            id=new_id,
            player_id=player.id,
            fg_made_17_29=career_kicking_stats.fg_made_17_29,
            fg_att_17_29=career_kicking_stats.fg_att_17_29,
            long_fg=career_kicking_stats.long_fg,
            ko_touchbacks=career_kicking_stats.ko_touchbacks,
            long_punt=career_kicking_stats.long_punt,
            xp_att=career_kicking_stats.xp_att,
            year=None,
            punts_blocked=career_kicking_stats.punts_blocked,
            fg_att=career_kicking_stats.fg_att,
            total_punt_yards=career_kicking_stats.total_punt_yards,
            xp_blocked=career_kicking_stats.xp_blocked,
            fg_blocked=career_kicking_stats.fg_blocked,
            fg_att_40_49=career_kicking_stats.fg_att_40_49,
            fg_made_40_49=career_kicking_stats.fg_made_40_49,
            fg_att_30_39=career_kicking_stats.fg_att_30_39,
            fg_made_30_39=career_kicking_stats.fg_made_30_39,
            fg_att_50_plus=career_kicking_stats.fg_att_50_plus,
            fg_made_50_plus=career_kicking_stats.fg_made_50_plus,
            punt_touchbacks=career_kicking_stats.punt_touchbacks,
            games_played=career_kicking_stats.games_played,
            kickoffs=career_kicking_stats.kickoffs,
            xp_made=career_kicking_stats.xp_made,
            net_punting=career_kicking_stats.net_punting,
            fg_made=career_kicking_stats.fg_made,
            number_punts=career_kicking_stats.number_punts,
            inside_twenty=career_kicking_stats.inside_twenty,
            fg_pct=career_kicking_stats.fg_pct,
            xp_pct=career_kicking_stats.xp_pct,
            fg_50_plus_pct=career_kicking_stats.fg_50_plus_pct,
            punt_avg=career_kicking_stats.punt_avg,
            net_avg=career_kicking_stats.net_avg
        )

        player_query: CareerKickingStatsData = session.query(CareerKickingStatsData).where(
            CareerKickingStatsData.player_id == player_career_kick_stats.player_id
        ).scalar()
        
        if not player_query:
            session.add(player_career_kick_stats)
            session.flush()
        else:
            update(CareerKickingStatsData).where(
                CareerKickingStatsData.player_id == player_career_kick_stats.player_id
            ).values(
                player_id=player_career_kick_stats.player_id,
                fg_made_17_29=player_career_kick_stats.fg_made_17_29,
                fg_att_17_29=player_career_kick_stats.fg_att_17_29,
                long_fg=player_career_kick_stats.long_fg,
                ko_touchdowns=player_career_kick_stats.ko_touchbacks,
                long_punt=player_career_kick_stats.long_punt,
                xp_att=player_career_kick_stats.xp_att,
                year=player_career_kick_stats.year,
                punts_blocked=player_career_kick_stats.punts_blocked,
                fg_att=player_career_kick_stats.fg_att,
                total_punt_yards=player_career_kick_stats.total_punt_yards,
                xp_blocked=player_career_kick_stats.xp_blocked,
                fg_blocked=player_career_kick_stats.fg_blocked,
                fg_att_40_49=player_career_kick_stats.fg_att_40_49,
                fg_made_40_49=player_career_kick_stats.fg_made_40_49,
                fg_att_30_39=player_career_kick_stats.fg_att_30_39,
                fg_made_30_39=player_career_kick_stats.fg_made_30_39,
                fg_att_50_plus=player_career_kick_stats.fg_att_50_plus,
                fg_made_50_plus=player_career_kick_stats.fg_made_50_plus,
                punt_touchbacks=player_career_kick_stats.punt_touchbacks,
                games_played=player_career_kick_stats.games_played,
                kickoffs=player_career_kick_stats.kickoffs,
                xp_made=player_career_kick_stats.xp_made,
                net_punting=player_career_kick_stats.net_punting,
                fg_made=player_career_kick_stats.fg_made,
                number_punts=player_career_kick_stats.number_punts,
                inside_twenty=player_career_kick_stats.inside_twenty,
                net_avg=player_career_kick_stats.net_avg
            )
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_career_off_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        off_stats_data: List[SeasonOffensiveStatsData] = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have kicking stats
        if not off_stats_data:
            continue

        career_pass_stats: PassingStats = _compile_career_passing_stats(off_stats_data)
        career_rec_stats: ReceivingStats = _compile_career_receiving_stats(off_stats_data)
        career_rush_stats: RushingStats = _compile_career_rushing_stats(off_stats_data)
        career_total_stats: TotalStats = _compile_career_total_stats(off_stats_data)
        
        new_id = str(uuid4())

        games_played = sum([stats.games_played for stats in off_stats_data])

        player_career_off_stats = CareerOffensiveStatsData(
            id=new_id,
            player_id=player.id,
            pass_yards=career_pass_stats.pass_yards,
            longest_rec=career_rec_stats.longest_rec,
            longest_pass=career_pass_stats.longest_pass,
            longest_run=career_rush_stats.longest_run,
            year=None,
            receptions=career_rec_stats.receptions,
            sacked=career_pass_stats.sacked,
            rec_yards=career_rec_stats.rec_yards,
            rush_yards=career_rush_stats.rush_yards,
            yac=career_rec_stats.yac,
            pass_tds=career_pass_stats.pass_tds,
            games_played=games_played,
            rec_tds=career_rec_stats.rec_tds,
            rush_tds=career_rush_stats.rush_tds,
            ya_contact=career_rush_stats.ya_contact,
            completions=career_pass_stats.completions,
            ints=career_pass_stats.ints,
            drops=career_rec_stats.drops,
            pass_att=career_pass_stats.pass_att,
            rush_att=career_rush_stats.rush_att,
            broke_tkls=career_rush_stats.broke_tkls,
            fumbles=career_rush_stats.fumbles,
            twenty_plus_yd_runs=career_rush_stats.twenty_plus_yd_runs,
            pass_yp_attempt=career_pass_stats.pass_yp_attempt,
            pass_yp_game=career_pass_stats.pass_yp_game,
            rush_yp_carry=career_rush_stats.rush_yp_carry,
            rush_yp_game=career_rush_stats.rush_yp_game,
            rec_yp_catch=career_rec_stats.rec_yp_catch,
            rec_yp_game=career_rec_stats.rec_yp_game,
            pass_rating=career_pass_stats.pass_rating,
            total_yards=career_total_stats.total_yards,
            total_tds=career_total_stats.total_tds,
            total_ypg=career_total_stats.total_ypg,
            turnovers=career_total_stats.turnovers
        )
        

        player_query: CareerOffensiveStatsData = session.query(CareerOffensiveStatsData).where(
            CareerOffensiveStatsData.player_id == player_career_off_stats.player_id).scalar()

        if not player_query:
            session.add(player_career_off_stats)
            session.flush()
        else:
            update(CareerOffensiveStatsData).where(CareerOffensiveStatsData.player_id == player_career_off_stats.player_id).values(
                player_id=player_career_off_stats.player_id,
                pass_yards=player_career_off_stats.pass_yards,
                longest_rec=player_career_off_stats.longest_rec,
                longest_pass=player_career_off_stats.longest_pass,
                longest_run=player_career_off_stats.longest_run,
                year=player_career_off_stats.year,
                receptions=player_career_off_stats.receptions,
                sacked=player_career_off_stats.sacked,
                rec_yards=player_career_off_stats.rec_yards,
                rush_yards=player_career_off_stats.rush_yards,
                yac=player_career_off_stats.yac,
                pass_tds=player_career_off_stats.pass_tds,
                games_played=player_career_off_stats.games_played,
                rec_tds=player_career_off_stats.rec_tds,
                rush_tds=player_career_off_stats.rush_tds,
                ya_contact=player_career_off_stats.ya_contact,
                completions=player_career_off_stats.completions,
                ints=player_career_off_stats.ints,
                drops=player_career_off_stats.drops,
                pass_att=player_career_off_stats.pass_att,
                rush_att=player_career_off_stats.rush_att,
                broke_tkls=player_career_off_stats.broke_tkls,
                fumbles=player_career_off_stats.fumbles,
                twenty_plus_yd_runs=player_career_off_stats.twenty_plus_yd_runs,
                pass_yp_attempt=player_career_off_stats.pass_yp_attempt,
                pass_yp_game=player_career_off_stats.pass_yp_game,
                rush_yp_carry=player_career_off_stats.rush_yp_carry,
                rush_yp_game=player_career_off_stats.rush_yp_game,
                rec_yp_catch=player_career_off_stats.rec_yp_catch,
                rec_yp_game=player_career_off_stats.rec_yp_game,
                total_yards=player_career_off_stats.total_yards,
                total_tds=player_career_off_stats.total_tds,
                total_ypg=player_career_off_stats.total_ypg,
                turnovers=player_career_off_stats.turnovers
            )
            session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_career_return_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        return_stats_data: List[SeasonReturnStatsData] = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have kicking stats
        if not return_stats_data:
            continue
            
        career_return_stats: ReturnStats = _compile_career_return_stats(return_stats_data)

        new_id = str(uuid4())

        player_career_return_stats = CareerReturnStatsData(
            id=new_id,
            player_id=player.id,
            kick_returns=career_return_stats.kick_returns,
            year=None,
            long_kr=career_return_stats.long_kr,
            punt_returns=career_return_stats.punt_returns,
            long_pr=career_return_stats.long_pr,
            games_played=career_return_stats.games_played,
            kr_tds=career_return_stats.kr_tds,
            pr_tds=career_return_stats.pr_tds,
            kr_yds=career_return_stats.kr_yds,
            pr_yds=career_return_stats.pr_yds,
            kr_avg=career_return_stats.kr_avg,
            pr_avg=career_return_stats.pr_avg
        )
        

        player_query: CareerReturnStatsData = session.query(CareerReturnStatsData).where(
            CareerReturnStatsData.player_id == player_career_return_stats.player_id).scalar()
        
        if not player_query:
            session.add(player_career_return_stats)
            session.flush()
            
        else:
            update(CareerReturnStatsData).where(CareerReturnStatsData.player_id == player_career_return_stats.player_id).values(
                player_id=player_career_return_stats.player_id,
                kick_returns=player_career_return_stats.kick_returns,
                year=player_career_return_stats.year,
                long_kr=player_career_return_stats.long_kr,
                punt_returns=player_career_return_stats.punt_returns,
                long_pr=player_career_return_stats.long_pr,
                games_played=player_career_return_stats.games_played,
                kr_tds=player_career_return_stats.kr_tds,
                pr_tds=player_career_return_stats.pr_tds,
                kr_yds=player_career_return_stats.kr_yds,
                pr_yds=player_career_return_stats.pr_yds,
                kr_avg=player_career_return_stats.kr_avg,
                pr_avg=player_career_return_stats.pr_avg
            )
            session.flush()

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
