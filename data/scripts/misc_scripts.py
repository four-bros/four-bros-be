from sqlalchemy import desc
from uuid import uuid4

from src.constants import session
from src.utils.helpers import(
    _convert_stats_year
)
from src.data_models.CommitsData import CommitsData
from src.data_models.WeekYearData import WeekYearData


def insert_commits_into_db(commits):

    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()
    
    for i, value in enumerate(commits):
        record = commits[i]
        
        new_commit = CommitsData(
            stars=record.fields['Stars'],
            name=record.fields['Name'],
            position=record.fields['Position'],
            rank=record.fields['Rank'],
            school=record.fields['School'],
            week=week_year.week,
            year=week_year.year
        )

        commit_query = session.query(CommitsData).where(
            CommitsData.name == new_commit.name).scalar()
        
        if commit_query is None:
            session.add(new_commit)
            
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_week_year_into_db(week_year):
    
    record = week_year[0]
    
    readable_year = _convert_stats_year(record.fields['Year'])

    new_id = str(uuid4())
    
    new_week_year = WeekYearData(
        id=new_id,
        week=record.fields['Week'],
        year=readable_year
    )

    week_year_query: WeekYearData = session.query(WeekYearData).filter(
        WeekYearData.week == new_week_year.week,
        WeekYearData.year == new_week_year.year
    ).scalar()
    
    if not week_year_query:
        session.add(new_week_year)
        session.flush()
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
