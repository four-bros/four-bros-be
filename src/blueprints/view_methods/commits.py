from src.controllers.CommitsController import CommitsController

def get_all_commits(request):
    return 
    # week_year: WeekYearData = session.query(WeekYearData).order_by(
    #     desc(WeekYearData.year),
    #     desc(WeekYearData.week)
    # ).first()

    # commits_data: List[CommitsData] = session.query(CommitsData).where(
    #     CommitsData.year == week_year.year
    # ).order_by(
    #     CommitsData.school,
    #     CommitsData.rank
    # ).all()

    # response = {}

    # for team in user_team_names:
    #     key = team.replace(' ', '_').lower()
    #     response[key] = commits_schema.dump(
    #         [commit for commit in commits_data if commit.school == team])

    # return response
