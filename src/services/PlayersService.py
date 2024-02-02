from typing import List, Union
from src.constants import (
    player_schema_list,
    player_schema_single,
    player_hof_schema_list
)
from src.data_services.PlayersCareerStatsDataService import PlayersCareerStatsDataService
from src.data_services.PlayersDataService import PlayersDataService
from src.data_services.PlayersGameStatsDataService import PlayersGameStatsDataService
from src.data_services.PlayerSeasonStatsDataService import PlayerSeasonStatsDataService
from src.data_services.TeamInfoDataService import TeamInfoDataService
from src.data_services.WeekYearDataService import WeekYearDataService
from src.data_models.HallOfFame import HallOfFame
from src.data_models.PlayerInfoData import PlayerInfoData
from src.models.Player import (
    PlayerAbilities,
    PlayerAbilitiesDetailsStats,
    PlayerDetails,
    PlayerStats,
    PlayerHofInfo,
    PlayerStatsList
)
from src.data_models.CareerDefensiveStatsData import CareerDefensiveStatsData
from src.data_models.CareerKickingStatsData import CareerKickingStatsData
from src.data_models.CareerOffensiveStatsData import CareerOffensiveStatsData
from src.data_models.CareerReturnStatsData import CareerReturnStatsData
from src.data_models.GameDefensiveStatsData import GameDefensiveStatsData
from src.data_models.GameKickingStatsData import GameKickingStatsData
from src.data_models.GameOffensiveStatsData import GameOffensiveStatsData
from src.data_models.GameReturnStatsData import GameReturnStatsData
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.WeekYearData import WeekYearData
from src.models.Stats import (
    DefensiveStats,
    KickingStats,
    KickReturnStats,
    PassingStats,
    PuntingStats,
    PuntReturnStats,
    ReceivingStats,
    RushingStats,
    TotalStats
)
from src.schemas.Players import PlayerSchema


