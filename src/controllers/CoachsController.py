from src.services.CoachsService import CoachsService

class CoachsController():
    def __intit__(self):
        self.CoachsService = CoachsService()
    
    def get_coach_records(self):
        return self.CoachsService.get_coach_records()