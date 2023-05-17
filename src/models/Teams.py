from typing import List
from src.models.Player import PlayerDetails


class TeamDetails:
    def __init__(
        self,
        id,
        team_name,
        team_short_name,
        is_user,
        avg_overall,
        avg_offense,
        avg_defense,
        avg_sp_teams,
        coachs_poll_1st_votes,
        nickname,
        wins,
        bcs_rank,
        coachs_poll_rank,
        media_poll_rank,
        losses,
        media_poll_points,
        coachs_poll_points
    ):
        self.id = id
        self.team_name = team_name
        self.team_short_name = team_short_name
        self.is_user = is_user
        self.avg_overall = avg_overall
        self.avg_offense = avg_offense
        self.avg_defense = avg_defense
        self.avg_sp_teams = avg_sp_teams
        self.coachs_poll_1st_votes = coachs_poll_1st_votes
        self.nickname = nickname
        self.wins = wins
        self.bcs_rank = bcs_rank
        self.coachs_poll_rank = coachs_poll_rank
        self.media_poll_rank = media_poll_rank
        self.losses = losses
        self.media_poll_points = media_poll_points
        self.coachs_poll_points = coachs_poll_points


class TeamInfo:
    def __init__(
        self,
        id,
        team_name,
        nickname,
        is_user,
    ):
        self.id = id
        self.team_name = team_name
        self.nickname = nickname
        self.is_user = is_user


# Should be able to refactor this in some way
class TeamRoster(PlayerDetails):
    def __init__(
        self,
        id,
        first_name,
        last_name,
        height,
        weight,
        jersey_number,
        player_year,
        redshirt,
        position,
        hometown_desc,
        overall
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.jersey_number = jersey_number
        self.player_year = player_year
        self.redshirt = redshirt
        self.position = position
        self.hometown_desc = hometown_desc
        self.overall = overall


class TeamGameStats:
    def __init__(
        self,
        team_id,
        week,
        year,
        total_points,
        completions,
        pass_att,
        comp_pct,
        pass_yds,
        pass_ypa,
        pass_tds,
        ints,
        sacked,
        rush_att,
        rush_yds,
        rush_ypc,
        rush_tds,
        fumbles,
        receptions,
        rec_yds,
        rec_ypc,
        rec_tds,
        drops,
        off_yards,
        total_yards,
        off_turnovers,
        sacks,
        tfl,
        ints_made,
        ff,
        fr,
        def_turnovers,
        to_margin,
        pass_def,
        blocked_kicks,
        safeties,
        def_tds,
        kr_yds,
        kr_tds,
        pr_yds,
        pr_tds,
    ):
        self.team_id = team_id
        self.week = week
        self.year = year
        self.total_points = total_points
        self.completions = completions
        self.pass_att = pass_att
        self.comp_pct = comp_pct
        self.pass_yds = pass_yds
        self.pass_ypa = pass_ypa
        self.pass_tds = pass_tds
        self.ints = ints
        self.sacked = sacked
        self.rush_att = rush_att
        self.rush_yds = rush_yds
        self.rush_ypc = rush_ypc
        self.rush_tds = rush_tds
        self.fumbles = fumbles
        self.receptions = receptions
        self.rec_yds = rec_yds
        self.rec_ypc = rec_ypc
        self.rec_tds = rec_tds
        self.drops = drops
        self.off_yards = off_yards
        self.total_yards = total_yards
        self.off_turnovers = off_turnovers
        self.sacks = sacks
        self.tfl = tfl
        self.ints_made = ints_made
        self.ff = ff
        self.fr = fr
        self.def_turnovers = def_turnovers
        self.to_margin = to_margin
        self.pass_def = pass_def
        self.blocked_kicks = blocked_kicks
        self.safeties = safeties
        self.def_tds = def_tds
        self.kr_yds = kr_yds
        self.kr_tds = kr_tds
        self.pr_yds = pr_yds
        self.pr_tds = pr_tds


class TeamSeasonStats:
    def __init__(
        self,
        team_id,
        year,
        games_played,
        total_points,
        ppg,
        pass_yds,
        pass_ypg,
        pass_tds,
        ints,
        sacked,
        rush_yds,
        rush_ypg,
        rush_tds,
        fumbles,
        rec_yds,
        rec_ypg,
        rec_tds,
        drops,
        off_yards,
        off_ypg,
        total_yards,
        total_ypg,
        off_turnovers,
        sacks,
        tfl,
        ints_made,
        ff,
        fr,
        def_turnovers,
        pass_def,
        safeties,
        blocked_kicks,
        def_tds,
        to_margin,
        kr_yds,
        kr_tds,
        pr_yds,
        pr_tds,
    ):
        self.team_id = team_id
        self.year = year
        self.games_played = games_played
        self.total_points = total_points
        self.ppg = ppg
        self.pass_yds = pass_yds
        self.pass_ypg = pass_ypg
        self.pass_tds = pass_tds
        self.ints = ints
        self.sacked = sacked
        self.rush_yds = rush_yds
        self.rush_ypg = rush_ypg
        self.rush_tds = rush_tds
        self.fumbles = fumbles
        self.rec_yds = rec_yds
        self.rec_ypg = rec_ypg
        self.rec_tds = rec_tds
        self.drops = drops
        self.off_yards = off_yards
        self.off_ypg = off_ypg
        self.total_yards = total_yards
        self.total_ypg = total_ypg
        self.off_turnovers = off_turnovers
        self.sacks = sacks
        self.tfl = tfl
        self.ints = ints_made
        self.ints_made = ints_made
        self.ff = ff
        self.fr = fr
        self.def_turnovers = def_turnovers
        self.pass_def = pass_def
        self.safeties = safeties
        self.blocked_kicks = blocked_kicks
        self.def_tds = def_tds
        self.to_margin = to_margin
        self.kr_yds = kr_yds
        self.kr_tds = kr_tds
        self.pr_yds = pr_yds
        self.pr_tds = pr_tds


class TeamGameRecord:
    def __init__(
        self,
        team_info: TeamInfo,
        team_stats: TeamGameStats
    ):
        self.team_info = team_info
        self.team_stats = team_stats


class TeamSeasonRecord:
    def __init__(
        self,
        team_info: TeamInfo,
        team_stats: TeamSeasonStats
    ):
        self.team_info = team_info
        self.team_stats = team_stats


class TeamSummary:
    def __init__(
        self,
        team_details: TeamDetails,
        team_roster: List[TeamRoster],
        team_stats: TeamSeasonStats
    ):
        self.team_details = team_details
        self.team_roster = team_roster
        self.team_stats = team_stats

class TeamDetailsSummary:
    def __init__(
        self,
        team_details: TeamDetails
    ):
        self.team_details = team_details

class TeamRosterSummary:
    def __init__(
        self,
        team_roster: List[TeamRoster]
    ):
        self.team_roster = team_roster
    
class TeamStatsSummary:
    def __init__(
        self,
        team_stats: TeamSeasonStats
    ):
        self.team_stats = team_stats
