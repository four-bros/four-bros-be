from typing import List

from src.constants import (
    defensive_stats_schema,
    kick_return_stats_schema
)
from src.data_services.DefensiveSeasonLeadersDataService import DefensiveSeasonLeadersDataService
from src.data_services.ReturnSeasonLeadersDataService import ReturnSeasonLeadersDataService
from src.data_services.WeekYearDataService import WeekYearDataService
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.WeekYearData import WeekYearData
from src.services.PlayersService import PlayersService
from src.models.Stats import (
    KickReturnStats,
    KickingStats,
    PassingStats,
    PlayerDefensiveStats,
    PlayerKickingStats,
    PlayerKickReturnStats,
    PlayerPassingStats,
    PlayerPuntingStats,
    PlayerPuntReturnStats,
    PlayerReceivingStats,
    PlayerReturnStats,
    PlayerRushingStats,
    PlayerTotalStats,
    PuntReturnStats,
    PuntingStats,
    ReceivingStats,
    RushingStats,
    TotalStats
)
from src.models.Player import (
    PlayerAbilities,
    PlayerAbilitiesDetailsStats,
    PlayerDetails,
    PlayerStats,
    PlayerHofInfo
)


class SeasonLeadersService():
    def __init__(self) -> None:
        self.PlayersService = PlayersService()
        self.DefensiveSeasonLeadersDataService = DefensiveSeasonLeadersDataService()
        self.ReturnSeasonLeadersDataService = ReturnSeasonLeadersDataService()
        self.WeekYearDataService = WeekYearDataService()

    def get_season_defensive_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        # Query the year to filter out irrelevant years
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        # Querying PlayerInfo first and DefensiveStats second will return
        # a set or tuple to the players variable.
        long_int_ret_data = self.DefensiveSeasonLeadersDataService.get_long_int_ret_leaders(
            week_year.year, is_season_specific, is_users_only)
        sacks_data = self.DefensiveSeasonLeadersDataService.get_sacks_leaders(
            week_year.year, is_season_specific, is_users_only)
        ff_data = self.DefensiveSeasonLeadersDataService.get_ff_leaders(
            week_year.year, is_season_specific, is_users_only)
        safeties_data = self.DefensiveSeasonLeadersDataService.get_safeties_leaders(
            week_year.year, is_season_specific, is_users_only)
        pass_def_data = self.DefensiveSeasonLeadersDataService.get_pass_def_leaders(
            week_year.year, is_season_specific, is_users_only)
        blocked_kicks_data = self.DefensiveSeasonLeadersDataService.get_blocked_kicks_leaders(
            week_year.year, is_season_specific, is_users_only)
        tfl_data = self.DefensiveSeasonLeadersDataService.get_tfl_leaders(
            week_year.year, is_season_specific, is_users_only)
        ints_made_data = self.DefensiveSeasonLeadersDataService.get_ints_made_leaders(
            week_year.year, is_season_specific, is_users_only)
        fr_data = self.DefensiveSeasonLeadersDataService.get_fr_leaders(
            week_year.year, is_season_specific, is_users_only)
        def_td_data = self.DefensiveSeasonLeadersDataService.get_def_td_leaders(
            week_year.year, is_season_specific, is_users_only)
        fr_yards_data = self.DefensiveSeasonLeadersDataService.get_fr_yards_leaders(
            week_year.year, is_season_specific, is_users_only)
        int_ret_yards_data = self.DefensiveSeasonLeadersDataService.get_int_ret_yards_leaders(
            week_year.year, is_season_specific, is_users_only)
        total_tkls_data = self.DefensiveSeasonLeadersDataService.get_total_tackles_leaders(
            week_year.year, is_season_specific, is_users_only)
        total_sacks_data = self.DefensiveSeasonLeadersDataService.get_total_sacks_leaders(
            week_year.year, is_season_specific, is_users_only)

        # Convert data into models
        converted_long_int_ret: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in long_int_ret_data]
        converted_sacks: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in sacks_data]
        converted_ff: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in ff_data]
        converted_safeties: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in safeties_data]
        converted_pass_def: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in pass_def_data]
        converted_blocked_kicks: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in blocked_kicks_data]
        converted_tfl: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in tfl_data]
        converted_ints_made: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in ints_made_data]
        converted_fr: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in fr_data]
        converted_def_td: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in def_td_data]
        converted_fr_yards: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in fr_yards_data]
        converted_int_ret_yards: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in int_ret_yards_data]
        converted_total_tkls: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in total_tkls_data]
        converted_total_sacks: List[PlayerDefensiveStats] = [
            self._get_player_season_defensive_stats(player) for player in total_sacks_data]

        # Convert top ten lists into json
        long_int_ret_leaders_json = defensive_stats_schema.dump(converted_long_int_ret)
        sacks_leaders_json = defensive_stats_schema.dump(converted_sacks)
        forced_fumbles_leaders_json = defensive_stats_schema.dump(converted_ff)
        safeties_leaders_json = defensive_stats_schema.dump(converted_safeties)
        pass_def_leaders_json = defensive_stats_schema.dump(converted_pass_def)
        blocked_kicks_leaders_json = defensive_stats_schema.dump(converted_blocked_kicks)
        tfl_leaders_json = defensive_stats_schema.dump(converted_tfl)
        ints_made_leaders_json = defensive_stats_schema.dump(converted_ints_made)
        fumbles_rec_leaders_json = defensive_stats_schema.dump(converted_fr)
        def_tds_leaders_json = defensive_stats_schema.dump(converted_def_td)
        fum_rec_yards_leaders_json = defensive_stats_schema.dump(converted_fr_yards)
        int_ret_yards_leaders_json = defensive_stats_schema.dump(converted_int_ret_yards)
        total_tkls_leaders_json = defensive_stats_schema.dump(converted_total_tkls)
        total_sacks_leaders_json = defensive_stats_schema.dump(converted_total_sacks)

        response = {
            'long_int_ret': long_int_ret_leaders_json,
            'sacks': sacks_leaders_json,
            'forced_fumbles': forced_fumbles_leaders_json,
            'safeties': safeties_leaders_json,
            'pass_def': pass_def_leaders_json,
            'blocked_kicks': blocked_kicks_leaders_json,
            'tfl': tfl_leaders_json,
            'ints_made': ints_made_leaders_json,
            'fumbles_rec': fumbles_rec_leaders_json,
            'def_tds': def_tds_leaders_json,
            'fum_rec_yards': fum_rec_yards_leaders_json,
            'int_ret_yards': int_ret_yards_leaders_json,
            'total_tkls': total_tkls_leaders_json,
            'total_sack': total_sacks_leaders_json
        }

        return response

    def get_season_kick_return_stats_leaders(self, is_season_specific: bool, is_users_only: bool):
        # Query the year to filter out irrelevant years
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        # Querying PlayerInfo first and SeasonReturnStatsData second will return
        # a set or tuple to the players variable.
        kick_returns_data = self.ReturnSeasonLeadersDataService.get_kick_return_leaders(week_year.year, is_season_specific, is_users_only)
        long_kr_data = self.ReturnSeasonLeadersDataService.get_long_kr_leaders(week_year.year, is_season_specific, is_users_only)
        kr_tds_data = self.ReturnSeasonLeadersDataService.get_kr_tds_leaders(week_year.year, is_season_specific, is_users_only)
        kr_yards_data = self.ReturnSeasonLeadersDataService.get_kr_yards_leaders(week_year.year, is_season_specific, is_users_only)
        kr_avg_data = self.ReturnSeasonLeadersDataService.get_kr_avg_leaders(week_year.year, is_season_specific, is_users_only)

        # Convert players to PlayerKickingStats model so they can be sorted
        converted_kick_returns: List[PlayerKickReturnStats] = [self._get_player_kick_return_stats(player) for player in kick_returns_data]
        converted_long_kr: List[PlayerKickReturnStats] = [self._get_player_kick_return_stats(player) for player in long_kr_data]
        converted_kr_tds: List[PlayerKickReturnStats] = [self._get_player_kick_return_stats(player) for player in kr_tds_data]
        converted_kr_yards: List[PlayerKickReturnStats] = [self._get_player_kick_return_stats(player) for player in kr_yards_data]
        converted_kr_avg_data: List[PlayerKickReturnStats] = [self._get_player_kick_return_stats(player) for player in kr_avg_data]

        # Convert top ten lists to json
        kick_return_leaders_json = kick_return_stats_schema.dump(converted_kick_returns)
        long_kr_leaders_json = kick_return_stats_schema.dump(converted_long_kr)
        kr_tds_leaders_json = kick_return_stats_schema.dump(converted_kr_tds)
        kr_yds_leaders_json = kick_return_stats_schema.dump(converted_kr_yards)
        kr_avg_leaders_json = kick_return_stats_schema.dump(converted_kr_avg_data)

        response = {
            'kick_returns': kick_return_leaders_json,
            'long_kr': long_kr_leaders_json,
            'kr_tds': kr_tds_leaders_json,
            'kr_yards': kr_yds_leaders_json,
            'kr_avg': kr_avg_leaders_json,
        }

        return response

    ########################################
    ####### Get player stats utils #########
    ########################################
    def _get_player_season_defensive_stats(self, player) -> PlayerDefensiveStats:

        player_info: PlayerInfoData = player[0]
        def_stats: SeasonDefensiveStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        defensive_stats: SeasonDefensiveStatsData = self.PlayersService._get_defensive_stats(
            defensive_stats_data=def_stats)

        player_defensive_stats: PlayerDefensiveStats = PlayerDefensiveStats(
            player_details=player_details,
            defensive_stats=defensive_stats
        )

        return player_defensive_stats
    
    def _get_player_kick_return_stats(self, player) -> PlayerReturnStats:
        player_info: PlayerInfoData = player[0]
        return_stats_data: SeasonReturnStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(player=player_info)
        return_stats: KickReturnStats = self.PlayersService._get_kick_return_stats(return_stats=return_stats_data)

        player_kick_return_stats: PlayerKickReturnStats = PlayerKickReturnStats(
            player_details=player_details,
            kick_return_stats=return_stats
        )

        return player_kick_return_stats

    def _get_player_season_passing_stats(self, player) -> PlayerPassingStats:

        player_info: PlayerInfoData = player[0]
        off_stats: SeasonOffensiveStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        passing_stats: PassingStats = self.PlayersService._get_passing_stats(
            offensive_stats=off_stats)

        player_passing_stats: PlayerPassingStats = PlayerPassingStats(
            player_details=player_details,
            passing_stats=passing_stats
        )

        return player_passing_stats

    def _get_player_season_receiving_stats(self, player) -> PlayerReceivingStats:

        player_info: PlayerInfoData = player[0]
        offensive_stats: SeasonOffensiveStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        receiving_stats: ReceivingStats = self.PlayersService._get_receiving_stats(
            offensive_stats=offensive_stats)

        player_receiving_stats: PlayerReceivingStats = PlayerReceivingStats(
            player_details=player_details,
            receiving_stats=receiving_stats
        )

        return player_receiving_stats

    def _get_player_rushing_stats(self, player) -> PlayerRushingStats:

        player_info: PlayerInfoData = player[0]
        offensive_stats: SeasonOffensiveStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        rushing_stats: RushingStats = self.PlayersService._get_rushing_stats(
            offensive_stats=offensive_stats)

        player_rushing_stats: PlayerRushingStats = PlayerRushingStats(
            player_details=player_details,
            rushing_stats=rushing_stats
        )

        return player_rushing_stats

    def _get_player_season_kicking_stats(self, player) -> PlayerKickingStats:

        player_info: PlayerInfoData = player[0]
        kicking_stats_data: SeasonKickingStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        kicking_stats: KickingStats = self.PlayersService._get_kicking_stats(
            kicking_stats=kicking_stats_data)

        player_kicking_stats: PlayerKickingStats = PlayerKickingStats(
            player_details=player_details,
            kicking_stats=kicking_stats
        )

        return player_kicking_stats

    def _get_player_kick_return_stats(self, player) -> PlayerReturnStats:

        player_info: PlayerInfoData = player[0]
        return_stats_data: SeasonReturnStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        return_stats: KickReturnStats = self.PlayersService._get_kick_return_stats(
            return_stats=return_stats_data)

        player_kick_return_stats: PlayerKickReturnStats = PlayerKickReturnStats(
            player_details=player_details,
            kick_return_stats=return_stats
        )

        return player_kick_return_stats

    def _get_player_season_punting_stats(self, player) -> PlayerPuntingStats:

        player_info: PlayerInfoData = player[0]
        kicking_stats_data: SeasonKickingStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        punting_stats: PuntingStats = self.PlayersService._get_punting_stats(
            punting_stats=kicking_stats_data)

        player_punting_stats: PlayerPuntingStats = PlayerPuntingStats(
            player_details=player_details,
            punting_stats=punting_stats
        )

        return player_punting_stats

    def _get_player_season_punt_return_stats(self, player) -> PlayerReturnStats:

        player_info: PlayerInfoData = player[0]
        return_stats_data: SeasonReturnStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        return_stats: PuntReturnStats = self.PlayersService._get_punt_return_stats(
            return_stats=return_stats_data)

        player_punt_return_stats: PlayerPuntReturnStats = PlayerPuntReturnStats(
            player_details=player_details,
            punt_return_stats=return_stats
        )

        return player_punt_return_stats

    def _get_player_season_total_off_stats(self, player) -> PlayerTotalStats:

        player_info: PlayerInfoData = player[0]
        off_stats_data: SeasonOffensiveStatsData = player[1]

        player_details: PlayerDetails = self.PlayersService._get_player_details(
            player=player_info)
        total_stats: TotalStats = self.PlayersService._get_total_stats(
            offensive_stats=off_stats_data)

        player_punt_return_stats: PlayerTotalStats = PlayerTotalStats(
            player_details=player_details,
            total_stats=total_stats
        )

        return player_punt_return_stats
