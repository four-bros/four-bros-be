from src.models.Player import PlayerDetails


class RushingStats:
    def __init__(
        self,
        rush_att,
        rush_yards,
        ya_contact,
        broke_tkls,
        fumbles,
        twenty_plus_yd_runs
    ):
        self.rush_att = rush_att
        self.rush_yards = rush_yards
        self.ya_contact = ya_contact
        self.broke_tkls = broke_tkls
        self.fumbles = fumbles
        self.twenty_plus_yd_runs = twenty_plus_yd_runs


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



class PlayerRushingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        rushing_stats: RushingStats
    ):
        self.player_details = player_details
        self.rushing_stats = rushing_stats


class PlayerPassingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        passing_stats: PassingStats
    ):

        self.player_details = player_details
        self. passing_stats = passing_stats
