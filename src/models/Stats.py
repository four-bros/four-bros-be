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


#################################################
########### Individual Stats models #############
#################################################
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
        total_tkls,
        total_sacks
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
        self.total_sacks = total_sacks


    def __repr__(self):
        return f'Total Tackles: {self.total_tkls}'


################################################
########### Offensive Stats models #############
################################################
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
        pass_ypa,
        pass_ypg,
        pass_rating,
        sacked,
        comp_pct
    ):      
        self.pass_yards = pass_yards
        self.longest_pass = longest_pass
        self.year = year
        self.pass_tds = pass_tds
        self.games_played = games_played
        self.completions = completions
        self.ints = ints
        self.pass_att = pass_att
        self.pass_ypa = pass_ypa
        self.pass_ypg = pass_ypg
        self.pass_rating = pass_rating
        self.sacked = sacked
        self.comp_pct = comp_pct

    def __repr__(self):
        return f'Total Pass Yards: {self.pass_yards}'


class ReceivingStats:
    def __init__(
        self,
        receptions,
        rec_yards,
        rec_tds,
        yac,
        drops,
        rec_ypc,
        rec_ypg,
        games_played,
        year,
        longest_rec

    ):
        self.receptions = receptions
        self.rec_yards = rec_yards
        self.rec_tds = rec_tds
        self.yac = yac
        self.drops = drops
        self.rec_ypc = rec_ypc
        self.rec_ypg = rec_ypg
        self.games_played = games_played
        self.year = year
        self.longest_rec = longest_rec

    def __repr__(self):
        return f'Total Rec. Yards: {self.rec_yards}'


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
        rush_ypc,
        rush_ypg,
        games_played,
        year,
        longest_run
    ):
        self.rush_att = rush_att
        self.rush_yards = rush_yards
        self.rush_tds = rush_tds
        self.ya_contact = ya_contact
        self.broke_tkls = broke_tkls
        self.fumbles = fumbles
        self.twenty_plus_yd_runs = twenty_plus_yd_runs
        self.rush_ypc = rush_ypc
        self.rush_ypg = rush_ypg
        self.games_played = games_played
        self.year = year
        self.longest_run = longest_run

    def __repr__(self):
        return f'Total Rush Yards: {self.rush_yards}'


####################################################
########### Special Teams Stats models #############
####################################################
class KickingAndPuntingStats:
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
        fg_pct,
        xp_pct,
        fg_50_plus_pct,
        punt_avg,
        net_avg
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
        self.fg_pct = fg_pct
        self.xp_pct = xp_pct
        self.fg_50_plus_pct = fg_50_plus_pct
        self.punt_avg = punt_avg
        self.net_avg = net_avg

    def __repr__(self):
        return f'Total FGs: {self.fg_made}, Total Punts: {self.number_punts}'


class KickingStats:
    def __init__(
        self,
        fg_made_17_29,
        fg_att_17_29,
        long_fg,
        ko_touchbacks,
        xp_att,
        year,
        fg_att,
        xp_blocked,
        fg_blocked,
        fg_att_40_49,
        fg_made_40_49,
        fg_att_30_39,
        fg_made_30_39,
        fg_att_50_plus,
        fg_made_50_plus,
        games_played,
        kickoffs,
        xp_made,
        fg_made,
        fg_pct,
        xp_pct,
        fg_50_plus_pct
    ):
        self.fg_made_17_29 = fg_made_17_29
        self.fg_att_17_29 = fg_att_17_29
        self.long_fg = long_fg
        self.ko_touchbacks = ko_touchbacks
        self.xp_att = xp_att
        self.year = year
        self.fg_att = fg_att
        self.xp_blocked = xp_blocked
        self.fg_blocked = fg_blocked
        self.fg_att_40_49 = fg_att_40_49
        self.fg_made_40_49 = fg_made_40_49
        self.fg_att_30_39 = fg_att_30_39
        self.fg_made_30_39 = fg_made_30_39
        self.fg_att_50_plus = fg_att_50_plus
        self.fg_made_50_plus = fg_made_50_plus
        self.games_played = games_played
        self.kickoffs = kickoffs
        self.xp_made = xp_made
        self.fg_made = fg_made
        self.fg_pct = fg_pct
        self.xp_pct = xp_pct
        self.fg_50_plus_pct = fg_50_plus_pct

    def __repr__(self):
        return f'Total FGs: {self.fg_made}, Total Punts: {self.number_punts}'


class KickReturnStats:
    def __init__(
        self,
        kick_returns,
        year,
        long_kr,
        games_played,
        kr_tds,
        kr_yds,
        kr_avg
    ):

        self.kick_returns = kick_returns
        self.year = year
        self.long_kr = long_kr
        self.games_played = games_played
        self.kr_tds = kr_tds
        self.kr_yds = kr_yds
        self.kr_avg = kr_avg

    def __repr__(self):
        return f'Total KR TDs and YDs: {self.kr_tds + self.kr_yds}'


class PuntingStats:
    def __init__(
        self,
        number_punts,
        total_punt_yards,
        punt_avg,
        net_punting,
        long_punt,
        year,
        games_played,
        punts_blocked,
        inside_twenty,
        punt_touchbacks,
        net_avg
        
    ):
        self.number_punts = number_punts
        self.total_punt_yards = total_punt_yards
        self.punt_avg = punt_avg
        self.net_punting = net_punting
        self.long_punt = long_punt
        self.year = year
        self.games_played = games_played
        self.punts_blocked = punts_blocked
        self.inside_twenty = inside_twenty
        self.punt_touchbacks = punt_touchbacks
        self.net_avg = net_avg
        

    def __repr__(self):
        return f'Punt AVG: {self.punt_avg}, Total Punts: {self.number_punts}'


class PuntReturnStats:
    def __init__(
        self,
        year,
        punt_returns,
        long_pr,
        games_played,
        pr_tds,
        pr_yds,
        pr_avg
    ):

        self.year = year
        self.punt_returns = punt_returns
        self.long_pr = long_pr
        self.games_played = games_played
        self.pr_tds = pr_tds
        self.pr_yds = pr_yds
        self.pr_avg = pr_avg

    def __repr__(self):
        return f'Total PR TDs and YDs: {self.pr_tds + self.pr_tds}'


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

    def __repr__(self):
        return f'Total Ret. TDS: {self.kr_tds + self.pr_tds}'


############################################
########## Total Stats models #############
############################################
class TotalStats:
    def __init__(
        self,
        total_yards,
        total_tds,
        total_ypg,
        games_played,
        year,
        turnovers
    ):
        self.total_yards = total_yards
        self.total_tds = total_tds
        self.total_ypg = total_ypg
        self.games_played = games_played
        self.year = year
        self.turnovers = turnovers


############################################
########## Player Stats models #############
############################################
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


class PlayerKickReturnStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        kick_return_stats: KickReturnStats
    ):
        self.player_details = player_details
        self.kick_return_stats = kick_return_stats   


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


class PlayerPuntingStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        punting_stats: PuntingStats
    ):
        self.player_details = player_details
        self.punting_stats = punting_stats


class PlayerPuntReturnStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        punt_return_stats: PuntReturnStats
    ):
        self.player_details = player_details
        self.punt_return_stats = punt_return_stats  


class PlayerTotalStats:
    def __init__(
        self,
        player_details: PlayerDetails,
        total_stats: TotalStats
    ):
        self.player_details = player_details
        self.total_stats = total_stats