class PlayersService():
    def __init__(self) -> None:
        self.PlayersCareerStatsDataService = PlayersCareerStatsDataService()
        self.PlayersDataService = PlayersDataService()
        self.PlayersGameStatsDataService = PlayersGameStatsDataService()
        self.PlayerSeasonStatsDataService = PlayerSeasonStatsDataService()
        self.TeamInfoDataService = TeamInfoDataService()
        self.WeekYearDataService = WeekYearDataService()

    def get_all_players(self):
        players: List[PlayerInfoData] = self.PlayersDataService.get_all_players()
        converted_players: List[PlayerAbilitiesDetailsStats] = [
            self._get_player_abilities_details_stats(player) for player in players]
        players_json = player_schema_list.dump(converted_players)
        response = {'players': players_json}

        return response

    def get_player_by_player_id(self, player_id: str) -> PlayerSchema:
        player: PlayerInfoData = self.PlayersDataService.get_player_by_player_id(
            player_id)
        converted_player: PlayerAbilitiesDetailsStats = self._get_player_abilities_details_stats(
            player)
        response: PlayerSchema = player_schema_single.dump(converted_player)

        return response

    def get_hof(self):
        hof: List[HallOfFame] = self.PlayersDataService.get_hof()
        player_ids: List[str] = [player.player_id for player in hof]
        players: List[PlayerInfoData] = self.PlayersDataService.get_hof_player_info(
            player_ids)
        converted_players: List[PlayerHofInfo] = [
            self._get_player_hof_info(player) for player in players]
        players_json = player_hof_schema_list.dump(converted_players)

        response = {
            'players': players_json
        }

        return response

    def _get_player_abilities_details_stats(self, player: PlayerInfoData) -> PlayerAbilitiesDetailsStats:
        player_details: PlayerDetails = self._get_player_details(player=player)
        player_abilities: PlayerAbilities = self._get_player_abilities(
            player=player)
        season_stats: PlayerStats = self._get_player_current_season_stats(
            player=player)
        career_stats: PlayerStats = self._get_player_career_stats(
            player=player)
        game_stats: PlayerStats = self._get_player_game_stats(player=player)

        player_abilities_details_stats: PlayerAbilitiesDetailsStats = PlayerAbilitiesDetailsStats(
            details=player_details,
            abilities=player_abilities,
            career_stats=career_stats,
            season_stats=season_stats,
            game_stats=game_stats
        )

        return player_abilities_details_stats

    def _get_player_career_stats(self, player: PlayerInfoData) -> PlayerStats:
        offensive_stats_data: List[CareerOffensiveStatsData] = self.PlayersCareerStatsDataService.get_offensive_stats(
            player.id)
        defensive_stats_data: List[CareerDefensiveStatsData] = self.PlayersCareerStatsDataService.get_defensive_stats(
            player.id)
        return_stats_data: List[CareerReturnStatsData] = self.PlayersCareerStatsDataService.get_return_stats(
            player.id)
        kicking_stats_data: List[CareerKickingStatsData] = self.PlayersCareerStatsDataService.get_kicking_stats(
            player.id)

        passing_stats: PassingStats = None
        receiving_stats: ReceivingStats = None
        rushing_stats: RushingStats = None
        defensive_stats: DefensiveStats = None
        kicking_stats: KickingStats = None
        kick_return_stats: KickReturnStats = None
        punting_stats: PuntingStats = None
        punt_return_stats: PuntReturnStats = None
        total_stats: TotalStats = None

        if offensive_stats_data:
            passing_stats = self._get_passing_stats(offensive_stats_data)
            receiving_stats = self._get_receiving_stats(offensive_stats_data)
            rushing_stats = self._get_rushing_stats(offensive_stats_data)
            total_stats = self._get_total_stats(offensive_stats_data)
        if defensive_stats_data:
            defensive_stats = self._get_defensive_stats(defensive_stats_data)
        if return_stats_data:
            kick_return_stats = self._get_kick_return_stats(return_stats_data)
            punt_return_stats = self._get_punt_return_stats(return_stats_data)
        if kicking_stats_data:
            kicking_stats = self._get_kicking_stats(kicking_stats_data)
            punting_stats = self._get_punting_stats(kicking_stats_data)

        player_stats: PlayerStats = PlayerStats(
            passing=passing_stats,
            rushing=rushing_stats,
            receiving=receiving_stats,
            defensive=defensive_stats,
            kicking=kicking_stats,
            kick_return=kick_return_stats,
            punting=punting_stats,
            punt_return=punt_return_stats,
            total=total_stats
        )

        return player_stats

    def _get_player_game_stats(self, player: PlayerInfoData) -> PlayerStats:
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        offensive_stats_data: GameOffensiveStatsData = self.PlayersGameStatsDataService.get_offensive_stats(
            player.id, week_year.year)
        defensive_stats_data: GameDefensiveStatsData = self.PlayersGameStatsDataService.get_defensive_stats(
            player.id, week_year.year)
        return_stats_data: GameReturnStatsData = self.PlayersGameStatsDataService.get_return_stats(
            player.id, week_year.year)
        kicking_stats_data: GameKickingStatsData = self.PlayersGameStatsDataService.get_kicking_stats(
            player.id, week_year.year)

        passing_stats: List[PassingStats] = None
        receiving_stats: List[ReceivingStats] = None
        rushing_stats: List[RushingStats] = None
        defensive_stats: List[DefensiveStats] = None
        kicking_stats: List[KickingStats] = None
        kick_return_stats: List[KickReturnStats] = None
        punting_stats: List[PuntingStats] = None
        punt_return_stats: List[PuntReturnStats] = None
        total_stats: List[TotalStats] = None

        if offensive_stats_data:
            passing_stats = [self._get_passing_stats(
                game) for game in offensive_stats_data]
            receiving_stats = [self._get_receiving_stats(
                game) for game in offensive_stats_data]
            rushing_stats = [self._get_rushing_stats(
                game) for game in offensive_stats_data]
            total_stats = [self._get_total_stats(
                game) for game in offensive_stats_data]
        if defensive_stats_data:
            defensive_stats = [self._get_defensive_stats(
                game) for game in defensive_stats_data]
        if return_stats_data:
            kick_return_stats = [self._get_kick_return_stats(
                game) for game in return_stats_data]
            punt_return_stats = [self._get_punt_return_stats(
                game) for game in return_stats_data]
        if kicking_stats_data:
            kicking_stats = [self._get_kicking_stats(
                game) for game in kicking_stats_data]
            punting_stats = [self._get_punting_stats(
                game) for game in kicking_stats_data]

        player_stats: PlayerStatsList = PlayerStatsList(
            passing=passing_stats,
            rushing=rushing_stats,
            receiving=receiving_stats,
            defensive=defensive_stats,
            kicking=kicking_stats,
            kick_return=kick_return_stats,
            punting=punting_stats,
            punt_return=punt_return_stats,
            total=total_stats
        )

        return player_stats

    def _get_player_current_season_stats(self, player: PlayerInfoData) -> PlayerStats:
        week_year: WeekYearData = self.WeekYearDataService.get_week_year()
        offensive_stats_data: SeasonOffensiveStatsData = self.PlayerSeasonStatsDataService.get_offensive_stats_by_year(
            player.id, week_year.year)
        defensive_stats_data: SeasonDefensiveStatsData = self.PlayerSeasonStatsDataService.get_defensive_stats_by_year(
            player.id, week_year.year)
        return_stats_data: SeasonReturnStatsData = self.PlayerSeasonStatsDataService.get_return_stats_by_year(
            player.id, week_year.year)
        kicking_stats_data: SeasonKickingStatsData = self.PlayerSeasonStatsDataService.get_kicking_stats_by_year(
            player.id, week_year.year)

        passing_stats: PassingStats = None
        receiving_stats: ReceivingStats = None
        rushing_stats: RushingStats = None
        defensive_stats: DefensiveStats = None
        kicking_stats: KickingStats = None
        kick_return_stats: KickReturnStats = None
        punting_stats: PuntingStats = None
        punt_return_stats: PuntReturnStats = None
        total_stats: TotalStats = None

        if offensive_stats_data:
            passing_stats = self._get_passing_stats(offensive_stats_data)
            receiving_stats = self._get_receiving_stats(offensive_stats_data)
            rushing_stats = self._get_rushing_stats(offensive_stats_data)
            total_stats = self._get_total_stats(offensive_stats_data)
        if defensive_stats_data:
            defensive_stats = self._get_defensive_stats(defensive_stats_data)
        if return_stats_data:
            kick_return_stats = self._get_kick_return_stats(return_stats_data)
            punt_return_stats = self._get_punt_return_stats(return_stats_data)
        if kicking_stats_data:
            kicking_stats = self._get_kicking_stats(kicking_stats_data)
            punting_stats = self._get_punting_stats(kicking_stats_data)

        player_stats: PlayerStats = PlayerStats(
            passing=passing_stats,
            rushing=rushing_stats,
            receiving=receiving_stats,
            defensive=defensive_stats,
            kicking=kicking_stats,
            kick_return=kick_return_stats,
            punting=punting_stats,
            punt_return=punt_return_stats,
            total=total_stats
        )

        return player_stats

    # Compiling Stats utils
    def _get_player_abilities(self, player: PlayerInfoData) -> PlayerAbilities:
        player_abilities: PlayerAbilities = PlayerAbilities(
            play_recognition=player.play_recognition,
            press=player.press,
            power_moves=player.power_moves,
            kick_accuracy=player.kick_accuracy,
            throwing_power=player.throwing_power,
            throwing_accuracy=player.throwing_accuracy,
            overall=player.overall,
            agility=player.agility,
            stamina=player.stamina,
            acceleration=player.acceleration,
            pursuit=player.pursuit,
            route_running=player.route_running,
            speed=player.speed,
            trucking=player.trucking,
            ball_carrier_vision=player.ball_carrier_vision,
            catch_in_traffic=player.catch_in_traffic,
            block_shedding=player.block_shedding,
            strength=player.strength,
            catch=player.catch,
            injury=player.injury,
            tackling=player.tackling,
            pass_blocking=player.pass_blocking,
            run_blocking=player.run_blocking,
            break_tackle=player.break_tackle,
            impact_blocking=player.impact_blocking,
            jump=player.jump,
            carry=player.carry,
            stiff_arm=player.stiff_arm,
            kick_power=player.kick_power,
            awareness=player.awareness,
            release=player.release,
            spec_catch=player.spec_catch,
            elusiveness=player.elusiveness,
            spin_move=player.spin_move,
            hit_power=player.hit_power,
            kick_return=player.kick_return,
            man_coverage=player.man_coverage,
            zone_coverage=player.zone_coverage,
            finesse_moves=player.finesse_moves,
            juke_move=player.juke_move,
        )

        return player_abilities

    def _get_player_details(self, player: PlayerInfoData) -> PlayerDetails:
        team_info: TeamInfoData = self.TeamInfoDataService.get_team_info_by_id(
            player.team_id)

        player_details: PlayerDetails = PlayerDetails(
            id=player.id,
            team_id=player.team_id,
            team_name=team_info.team_name,
            first_name=player.first_name,
            last_name=player.last_name,
            height=player.height,
            weight=player.weight,
            jersey_number=player.jersey_number,
            player_year=player.player_year,
            redshirt=player.redshirt,
            position=player.position,
            hometown_desc=player.hometown_desc
        )

        return player_details

    def _get_player_hof_info(self, player: PlayerInfoData) -> PlayerHofInfo:
        player_details: PlayerDetails = self._get_player_details(player=player)
        player_abilities: PlayerAbilities = self._get_player_abilities(player=player)
        season_stats: List[PlayerStats] = self._get_player_all_season_stats(player=player)
        career_stats: PlayerStats = self._get_player_career_stats(player=player)

        player_hof_info = PlayerHofInfo(
            details=player_details,
            abilities=player_abilities,
            career_stats=career_stats,
            season_stats=season_stats
        )

        return player_hof_info

    def _get_player_all_season_stats(self, player: PlayerInfoData) -> List[PlayerStats]:
        offensive_stats_data: List[SeasonOffensiveStatsData] = self.PlayerSeasonStatsDataService.get_all_offensive_stats(player.id)
        defensive_stats_data: List[SeasonDefensiveStatsData] = self.PlayerSeasonStatsDataService.get_all_defensive_stats(player.id)
        return_stats_data: List[SeasonReturnStatsData] = self.PlayerSeasonStatsDataService.get_all_return_stats(player.id)
        kicking_stats_data: List[SeasonKickingStatsData] = self.PlayerSeasonStatsDataService.get_all_kicking_stats(player.id)

        passing_stats: List[PassingStats] = []
        receiving_stats: List[ReceivingStats] = []
        rushing_stats: List[RushingStats] = []
        defensive_stats: List[DefensiveStats] = []
        kicking_stats: List[KickingStats] = []
        kick_return_stats: List[KickReturnStats] = []
        punting_stats: List[PuntingStats] = []
        punt_return_stats: List[PuntReturnStats] = []
        total_stats: List[TotalStats] = []

        if len(offensive_stats_data) > 0:
            passing_stats = [self._get_passing_stats(
                season) for season in offensive_stats_data]
            receiving_stats = [self._get_receiving_stats(
                season) for season in offensive_stats_data]
            rushing_stats = [self._get_rushing_stats(
                season) for season in offensive_stats_data]
            total_stats = [self._get_total_stats(
                season) for season in offensive_stats_data]
        if len(defensive_stats_data) > 0:
            defensive_stats = [self._get_defensive_stats(
                season) for season in defensive_stats_data]
        if len(return_stats_data) > 0:
            kick_return_stats = [self._get_kick_return_stats(
                season) for season in return_stats_data]
            punt_return_stats = [self._get_punt_return_stats(
                season) for season in return_stats_data]
        if len(kicking_stats_data) > 0:
            kicking_stats = [self._get_kicking_stats(
                season) for season in kicking_stats_data]
            punting_stats = [self._get_punting_stats(
                season) for season in kicking_stats_data]

        player_stats: PlayerStatsList = PlayerStatsList(
            passing=passing_stats,
            rushing=rushing_stats,
            receiving=receiving_stats,
            defensive=defensive_stats,
            kicking=kicking_stats,
            kick_return=kick_return_stats,
            punting=punting_stats,
            punt_return=punt_return_stats,
            total=total_stats
        )

        return player_stats

    def _get_passing_stats(
        self,
        offensive_stats: Union[CareerOffensiveStatsData,
                               GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> PassingStats:
        passing_stats: PassingStats = PassingStats(
            pass_yards=offensive_stats.pass_yards,
            longest_pass=offensive_stats.longest_pass,
            year=offensive_stats.year,
            pass_tds=offensive_stats.pass_tds,
            games_played=offensive_stats.games_played,
            completions=offensive_stats.completions,
            ints=offensive_stats.ints,
            pass_att=offensive_stats.pass_att,
            pass_ypa=offensive_stats.pass_ypa,
            pass_ypg=offensive_stats.pass_ypg,
            pass_rating=offensive_stats.pass_rating,
            sacked=offensive_stats.sacked,
            comp_pct=offensive_stats.comp_pct
        )

        return passing_stats

    def _get_receiving_stats(
        self,
        offensive_stats: Union[CareerOffensiveStatsData,
                               GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> ReceivingStats:
        receiving_stats: ReceivingStats = ReceivingStats(
            receptions=offensive_stats.receptions,
            rec_yards=offensive_stats.rec_yards,
            rec_tds=offensive_stats.rec_tds,
            yac=offensive_stats.yac,
            drops=offensive_stats.drops,
            rec_ypc=offensive_stats.rec_ypc,
            rec_ypg=offensive_stats.rec_ypg,
            games_played=offensive_stats.games_played,
            year=offensive_stats.year,
            longest_rec=offensive_stats.longest_rec
        )

        return receiving_stats

    def _get_rushing_stats(
        self,
        offensive_stats: Union[CareerOffensiveStatsData,
                               GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> RushingStats:
        rushing_stats: RushingStats = RushingStats(
            rush_att=offensive_stats.rush_att,
            rush_yards=offensive_stats.rush_yards,
            rush_tds=offensive_stats.rush_tds,
            ya_contact=offensive_stats.ya_contact,
            broke_tkls=offensive_stats.broke_tkls,
            fumbles=offensive_stats.fumbles,
            twenty_plus_yd_runs=offensive_stats.twenty_plus_yd_runs,
            rush_ypc=offensive_stats.rush_ypc,
            rush_ypg=offensive_stats.rush_ypg,
            games_played=offensive_stats.games_played,
            year=offensive_stats.year,
            longest_run=offensive_stats.longest_run
        )

        return rushing_stats

    def _get_total_stats(
        self,
        offensive_stats: Union[CareerOffensiveStatsData,
                               GameOffensiveStatsData, SeasonOffensiveStatsData]
    ) -> TotalStats:
        total_stats: TotalStats = TotalStats(
            total_yards=offensive_stats.total_yards,
            total_tds=offensive_stats.total_tds,
            total_ypg=offensive_stats.total_ypg,
            games_played=offensive_stats.games_played,
            year=offensive_stats.year,
            turnovers=offensive_stats.turnovers
        )

        return total_stats

    def _get_defensive_stats(
        self,
        defensive_stats_data: Union[CareerDefensiveStatsData,
                                    GameDefensiveStatsData, SeasonDefensiveStatsData]
    ) -> DefensiveStats:
        defensive_stats = DefensiveStats(
            long_int_ret=defensive_stats_data.long_int_ret,
            sacks=defensive_stats_data.sacks,
            year=defensive_stats_data.year,
            forced_fumbles=defensive_stats_data.forced_fumbles,
            solo_tkls=defensive_stats_data.solo_tkls,
            safeties=defensive_stats_data.safeties,
            pass_def=defensive_stats_data.pass_def,
            blocked_kicks=defensive_stats_data.blocked_kicks,
            tfl=defensive_stats_data.tfl,
            ints_made=defensive_stats_data.ints_made,
            games_played=defensive_stats_data.games_played,
            fumbles_rec=defensive_stats_data.fumbles_rec,
            half_a_sack=defensive_stats_data.half_a_sack,
            asst_tkls=defensive_stats_data.asst_tkls,
            def_tds=defensive_stats_data.def_tds,
            fum_rec_yards=defensive_stats_data.fum_rec_yards,
            int_ret_yards=defensive_stats_data.int_ret_yards,
            total_tkls=defensive_stats_data.total_tkls,
            total_sacks=defensive_stats_data.total_sacks
        )

        return defensive_stats

    def _get_kicking_stats(
        self,
        kicking_stats: Union[CareerKickingStatsData,
                             GameKickingStatsData, SeasonKickingStatsData]
    ) -> KickingStats:
        kicking_stats_all: KickingStats = KickingStats(
            fg_made_17_29=kicking_stats.fg_made_17_29,
            fg_att_17_29=kicking_stats.fg_att_17_29,
            long_fg=kicking_stats.long_fg,
            ko_touchbacks=kicking_stats.ko_touchbacks,
            xp_att=kicking_stats.xp_att,
            year=kicking_stats.year,
            fg_att=kicking_stats.fg_att,
            xp_blocked=kicking_stats.xp_blocked,
            fg_blocked=kicking_stats.fg_blocked,
            fg_att_40_49=kicking_stats.fg_att_40_49,
            fg_made_40_49=kicking_stats.fg_made_40_49,
            fg_att_30_39=kicking_stats.fg_att_30_39,
            fg_made_30_39=kicking_stats.fg_made_30_39,
            fg_att_50_plus=kicking_stats.fg_att_50_plus,
            fg_made_50_plus=kicking_stats.fg_made_50_plus,
            games_played=kicking_stats.games_played,
            kickoffs=kicking_stats.kickoffs,
            xp_made=kicking_stats.xp_made,
            fg_made=kicking_stats.fg_made,
            fg_pct=kicking_stats.fg_pct,
            xp_pct=kicking_stats.xp_pct,
            fg_50_plus_pct=kicking_stats.fg_50_plus_pct
        )

        return kicking_stats_all

    def _get_kick_return_stats(
        self,
        return_stats: Union[CareerReturnStatsData,
                            GameReturnStatsData, SeasonReturnStatsData]
    ) -> KickReturnStats:
        kick_return_stats: KickReturnStats = KickReturnStats(
            kick_returns=return_stats.kick_returns,
            year=return_stats.year,
            long_kr=return_stats.long_kr,
            games_played=return_stats.games_played,
            kr_tds=return_stats.kr_tds,
            kr_yds=return_stats.kr_yds,
            kr_avg=return_stats.kr_avg
        )

        return kick_return_stats

    def _get_punting_stats(
        self,
        punting_stats: Union[CareerKickingStatsData,
                             GameKickingStatsData, SeasonKickingStatsData]
    ) -> PuntingStats:
        punting_stats: PuntingStats = PuntingStats(
            long_punt=punting_stats.long_punt,
            year=punting_stats.year,
            punts_blocked=punting_stats.punts_blocked,
            total_punt_yards=punting_stats.total_punt_yards,
            punt_touchbacks=punting_stats.punt_touchbacks,
            games_played=punting_stats.games_played,
            net_punting=punting_stats.net_punting,
            number_punts=punting_stats.number_punts,
            inside_twenty=punting_stats.inside_twenty,
            punt_avg=punting_stats.punt_avg,
            net_avg=punting_stats.net_avg
        )

        return punting_stats

    def _get_punt_return_stats(
        self,
        return_stats: Union[CareerReturnStatsData,
                            GameReturnStatsData, SeasonReturnStatsData]
    ) -> PuntReturnStats:
        punt_return_stats: PuntReturnStats = PuntReturnStats(
            year=return_stats.year,
            punt_returns=return_stats.punt_returns,
            long_pr=return_stats.long_pr,
            games_played=return_stats.games_played,
            pr_tds=return_stats.pr_tds,
            pr_yds=return_stats.pr_yds,
            pr_avg=return_stats.pr_avg
        )

        return punt_return_stats
