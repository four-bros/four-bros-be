from typing import List

from src.constants import Positions
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.TeamGameStatsData import TeamGameStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamSeasonStatsData import TeamSeasonStatsData
from src.models.Teams import (
    TeamDetails,
    TeamInfo,
    TeamRoster,
    TeamSeasonStats,
    TeamGameStats
)


################################################
########## Get team info and stats #############
################################################
def _get_team_game_stats(team_game_stats: TeamGameStatsData) -> TeamGameStats:

        team_game_stats: TeamGameStats = TeamGameStats(
            team_id=team_game_stats.team_id,
            week=team_game_stats.week,
            year=team_game_stats.year,
            total_points=team_game_stats.total_points,
            completions=team_game_stats.completions,
            pass_att=team_game_stats.pass_att,
            comp_pct=team_game_stats.comp_pct,
            pass_yds=team_game_stats.pass_yds,
            pass_ypa=team_game_stats.pass_ypa,
            pass_tds=team_game_stats.pass_tds,
            ints=team_game_stats.ints,
            sacked=team_game_stats.sacked,
            rush_att=team_game_stats.rush_att,
            rush_yds=team_game_stats.rush_yds,
            rush_ypc=team_game_stats.rush_ypc,
            rush_tds=team_game_stats.rush_tds,
            fumbles=team_game_stats.fumbles,
            receptions=team_game_stats.receptions,
            rec_yds=team_game_stats.rec_yds,
            rec_ypc=team_game_stats.rec_ypc,
            rec_tds=team_game_stats.rec_tds,
            drops=team_game_stats.drops,
            off_yards=team_game_stats.off_yards,
            total_yards=team_game_stats.total_yards,
            off_turnovers=team_game_stats.off_turnovers,
            sacks=team_game_stats.sacks,
            tfl=team_game_stats.tfl,
            ints_made=team_game_stats.ints_made,
            ff=team_game_stats.ff,
            fr=team_game_stats.fr,
            def_turnovers=team_game_stats.def_turnovers,
            to_margin=team_game_stats.to_margin,
            pass_def=team_game_stats.pass_def,
            blocked_kicks=team_game_stats.blocked_kicks,
            safeties=team_game_stats.safeties,
            def_tds=team_game_stats.def_tds,
            kr_yds=team_game_stats.kr_yds,
            kr_tds=team_game_stats.kr_tds,
            pr_yds=team_game_stats.pr_yds,
            pr_tds=team_game_stats.pr_tds,
        )

        return team_game_stats



