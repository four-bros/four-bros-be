from src.models.Player import PlayerDetails


class DefensiveStatsAll:
    def __init__(
        self,
        long_int_ret,
        sacks,
        year,
        forced_fumbles,
        solo_tkls,
        safeties,
        pass_def,
        blocked_kicks,
        tfl,
        ints_made,
        games_played,
        fumbles_rec,
        half_a_sack,
        asst_tkls,
        def_tds,
        fum_rec_yards,
        int_ret_yards,
    ):
        self.long_int_ret = long_int_ret
        self.sacks = sacks
        self.year = year
        self.forced_fumbles = forced_fumbles
        self.solo_tkls = solo_tkls
        self.safeties = safeties
        self.pass_def = pass_def
        self.blocked_kicks = blocked_kicks
        self.tfl = tfl
        self.ints_made = ints_made
        self.games_played = games_played
        self.fumbles_rec = fumbles_rec
        self.half_a_sack = half_a_sack
        self.asst_tkls = asst_tkls
        self.def_tds = def_tds
        self.fum_rec_yards = fum_rec_yards
        self.int_ret_yards = int_ret_yards


class PassingStats:
    def __init__(
        self,
        pass_yards,
        longest_pass,
        year,
        pass_tds,
        games_played,
        completions,
        ints,
        pass_att
    ):      

        self.pass_yards = pass_yards
        self.longest_pass = longest_pass
        self.year = year
        self.pass_tds = pass_tds
        self.games_played = games_played
        self.completions = completions
        self.ints = ints
        self.pass_att = pass_att


class RushingStats:
    def __init__(
        self,
        rush_att,
        rush_yards,
        ya_contact,
        broke_tkls,
        fumbles,
        twenty_plus_yd_runs,
        year
    ):
        self.rush_att = rush_att
        self.rush_yards = rush_yards
        self.ya_contact = ya_contact
        self.broke_tkls = broke_tkls
        self.fumbles = fumbles
        self.twenty_plus_yd_runs = twenty_plus_yd_runs
        self.year = year


class ReceivingStats:
    def __init__(
        self,
        receptions,
        rec_yards,
        rec_tds,
        yac,
        drops

    ):
        self.receptions = receptions
        self.rec_yards = rec_yards
        self.rec_tds = rec_tds
        self.yac = yac
        self.drops = drops


class PlayerDefensiveStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        defensive_stats: DefensiveStatsAll
    ):
        self.player_details = player_details
        self.defensive_stats = defensive_stats


class PlayerRushingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        rushing_stats: RushingStats
    ):
        self.player_details = player_details
        self.rushing_stats = rushing_stats


class PlayerReceivingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        receiving_stats: ReceivingStats
    ):
        self.player_details = player_details
        self.receiving_stats = receiving_stats


class PlayerPassingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        passing_stats: PassingStats
    ):

        self.player_details = player_details
        self. passing_stats = passing_stats
