from typing import List
from src.constants import (
    player_defensive_stats_schema,
    kicking_stats_schema,
    kick_return_stats_schema,
    passing_stats_schema,
    punting_stats_schema,
    punt_return_stats_schema,
    receiving_stats_schema,
    rushing_stats_schema,
    total_stats_schema,
    user_team_ids,
    users,
    Positions
)
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamSeasonStatsData import TeamSeasonStatsData
from src.data_models.WeekYearData import WeekYearData
from src.data_services.PlayersDataService import PlayersDataService
from src.data_services.PlayerSeasonStatsDataService import PlayerSeasonStatsDataService
from src.data_services.TeamInfoDataService import TeamInfoDataService
from src.data_services.TeamSeasonStatsDataService import TeamSeasonStatsDataService
from src.data_services.WeekYearDataService import WeekYearDataService
from src.services.PlayersSeasonStatsService import PlayersSeasonStatsService
from src.models.Teams import (
    TeamDetails,
    TeamInfo,
    TeamRoster,
    TeamRosterSummary,
    TeamSeasonStats,
)
from src.models.Stats import (
    PlayerDefensiveStats,
    PlayerKickingStats,
    PlayerPassingStats,
    PlayerPuntReturnStats,
    PlayerPuntingStats,
    PlayerReceivingStats,
    PlayerRushingStats,
    PlayerTotalStats
)
from src.schemas.Teams import (
    TeamDetailsSchema,
    TeamRosterSchema,
    TeamSeasonStatsSchema,
    team_details_schema,
    team_details_schema,
    team_roster_schema,
    teams_details_schema,
    team_stats_schema
)


