from typing import List

from src.constants import Positions
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamStatsData import TeamStatsData
from src.models.Teams import (
    TeamDetails,
    TeamInfo,
    TeamRoster,
    TeamStats
)


################################################
########## Get team info and stats #############
################################################
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
        team_short_name=team.team_short_name,
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


def _get_team_stats(team_stats_data: TeamStatsData):

    team_stats: TeamStats = TeamStats(
        team_id=team_stats_data.team_id,
        year=team_stats_data.year,
        games_played=team_stats_data.games_played,
        total_points=team_stats_data.total_points,
        ppg=team_stats_data.ppg,
        pass_yds=team_stats_data.pass_yds,
        pass_ypg=team_stats_data.pass_ypg,
        pass_tds=team_stats_data.pass_tds,
        rush_yds=team_stats_data.rush_yds,
        rush_ypg=team_stats_data.rush_ypg,
        rush_tds=team_stats_data.rush_tds,
        rec_yds=team_stats_data.rec_yds,
        rec_ypg=team_stats_data.rec_ypg,
        rec_tds=team_stats_data.rec_tds,
        total_yds=team_stats_data.total_yards,
        total_ypg=team_stats_data.total_ypg,
        sacks=team_stats_data.sacks,
        ints=team_stats_data.ints,
        ff=team_stats_data.ff,
        fr=team_stats_data.fr,
        turnovers=team_stats_data.turnovers,
        pass_def=team_stats_data.pass_def,
        safeties=team_stats_data.safeties,
        blocked_kicks=team_stats_data.blocked_kicks,
        def_tds=team_stats_data.def_tds,
        kr_yds=team_stats_data.kr_yds,
        kr_tds=team_stats_data.kr_tds,
        pr_yds=team_stats_data.pr_yds,
        pr_tds=team_stats_data.pr_tds
    )

    return team_stats
