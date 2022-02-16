

class Team:
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