class TeamsService():
    def __init__(self):
        self.PlayersDataService = PlayersDataService()
        self.PlayerSeasonStatsDataService = PlayerSeasonStatsDataService()
        self.PlayersSeasonStatsService = PlayersSeasonStatsService()
        self.TeamInfoDataService = TeamInfoDataService()
        self.TeamSeasonStatsDataService = TeamSeasonStatsDataService()
        self.WeekYearDataService = WeekYearDataService()

    def get_all_teams(self):
        teams: List[TeamInfoData] = self.TeamInfoDataService.get_all_teams()
        teams_json = teams_details_schema.dump(teams)

        response = {
            'teams': teams_json
        }

        return response

    def get_team_details_by_id(self, team_id) -> TeamDetailsSchema:
        team_info_data: TeamInfoData = self.TeamInfoDataService.get_team_info_by_id(
            team_id)
        players: List[PlayerInfoData] = self.PlayersDataService.get_players_by_team_id(
            team_id)
        team_details: TeamDetails = self._get_team_details(
            team_info=team_info_data, players=players)
        response: TeamDetailsSchema = team_details_schema.dump(team_details)

        return response

    def get_user_teams_details(self) -> List[TeamDetailsSchema]:
        response = {'data': []}

        for team_id in user_team_ids:
            team_info_data: TeamInfoData = self.TeamInfoDataService.get_team_info_by_id(
                team_id)
            players: List[PlayerInfoData] = self.PlayersDataService.get_players_by_team_id(
                team_id)
            team_details: TeamDetails = self._get_team_details(
                team_info=team_info_data, players=players)
            response['data'].append(team_details_schema.dump(team_details))

        return response

    def get_roster_by_team_id(self, team_id: int):
        players: List[PlayerInfoData] = self.PlayersDataService.get_players_by_team_id(
            team_id)
        team_roster: List[TeamRoster] = [
            self._get_team_roster(player) for player in players]
        team_roster_summary: TeamRosterSummary = TeamRosterSummary(
            roster=team_roster)
        response: TeamRosterSchema = team_roster_schema.dump(
            team_roster_summary)

        return response

    def get_team_player_stats_by_team_id(self, team_id: int):
        # Query the year to filter out irrelevant years
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        # Query the team to get the team_id
        team: TeamInfoData = self.TeamInfoDataService.get_team_info_by_id(
            team_id)
        # Get defensive stats
        defense_data = self.PlayerSeasonStatsDataService.get_defensive_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        defense_to_data = self.PlayerSeasonStatsDataService.get_def_to_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        # Get offensive stats
        passing_data = self.PlayerSeasonStatsDataService.get_passing_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        receiving_data = self.PlayerSeasonStatsDataService.get_receiving_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        rushing_data = self.PlayerSeasonStatsDataService.get_rushing_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        total_off_data = self.PlayerSeasonStatsDataService.get_total_off_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        # Get kicking stats
        kicking_data = self.PlayerSeasonStatsDataService.get_kicking_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        punting_data = self.PlayerSeasonStatsDataService.get_punting_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        # Get return stats
        kick_return_data = self.PlayerSeasonStatsDataService.get_kr_stats_by_team_id(
            team_id=team_id, year=week_year.year)
        punt_return_data = self.PlayerSeasonStatsDataService.get_pr_stats_by_team_id(
            team_id=team_id, year=week_year.year)

        # Convert players to the appropriate models based on stat category
        defensive_stats: List[PlayerDefensiveStats] = [
            self.PlayersSeasonStatsService._get_player_season_defensive_stats(player) for player in defense_data
        ]
        defensive_to_stats: List[PlayerDefensiveStats] = [
            self.PlayersSeasonStatsService._get_player_season_defensive_stats(player) for player in defense_to_data
        ]
        kick_return_stats: List[PlayerKickingStats] = [
            self.PlayersSeasonStatsService._get_player_kick_return_stats(player) for player in kick_return_data
        ]
        kick_stats: List[PlayerKickingStats] = [
            self.PlayersSeasonStatsService._get_player_season_kicking_stats(player) for player in kicking_data
        ]
        passing_stats: List[PlayerPassingStats] = [
            self.PlayersSeasonStatsService._get_player_season_passing_stats(player) for player in passing_data
        ]
        punt_return_stats: List[PlayerPuntReturnStats] = [
            self.PlayersSeasonStatsService._get_player_season_punt_return_stats(player) for player in punt_return_data
        ]
        punt_stats: List[PlayerPuntingStats] = [
            self.PlayersSeasonStatsService._get_player_season_punting_stats(player) for player in punting_data
        ]
        receiving_stats: List[PlayerReceivingStats] = [
            self.PlayersSeasonStatsService._get_player_season_receiving_stats(player) for player in receiving_data
        ]
        rushing_stats: List[PlayerRushingStats] = [
            self.PlayersSeasonStatsService._get_player_rushing_stats(player) for player in rushing_data
        ]
        total_off_stats: List[PlayerTotalStats] = [
            self.PlayersSeasonStatsService._get_player_season_total_off_stats(player) for player in total_off_data
        ]

        # Convert players to json for response
        defensive_stats_json = player_defensive_stats_schema.dump(
            defensive_stats)
        defensive_to_stats_json = player_defensive_stats_schema.dump(
            defensive_to_stats)
        kicking_stats_json = kicking_stats_schema.dump(kick_stats)
        kick_return_stats_json = kick_return_stats_schema.dump(
            kick_return_stats)
        passing_stats_json = passing_stats_schema.dump(passing_stats)
        punt_return_json = punt_return_stats_schema.dump(punt_return_stats)
        punting_stats_json = punting_stats_schema.dump(punt_stats)
        receiving_stats_json = receiving_stats_schema.dump(receiving_stats)
        rushing_stats_json = rushing_stats_schema.dump(rushing_stats)
        total_stats_json = total_stats_schema.dump(total_off_stats)

        response = {
            'defense': defensive_stats_json,
            'defense_to': defensive_to_stats_json,
            'kicking': kicking_stats_json,
            'kick_return': kick_return_stats_json,
            'passing': passing_stats_json,
            'punting': punting_stats_json,
            'punt_return': punt_return_json,
            'receiving': receiving_stats_json,
            'rushing': rushing_stats_json,
            'total': total_stats_json
        }

        return response

    def get_user_teams_player_stats(self):
        # Query the year to filter out irrelevant years
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        # Get defensive stats
        defense_data = self.PlayerSeasonStatsDataService.get_users_defensive_stats(
            week_year.year)
        defense_to_data = self.PlayerSeasonStatsDataService.get_users_def_to_stats(
            week_year.year)
        # Get offensive stats
        passing_data = self.PlayerSeasonStatsDataService.get_users_passing_stats(
            week_year.year)
        receiving_data = self.PlayerSeasonStatsDataService.get_users_receiving_stats(
            week_year.year)
        rushing_data = self.PlayerSeasonStatsDataService.get_users_rushing_stats(
            week_year.year)
        total_off_data = self.PlayerSeasonStatsDataService.get_users_total_off_stats(
            week_year.year)
        # Get kicking stats
        kicking_data = self.PlayerSeasonStatsDataService.get_users_kicking_stats(
            week_year.year)
        punting_data = self.PlayerSeasonStatsDataService.get_users_punting_stats(
            week_year.year)
        # Get return stats
        kick_return_data = self.PlayerSeasonStatsDataService.get_users_kr_stats(
            week_year.year)
        punt_return_data = self.PlayerSeasonStatsDataService.get_users_pr_stats(
            week_year.year)

        # Convert players to the appropriate models based on stat category
        defensive_stats: List[PlayerDefensiveStats] = [
            self.PlayersSeasonStatsService._get_player_season_defensive_stats(player) for player in defense_data
        ]
        defensive_to_stats: List[PlayerDefensiveStats] = [
            self.PlayersSeasonStatsService._get_player_season_defensive_stats(player) for player in defense_to_data
        ]
        kick_return_stats: List[PlayerKickingStats] = [
            self.PlayersSeasonStatsService._get_player_kick_return_stats(player) for player in kick_return_data
        ]
        kick_stats: List[PlayerKickingStats] = [
            self.PlayersSeasonStatsService._get_player_season_kicking_stats(player) for player in kicking_data
        ]
        passing_stats: List[PlayerPassingStats] = [
            self.PlayersSeasonStatsService._get_player_season_passing_stats(player) for player in passing_data
        ]
        punt_return_stats: List[PlayerPuntReturnStats] = [
            self.PlayersSeasonStatsService._get_player_season_punt_return_stats(player) for player in punt_return_data
        ]
        punt_stats: List[PlayerPuntingStats] = [
            self.PlayersSeasonStatsService._get_player_season_punting_stats(player) for player in punting_data
        ]
        receiving_stats: List[PlayerReceivingStats] = [
            self.PlayersSeasonStatsService._get_player_season_receiving_stats(player) for player in receiving_data
        ]
        rushing_stats: List[PlayerRushingStats] = [
            self.PlayersSeasonStatsService._get_player_rushing_stats(player) for player in rushing_data
        ]
        total_off_stats: List[PlayerTotalStats] = [
            self.PlayersSeasonStatsService._get_player_season_total_off_stats(player) for player in total_off_data
        ]

        # Convert players to json for response
        defensive_stats_json = player_defensive_stats_schema.dump(
            defensive_stats)
        defensive_to_stats_json = player_defensive_stats_schema.dump(
            defensive_to_stats)
        kicking_stats_json = kicking_stats_schema.dump(kick_stats)
        kick_return_stats_json = kick_return_stats_schema.dump(
            kick_return_stats)
        passing_stats_json = passing_stats_schema.dump(passing_stats)
        punt_return_json = punt_return_stats_schema.dump(punt_return_stats)
        punting_stats_json = punting_stats_schema.dump(punt_stats)
        receiving_stats_json = receiving_stats_schema.dump(receiving_stats)
        rushing_stats_json = rushing_stats_schema.dump(rushing_stats)
        total_stats_json = total_stats_schema.dump(total_off_stats)

        response = {
            'defense': defensive_stats_json,
            'defense_to': defensive_to_stats_json,
            'kicking': kicking_stats_json,
            'kick_return': kick_return_stats_json,
            'passing': passing_stats_json,
            'punting': punting_stats_json,
            'punt_return': punt_return_json,
            'receiving': receiving_stats_json,
            'rushing': rushing_stats_json,
            'total': total_stats_json
        }

        return response

    def get_team_stats_by_id(self, team_id: int):
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        team_stats_data: TeamSeasonStatsData = self.TeamSeasonStatsDataService.get_team_stats_by_id(
            team_id=team_id, year=week_year.year)

        if team_stats_data is None:
            return {}

        team_stats: TeamSeasonStats = self._get_team_season_stats(
            team_stats_data=team_stats_data)
        response: TeamSeasonStatsSchema = team_stats_schema.dump(team_stats)

        return response

    def get_user_teams_stats(self):
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()

        response = {'data': []}

        for user in users:
            team_stats_data: TeamSeasonStatsData = self.TeamSeasonStatsDataService.get_team_stats_by_id(
                user.team_id, week_year.year)

            if team_stats_data is None:
                continue

            team_stats: TeamSeasonStats = self._get_team_season_stats(team_stats_data=team_stats_data)

            team = {}
            team[team_stats.team_id] = team_stats_schema.dump(team_stats)

            response['data'].append(team)

        return response

    def _get_team_details(self, team_info: TeamInfoData, players: List[PlayerInfoData]) -> TeamDetails:
        offense_players: List[PlayerInfoData] = [
            player for player in players if player.position in Positions.offense_positions
        ]
        defense_players: List[PlayerInfoData] = [
            player for player in players if player.position in Positions.defense_positions
        ]
        sp_team_players: List[PlayerInfoData] = [
            player for player in players if player.position in Positions.sp_teams_positions
        ]

        avg_overall = round(
            sum([player.overall for player in players]) / len(players), 1)
        avg_offense = round(
            sum(player.overall for player in offense_players) / len(offense_players), 1)
        avg_defense = round(
            sum(player.overall for player in defense_players) / len(defense_players), 1)
        avg_sp_teams = round(
            sum(player.overall for player in sp_team_players) / len(sp_team_players), 1)

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

    def _get_team_info(self, team: TeamInfoData) -> TeamInfo:
        team_info: TeamInfo = TeamInfo(
            id=team.id,
            team_name=team.team_name,
            nickname=team.nickname,
            is_user=team.is_user,
        )

        return team_info

    def _get_team_roster(self, player: PlayerInfoData) -> TeamRoster:
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

    def _get_team_season_stats(self, team_stats_data: TeamSeasonStatsData):
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