def _compile_prior_team_game_stats(team_game_stats_data: List[TeamGameStatsData]):

    prior_team_game_stats: List[TeamGameStats] = [_get_team_game_stats(game) for game in team_game_stats_data]

    team_id = prior_team_game_stats[0].team_id
    total_points = sum([game.total_points for game in prior_team_game_stats])
    completions = sum([game.completions for game in prior_team_game_stats])
    pass_att = sum([game.pass_att for game in prior_team_game_stats])
    pass_yds = sum([game.pass_yds for game in prior_team_game_stats])
    comp_pct = round(
        completions / pass_att *100 if pass_att > 0 else 0,
        1
    )
    pass_ypa = round(
        pass_yds / pass_att if pass_att != 0 else 0,
        1
    )
    pass_tds = sum([game.pass_tds for game in prior_team_game_stats])
    ints = sum([game.ints for game in prior_team_game_stats])
    sacked = sum([game.sacked for game in prior_team_game_stats])
    rush_att = sum([game.rush_att for game in prior_team_game_stats])
    rush_yds = sum([game.rush_yds for game in prior_team_game_stats])
    rush_ypc = sum([game.rush_ypc for game in prior_team_game_stats])
    rush_tds = sum([game.rush_tds for game in prior_team_game_stats])
    fumbles = sum([game.fumbles for game in prior_team_game_stats])
    receptions = sum([game.receptions for game in prior_team_game_stats])
    rec_yds = sum([game.rec_yds for game in prior_team_game_stats])
    rec_ypc = sum([game.rec_ypc for game in prior_team_game_stats])
    rec_tds = sum([game.rec_tds for game in prior_team_game_stats])
    drops = sum([game.drops for game in prior_team_game_stats])
    off_yards = sum([game.off_yards for game in prior_team_game_stats])
    total_yards = sum([game.total_yards for game in prior_team_game_stats])
    off_turnovers = sum([game.off_turnovers for game in prior_team_game_stats])
    sacks = sum([game.sacks for game in prior_team_game_stats])
    tfl = sum([game.tfl for game in prior_team_game_stats])
    ints_made = sum([game.ints_made for game in prior_team_game_stats])
    ff = sum([game.ff for game in prior_team_game_stats])
    fr = sum([game.fr for game in prior_team_game_stats])
    def_turnovers = sum([game.def_turnovers for game in prior_team_game_stats])
    to_margin = sum([game.to_margin for game in prior_team_game_stats])
    pass_def = sum([game.pass_def for game in prior_team_game_stats])
    blocked_kicks = sum([game.blocked_kicks for game in prior_team_game_stats])
    safeties = sum([game.safeties for game in prior_team_game_stats])
    def_tds = sum([game.def_tds for game in prior_team_game_stats])
    kr_tds = sum([game.kr_tds for game in prior_team_game_stats])
    kr_yds = sum([game.kr_yds for game in prior_team_game_stats])
    pr_tds = sum([game.pr_tds for game in prior_team_game_stats])
    pr_yds = sum([game.pr_yds for game in prior_team_game_stats])

    team_game_stats: TeamGameStats = TeamGameStats(
        team_id=team_id,
        week=None,
        year=None,
        total_points=total_points,
        completions=completions,
        pass_att=pass_att,
        comp_pct=comp_pct,
        pass_yds=pass_yds,
        pass_ypa=pass_ypa,
        pass_tds=pass_tds,
        ints=ints,
        sacked=sacked,
        rush_att=rush_att,
        rush_yds=rush_yds,
        rush_ypc=rush_ypc,
        rush_tds=rush_tds,
        fumbles=fumbles,
        receptions=receptions,
        rec_yds=rec_yds,
        rec_ypc=rec_ypc,
        rec_tds=rec_tds,
        drops=drops,
        off_yards=off_yards,
        total_yards=total_yards,
        off_turnovers=off_turnovers,
        sacks=sacks,
        tfl=tfl,
        ints_made=ints_made,
        ff=ff,
        fr=fr,
        def_turnovers=def_turnovers,
        to_margin=to_margin,
        pass_def=pass_def,
        blocked_kicks=blocked_kicks,
        safeties=safeties,
        def_tds=def_tds,
        kr_yds=kr_yds,
        kr_tds=kr_tds,
        pr_yds=pr_yds,
        pr_tds=pr_tds,
    )

    return team_game_stats


def _get_team_details(team_info: TeamInfoData, players: List[PlayerInfoData]) -> TeamDetails:

    offense_players: List[PlayerInfoData] = [player for player in players if player.position in Positions.offense_positions]
    defense_players: List[PlayerInfoData] = [player for player in players if player.position in Positions.defense_positions]
    sp_team_players: List[PlayerInfoData] = [player for player in players if player.position in Positions.sp_teams_positions]

    avg_overall = round(sum([player.overall for player in players]) / len(players), 1)
    avg_offense = round(sum(player.overall for player in offense_players) / len(offense_players), 1)
    avg_defense = round(sum(player.overall for player in defense_players) / len(defense_players), 1)
    avg_sp_teams = round(sum(player.overall for player in sp_team_players) / len(sp_team_players), 1)

    team_details: TeamDetails = TeamDetails(
        id=team_info.id,
        team_name=team_info.team_name,
        team_short_name=team_info.team_short_name,
        is_user=team_info.is_user,
        avg_overall=avg_overall,
        avg_offense=avg_offense,
        avg_defense=avg_defense,
        avg_sp_teams=avg_sp_teams,
        coachs_poll_1st_votes=team_info.coachs_poll_1st_votes,
        nickname=team_info.nickname,
        wins=team_info.wins,
        bcs_rank=team_info.bcs_rank,
        coachs_poll_rank=team_info.coachs_poll_rank,
        media_poll_rank=team_info.media_poll_rank,
        losses=team_info.losses,
        media_poll_points=team_info.media_poll_points,
        coachs_poll_points=team_info.coachs_poll_points
    )

    return team_details


def _get_team_info(team: TeamInfoData) -> TeamInfo:

    team_info: TeamInfo = TeamInfo(
        id=team.id,
        team_name=team.team_name,
        nickname=team.nickname,
        is_user=team.is_user,
    )

    return team_info


