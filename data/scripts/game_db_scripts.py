from typing import List
from uuid import uuid4

from src.constants import session
from src.data_models.GameOffensiveStatsData import GameOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.WeekYearData import WeekYearData
from src.models.Stats import (
    PassingStats,
    ReceivingStats,
    RushingStats,
    TotalStats
)
from src.utils.player_stats import (
    _get_career_passing_stats,
    _get_career_receiving_stats,
    _get_career_rushing_stats,
    _get_career_total_stats,
    _get_season_passing_stats,
    _get_season_receiving_stats,
    _get_season_rushing_stats,
    _get_season_total_stats
)


def insert_game_off_stats_into_db():

    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()
    week_year: WeekYearData = session.query(WeekYearData).first()

    for player in players:

        off_stats_data: List[SeasonOffensiveStatsData] = session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player.id,
            SeasonOffensiveStatsData.year == week_year.year
        ).scalar()

        # Skip over players that don't have kicking stats
        if not off_stats_data:
            continue

        season_pass_stats: PassingStats = _get_season_passing_stats(off_stats_data)
        season_rec_stats: ReceivingStats = _get_season_receiving_stats(off_stats_data)
        season_rush_stats: RushingStats = _get_season_rushing_stats(off_stats_data)
        season_total_stats: TotalStats = _get_season_total_stats(off_stats_data)
        
        new_id = str(uuid4())

        # Check for prior week offensive stats
        prior_off_stats_data: GameOffensiveStatsData = session.query(GameOffensiveStatsData).where(
            GameOffensiveStatsData.player_id == player.id
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

            prior_pass_stats: PassingStats = _get_career_passing_stats(prior_off_stats_data)
            prior_rec_stats: ReceivingStats = _get_career_receiving_stats(prior_off_stats_data)
            prior_rush_stats: RushingStats = _get_career_rushing_stats(prior_off_stats_data)
            prior_total_stats: TotalStats = _get_career_total_stats(prior_off_stats_data)

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
