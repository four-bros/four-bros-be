from flask import Blueprint

from src.controllers.CoachsController import CoachsController

coach_bp = Blueprint('coach', __name__)
CoachsController = CoachsController()

@coach_bp.route('', methods=['GET'])
def coach_get_records():
    return CoachsController.get_coach_records()
