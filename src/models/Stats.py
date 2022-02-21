# Create Player Details Model to avoid circular import
class PlayerDetails:
    def __init__(
        self,
        id,
        team_id,
        team_name,
        first_name,
        last_name,
        height,
        weight,
        jersey_number,
        player_year,
        redshirt,
        position,
        hometown_desc
    ):

        self.id = id
        self.team_id = team_id
        self.team_name = team_name
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.jersey_number = jersey_number
        self.player_year = player_year
        self.redshirt = redshirt
        self.position = position
        self.hometown_desc = hometown_desc

class DefensiveStats:
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
        total_tkls
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
        self.total_tkls = total_tkls

class KickingStats:
    def __init__(
        self,
        fg_made_17_29,
        fg_att_17_29,
        long_fg,
        ko_touchbacks,
        long_punt,
        xp_att,
        year,
        punts_blocked,
        fg_att,
        total_punt_yards,
        xp_blocked,
        fg_blocked,
        fg_att_40_49,
        fg_made_40_49,
        fg_att_30_39,
        fg_made_30_39,
        fg_att_50_plus,
        fg_made_50_plus,
        punt_touchbacks,
        games_played,
        kickoffs,
        xp_made,
        net_punting,
        fg_made,
        number_punts,
        inside_twenty,
    ):
        self.fg_made_17_29 = fg_made_17_29
        self.fg_att_17_29 = fg_att_17_29
        self.long_fg = long_fg
        self.ko_touchbacks = ko_touchbacks
        self.long_punt = long_punt
        self.xp_att = xp_att
        self.year = year
        self.punts_blocked = punts_blocked
        self.fg_att = fg_att
        self.total_punt_yards = total_punt_yards
        self.xp_blocked = xp_blocked
        self.fg_blocked = fg_blocked
        self.fg_att_40_49 = fg_att_40_49
        self.fg_made_40_49 = fg_made_40_49
        self.fg_att_30_39 = fg_att_30_39
        self.fg_made_30_39 = fg_made_30_39
        self.fg_att_50_plus = fg_att_50_plus
        self.fg_made_50_plus = fg_made_50_plus
        self.punt_touchbacks = punt_touchbacks
        self.games_played = games_played
        self.kickoffs = kickoffs
        self.xp_made = xp_made
        self.net_punting = net_punting
        self.fg_made = fg_made
        self.number_punts = number_punts
        self.inside_twenty = inside_twenty


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
        pass_att,
        pass_yp_attempt,
        pass_yp_game,
        pass_rating
    ):      

        self.pass_yards = pass_yards
        self.longest_pass = longest_pass
        self.year = year
        self.pass_tds = pass_tds
        self.games_played = games_played
        self.completions = completions
        self.ints = ints
        self.pass_att = pass_att
        self.pass_yp_attempt = pass_yp_attempt
        self.pass_yp_game = pass_yp_game
        self.pass_rating = pass_rating


class ReceivingStats:
    def __init__(
        self,
        receptions,
        rec_yards,
        rec_tds,
        yac,
        drops,
        rec_yp_catch,
        rec_yp_game,
        games_played

    ):
        self.receptions = receptions
        self.rec_yards = rec_yards
        self.rec_tds = rec_tds
        self.yac = yac
        self.drops = drops
        self.rec_yp_catch = rec_yp_catch
        self.rec_yp_game = rec_yp_game
        self.games_played = games_played


class ReturnStats:
    def __init__(
        self,
        kick_returns,
        year,
        long_kr,
        punt_returns,
        long_pr,
        games_played,
        kr_tds,
        pr_tds,
        kr_yds,
        pr_yds,
        kr_avg,
        pr_avg
    ):

        self.kick_returns = kick_returns
        self.year = year
        self.long_kr = long_kr
        self.punt_returns = punt_returns
        self.long_pr = long_pr
        self.games_played = games_played
        self.kr_tds = kr_tds
        self.pr_tds = pr_tds
        self.kr_yds = kr_yds
        self.pr_yds = pr_yds
        self.kr_avg = kr_avg
        self.pr_avg = pr_avg

class RushingStats:
    def __init__(
        self,
        rush_att,
        rush_yards,
        rush_tds,
        ya_contact,
        broke_tkls,
        fumbles,
        twenty_plus_yd_runs,
        rush_yp_carry,
        rush_yp_game,
        games_played
    ):
        self.rush_att = rush_att
        self.rush_yards = rush_yards
        self.rush_tds = rush_tds
        self.ya_contact = ya_contact
        self.broke_tkls = broke_tkls
        self.fumbles = fumbles
        self.twenty_plus_yd_runs = twenty_plus_yd_runs
        self.rush_yp_carry = rush_yp_carry
        self.rush_yp_game = rush_yp_game
        self.games_played = games_played



class PlayerDefensiveStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        defensive_stats: DefensiveStats
    ):
        self.player_details = player_details
        self.defensive_stats = defensive_stats


class PlayerKickingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        kicking_stats: KickingStats
    ):
        self.player_details = player_details
        self.kicking_stats = kicking_stats


class PlayerReceivingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        receiving_stats: ReceivingStats
    ):
        self.player_details = player_details
        self.receiving_stats = receiving_stats


class PlayerReturnStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        return_stats: ReturnStats
    ):
        self.player_details = player_details
        self.return_stats = return_stats    


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
