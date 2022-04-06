from flask import Blueprint, request

from src.blueprints.view_methods.coach import (
    get_coach_records
)

coach_bp = Blueprint('coach', __name__)


@coach_bp.route('', methods=['GET'])
def coach_get_records():
    return get_coach_records(request)
