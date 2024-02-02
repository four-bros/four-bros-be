from src.services.CommitsService import CommitsService

class CommitsController():
    def __init__(self):
        self.CommitsService = CommitsService()
    
    def get_all_commits(self):
        return self.CommitsService.get_all_commits()
