from src.models.Player import PlayerDetails


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


class PlayerPassingStats:
    def __init__(
                self,
                player_details: PlayerDetails,
                passing_stats: PassingStats
                ):

        self.player_details = player_details
        self. passing_stats = passing_stats
