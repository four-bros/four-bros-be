
class CoachInfo:
    def __init__(
        self,
        id,
        first_name,
        last_name,
        team_id,
        team_name
    ):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.team_id = team_id
        self.team_name = team_name
    
    def __repr__(self):
        return f'User: {self.id}, Name: {self.first_name} {self.last_name}'


class CoachStats:
    def __init__(
        self,
        id,
        coach_id,
        year,
        wins,
        losses,
        national_title
    ):

        self.id = id
        self.coach_id = coach_id
        self.year = year
        self.wins = wins
        self.losses = losses
        self.national_title = national_title
    
    def __repr__(self):
        return f'ID: {self.id}, User: {self.coach_id}'


class CoachSeasonRecord:
    def __init__(
        self,
        team_id,
        team_name,
        year,
        wins,
        losses,
        national_title
    ):
        self.team_id = team_id
        self.team_name = team_name
        self.year = year
        self.wins = wins
        self.losses = losses
        self.national_title = national_title
