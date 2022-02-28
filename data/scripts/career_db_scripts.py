from typing import List
import ncaa_dynasty
from sqlalchemy.sql.expression import update
from uuid import uuid4

from src.constants import session
from src.data_models.CareerDefensiveStatsData import CareerDefensiveStatsData
from src.data_models.CareerKickingStatsData import CareerKickingStatsData
from src.data_models.CareerOffensiveStatsData import CareerOffensiveStatsData
from src.data_models.CareerReturnStatsData import CareerReturnStatsData
from src.models.Stats import (
    DefensiveStats,
    KickingStats,
    PassingStats,
    ReceivingStats,
    ReturnStats,
    RushingStats,
    TotalStats
)
from src.utils.helpers import(
    _convert_stats_year
)
from src.utils.player_stats import (
    _get_career_defensive_stats,
    _get_career_kicking_stats,
    _get_career_passing_stats,
    _get_career_receiving_stats,
    _get_career_return_stats,
    _get_career_rushing_stats,
    _get_career_total_stats
)
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.WeekYearData import WeekYearData


def insert_career_def_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        defensive_stats_data: List[SeasonDefensiveStatsData] = session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have defensive stats
        if not defensive_stats_data:
            continue

        career_defensive_stats: DefensiveStats = _get_career_defensive_stats(defensive_stats_data)
        
        new_id = str(uuid4())
        
        new_player = CareerDefensiveStatsData(
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
        player: CareerDefensiveStatsData = session.query(CareerDefensiveStatsData).where(
            CareerDefensiveStatsData.player_id == new_player.id).scalar()

        if not player:
            session.add(new_player)
            session.flush()
        else:
            update(CareerDefensiveStatsData).where(CareerDefensiveStatsData.player_id == new_player.id).values(
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


def insert_career_kicking_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        kicking_stats_data: List[SeasonKickingStatsData] = session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have kicking stats
        if not kicking_stats_data:
            continue

        career_kicking_stats: KickingStats = _get_career_kicking_stats(kicking_stats_data)
        
        new_id = str(uuid4())

        new_player = CareerKickingStatsData(
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
            punt_avg=career_kicking_stats.punt_avg
        )

        player: CareerKickingStatsData = session.query(CareerKickingStatsData).where(
            CareerKickingStatsData.player_id == new_player.player_id
        ).scalar()
        
        if not player:
            session.add(new_player)
            session.flush()
        else:
            update(CareerKickingStatsData).where(CareerKickingStatsData.player_id == new_player.player_id).values(
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


def insert_career_off_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        off_stats_data: List[SeasonOffensiveStatsData] = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have kicking stats
        if not off_stats_data:
            continue

        career_pass_stats: PassingStats = _get_career_passing_stats(off_stats_data)
        career_rec_stats: ReceivingStats = _get_career_receiving_stats(off_stats_data)
        career_rush_stats: RushingStats = _get_career_rushing_stats(off_stats_data)
        career_total_stats: TotalStats = _get_career_total_stats(off_stats_data)
        
        new_id = str(uuid4())

        new_player = CareerOffensiveStatsData(
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
            games_played=career_pass_stats.games_played,
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
            total_ypg=career_total_stats.total_ypg
        )
        

        player: CareerOffensiveStatsData = session.query(CareerOffensiveStatsData).where(
            CareerOffensiveStatsData.player_id == new_player.player_id).scalar()

        if not player:
            session.add(new_player)
            session.flush()
        else:
            update(CareerOffensiveStatsData).where(CareerOffensiveStatsData.player_id == new_player.player_id).values(
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


def insert_career_return_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    for player in players:

        return_stats_data: List[SeasonReturnStatsData] = session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player.id
        ).all()

        # Skip over players that don't have kicking stats
        if not return_stats_data:
            continue
            
        career_return_stats: ReturnStats = _get_career_return_stats(return_stats_data)

        new_id = str(uuid4())

        new_player = CareerReturnStatsData(
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
        

        player: CareerReturnStatsData = session.query(CareerReturnStatsData).where(
            CareerReturnStatsData.player_id == new_player.player_id).scalar()
        
        if not player:
            session.add(new_player)
            session.flush()
            
        else:
            update(CareerReturnStatsData).where(CareerReturnStatsData.player_id == new_player.player_id).values(
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