def _get_team_roster(player: PlayerInfoData) -> TeamRoster:

    player_details: TeamRoster = TeamRoster(
        id=player.id,
        first_name=player.first_name,
        last_name=player.last_name,
        height=player.height,
        weight=player.weight,
        jersey_number=player.jersey_number,
        player_year=player.player_year,
        redshirt=player.redshirt,
        position=player.position,
        hometown_desc=player.hometown_desc,
        overall=player.overall
    )

    return player_details


def _get_team_game_stats(team_stats_data: TeamGameStatsData):

    team_stats: TeamGameStats = TeamGameStats(
        team_id=team_stats_data.team_id,
        week=team_stats_data.week,
        year=team_stats_data.year,
        total_points=team_stats_data.total_points,
        completions=team_stats_data.completions,
        pass_att=team_stats_data.pass_att,
        comp_pct=team_stats_data.comp_pct,
        pass_yds=team_stats_data.pass_yds,
        pass_ypa=team_stats_data.pass_ypa,
        pass_tds=team_stats_data.pass_tds,
        ints=team_stats_data.ints,
        sacked=team_stats_data.sacked,
        rush_att=team_stats_data.rush_att,
        rush_ypc=team_stats_data.rush_ypc,
        rush_yds=team_stats_data.rush_yds,
        rush_tds=team_stats_data.rush_tds,
        fumbles=team_stats_data.fumbles,
        receptions=team_stats_data.receptions,
        rec_yds=team_stats_data.rec_yds,
        rec_ypc=team_stats_data.rec_ypc,
        rec_tds=team_stats_data.rec_tds,
        drops=team_stats_data.drops,
        off_yards=team_stats_data.off_yards,
        total_yards=team_stats_data.total_yards,
        off_turnovers=team_stats_data.off_turnovers,
        sacks=team_stats_data.sacks,
        tfl=team_stats_data.tfl,
        ints_made=team_stats_data.ints_made,
        ff=team_stats_data.ff,
        fr=team_stats_data.fr,
        def_turnovers=team_stats_data.def_turnovers,
        pass_def=team_stats_data.pass_def,
        safeties=team_stats_data.safeties,
        blocked_kicks=team_stats_data.blocked_kicks,
        def_tds=team_stats_data.def_tds,
        to_margin=team_stats_data.to_margin,
        kr_yds=team_stats_data.kr_yds,
        kr_tds=team_stats_data.kr_tds,
        pr_yds=team_stats_data.pr_yds,
        pr_tds=team_stats_data.pr_tds
    )

    return team_stats


def _get_team_season_stats(team_stats_data: TeamSeasonStatsData):

    team_stats: TeamSeasonStats = TeamSeasonStats(
        team_id=team_stats_data.team_id,
        year=team_stats_data.year,
        games_played=team_stats_data.games_played,
        total_points=team_stats_data.total_points,
        ppg=team_stats_data.ppg,
        pass_yds=team_stats_data.pass_yds,
        pass_ypg=team_stats_data.pass_ypg,
        pass_tds=team_stats_data.pass_tds,
        ints=team_stats_data.ints,
        sacked=team_stats_data.sacked,
        rush_yds=team_stats_data.rush_yds,
        rush_ypg=team_stats_data.rush_ypg,
        rush_tds=team_stats_data.rush_tds,
        fumbles=team_stats_data.fumbles,
        rec_yds=team_stats_data.rec_yds,
        rec_ypg=team_stats_data.rec_ypg,
        rec_tds=team_stats_data.rec_tds,
        drops=team_stats_data.drops,
        off_yards=team_stats_data.off_yards,
        off_ypg=team_stats_data.off_ypg,
        total_yards=team_stats_data.total_yards,
        total_ypg=team_stats_data.total_ypg,
        off_turnovers=team_stats_data.off_turnovers,
        sacks=team_stats_data.sacks,
        tfl=team_stats_data.tfl,
        ints_made=team_stats_data.ints_made,
        ff=team_stats_data.ff,
        fr=team_stats_data.fr,
        def_turnovers=team_stats_data.def_turnovers,
        pass_def=team_stats_data.pass_def,
        safeties=team_stats_data.safeties,
        blocked_kicks=team_stats_data.blocked_kicks,
        def_tds=team_stats_data.def_tds,
        to_margin=team_stats_data.to_margin,
        kr_yds=team_stats_data.kr_yds,
        kr_tds=team_stats_data.kr_tds,
        pr_yds=team_stats_data.pr_yds,
        pr_tds=team_stats_data.pr_tds
    )

    return team_stats
