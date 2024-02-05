from src.services.UsersService import UsersService

class UsersController():
    def __init__(self):
        self.UsersService = UsersService()
    
    def get_users_and_week(self):
        return self.UsersService.get_users_and_week()
