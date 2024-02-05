from typing import List
from src.data_services.TeamSeasonStatsDataService import TeamSeasonStatsDataService
from src.data_services.WeekYearDataService import WeekYearDataService
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamSeasonStatsData import TeamSeasonStatsData
from src.data_models.WeekYearData import WeekYearData
from src.models.Teams import TeamInfo, TeamSeasonRecord, TeamSeasonStats
from src.schemas.Teams import team_season_records_schema


class TeamsSeasonStatsService():
    def __init__(self) -> None:
        self.TeamSeasonStatsDataService = TeamSeasonStatsDataService()
        self.WeekYearDataService = WeekYearDataService()

    def get_team_season_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        # Query Week/Year to get the current year
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        # Offensive Team Records Data
        total_points_data = self.TeamSeasonStatsDataService.get_total_points_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        total_yards_data = self.TeamSeasonStatsDataService.get_total_yards_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        ppg_data = self.TeamSeasonStatsDataService.get_ppg_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        pass_yds_data = self.TeamSeasonStatsDataService.get_pass_yards_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        pass_tds_data = self.TeamSeasonStatsDataService.get_pass_tds_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        ints_data = self.TeamSeasonStatsDataService.get_pass_ints_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        sacked_data = self.TeamSeasonStatsDataService.get_sacked_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        rush_yds_data = self.TeamSeasonStatsDataService.get_rush_yards_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        rush_tds_data = self.TeamSeasonStatsDataService.get_rush_tds_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        fumbles_data = self.TeamSeasonStatsDataService.get_fumbles_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        drops_data = self.TeamSeasonStatsDataService.get_drops_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        off_turnovers_data = self.TeamSeasonStatsDataService.get_off_turnovers_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        off_yards_data = self.TeamSeasonStatsDataService.get_off_yards_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        off_ypg_data = self.TeamSeasonStatsDataService.get_off_ypg_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        total_yards_data = self.TeamSeasonStatsDataService.get_total_yards_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        total_ypg_data = self.TeamSeasonStatsDataService.get_total_ypg_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )

        # Defensive Team Records Data
        sacks_data = self.TeamSeasonStatsDataService.get_sacks_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        tfl_data = self.TeamSeasonStatsDataService.get_tfl_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        ints_made_data = self.TeamSeasonStatsDataService.get_ints_made_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        ff_data = self.TeamSeasonStatsDataService.get_ff_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        fr_data = self.TeamSeasonStatsDataService.get_fr_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        def_turnovers_data = self.TeamSeasonStatsDataService.get_def_turnovers_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        pass_def_data = self.TeamSeasonStatsDataService.get_pass_def_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        safeties_data = self.TeamSeasonStatsDataService.get_safeties_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        blocked_kicks_data = self.TeamSeasonStatsDataService.get_blocked_kicks_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        def_tds_data = self.TeamSeasonStatsDataService.get_def_tds_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        to_margin_data = self.TeamSeasonStatsDataService.get_to_margin_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )

        # Special Teams Team Records Data
        kr_yds_data = self.TeamSeasonStatsDataService.get_kr_yards_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        kr_tds_data = self.TeamSeasonStatsDataService.get_kr_tds_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        pr_yds_data = self.TeamSeasonStatsDataService.get_pr_yards_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )
        pr_tds_data = self.TeamSeasonStatsDataService.get_pr_tds_leaders(
            year=week_year.year, is_season_specific=is_season_specific, is_users_only=is_users_only
        )

        # Convert data over to models to dump into json
        # Offense
        converted_total_points: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in total_points_data]
        converted_total_yards: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in total_yards_data]
        converted_total_ypg: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in total_ypg_data]
        converted_off_yards: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in off_yards_data]
        converted_off_ypg: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in off_ypg_data]
        converted_ppg: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in ppg_data]
        converted_pass_yds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in pass_yds_data]
        converted_pass_tds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in pass_tds_data]
        converted_ints: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in ints_data]
        converted_sacked: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in sacked_data]
        converted_rush_yds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in rush_yds_data]
        converted_rush_tds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in rush_tds_data]
        converted_fumbles: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in fumbles_data]
        converted_drops: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in drops_data]
        converted_off_turnovers: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in off_turnovers_data]
        # Defense
        converted_sacks: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in sacks_data]
        converted_tfl: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in tfl_data]
        converted_ints_made: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in ints_made_data]
        converted_ff: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in ff_data]
        converted_fr: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in fr_data]
        converted_def_turnovers: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in def_turnovers_data]
        converted_pass_def: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in pass_def_data]
        converted_safeties: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in safeties_data]
        converted_blocked_kicks: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in blocked_kicks_data]
        converted_def_tds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in def_tds_data]
        converted_to_margin: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in to_margin_data]
        # Special Teams
        converted_kr_yds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in kr_yds_data]
        converted_kr_tds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in kr_tds_data]
        converted_pr_yds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in pr_yds_data]
        converted_pr_tds: List[TeamSeasonRecord] = [
            self._get_team_info_and_season_stats(team) for team in pr_tds_data]

        # Dump models to json for api response
        # Offense
        total_points_json = team_season_records_schema.dump(
            converted_total_points)
        total_yards_json = team_season_records_schema.dump(
            converted_total_yards)
        total_ypg_json = team_season_records_schema.dump(converted_total_ypg)
        off_yards_json = team_season_records_schema.dump(converted_off_yards)
        off_ypg_json = team_season_records_schema.dump(converted_off_ypg)
        ppg_json = team_season_records_schema.dump(converted_ppg)
        pass_yds_json = team_season_records_schema.dump(converted_pass_yds)
        pass_tds_json = team_season_records_schema.dump(converted_pass_tds)
        ints_json = team_season_records_schema.dump(converted_ints)
        sacked_json = team_season_records_schema.dump(converted_sacked)
        rush_yds_json = team_season_records_schema.dump(converted_rush_yds)
        rush_tds_json = team_season_records_schema.dump(converted_rush_tds)
        fumbles_json = team_season_records_schema.dump(converted_fumbles)
        drops_json = team_season_records_schema.dump(converted_drops)
        off_turnovers_json = team_season_records_schema.dump(
            converted_off_turnovers)
        # Defense
        sacks_json = team_season_records_schema.dump(converted_sacks)
        tfl_json = team_season_records_schema.dump(converted_tfl)
        ints_made_json = team_season_records_schema.dump(converted_ints_made)
        ff_json = team_season_records_schema.dump(converted_ff)
        fr_json = team_season_records_schema.dump(converted_fr)
        def_turnovers_json = team_season_records_schema.dump(
            converted_def_turnovers)
        pass_def_json = team_season_records_schema.dump(converted_pass_def)
        safeties_json = team_season_records_schema.dump(converted_safeties)
        blocked_kicks_json = team_season_records_schema.dump(
            converted_blocked_kicks)
        def_tds_json = team_season_records_schema.dump(converted_def_tds)
        to_margin_json = team_season_records_schema.dump(converted_to_margin)
        # Special Teams
        kr_yds_json = team_season_records_schema.dump(converted_kr_yds)
        kr_tds_json = team_season_records_schema.dump(converted_kr_tds)
        pr_yds_json = team_season_records_schema.dump(converted_pr_yds)
        pr_tds_json = team_season_records_schema.dump(converted_pr_tds)

        response = {
            'offense': {
                'points': total_points_json,
                'off_yards': off_yards_json,
                'off_ypg': off_ypg_json,
                'total_yards': total_yards_json,
                'total_ypg': total_ypg_json,
                'ppg': ppg_json,
                'pass_yards': pass_yds_json,
                'pass_tds': pass_tds_json,
                'ints': ints_json,
                'sacked': sacked_json,
                'rush_yards': rush_yds_json,
                'rush_tds': rush_tds_json,
                'fumbles': fumbles_json,
                'drops': drops_json,
                'turnovers': off_turnovers_json
            },
            'defense': {
                'sacks': sacks_json,
                'tfl': tfl_json,
                'ints_made': ints_made_json,
                'ff': ff_json,
                'fr': fr_json,
                'turnovers': def_turnovers_json,
                'pass_def': pass_def_json,
                'safeties': safeties_json,
                'blocked_kicks': blocked_kicks_json,
                'def_td': def_tds_json,
                'to_margin': to_margin_json
            },
            'special_teams': {
                'kr_yds': kr_yds_json,
                'kr_tds': kr_tds_json,
                'pr_yds': pr_yds_json,
                'pr_tds': pr_tds_json,
            }
        }

        return response

    def _get_team_info_and_season_stats(self, team):
        team_info_data: TeamInfoData = team[0]
        team_stats_data: TeamSeasonStatsData = team[1]

        team_info: TeamInfo = self._get_team_info(team_info_data)
        team_stats: TeamSeasonStats = self._get_team_season_stats(
            team_stats_data)

        team_season_record: TeamSeasonRecord = TeamSeasonRecord(
            team_info=team_info,
            team_stats=team_stats
        )

        return team_season_record

    def _get_team_info(self, team: TeamInfoData) -> TeamInfo:
        team_info: TeamInfo = TeamInfo(
            id=team.id,
            team_name=team.team_name,
            nickname=team.nickname,
            is_user=team.is_user,
        )

        return team_info

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
