import asyncio
from typing import List
from sqlalchemy import desc
from uuid import uuid4
import time

from src.constants import session
from src.utils.helpers import(
    _convert_stats_year
)
from src.data_models.CommitsData import CommitsData
from src.data_models.WeekYearData import WeekYearData


async def insert_commits_into_db(week_year_data, commits):

    start_time = time.time()
    print('Starting Commits insert.')

    current_week: int = week_year_data[0].fields['Week']
    current_year: int = _convert_stats_year(week_year_data[0].fields['Year'])

    new_commits: List[CommitsData] = []
    
    for i, value in enumerate(commits):
        record = commits[i]

        new_commit = CommitsData(
            stars=record.fields['Stars'],
            name=record.fields['Name'],
            position=record.fields['Position'],
            rank=record.fields['Rank'],
            school=record.fields['School'],
            week=current_week,
            year=current_year
        )

        commit_query = session.query(CommitsData).where(
            CommitsData.name == new_commit.name).scalar()
        
        if commit_query is None:
            new_commits.append(new_commit)
            
    try:
        session.add_all(new_commits)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Commits took {(round(execution_time, 2))} seconds to complete.')


async def insert_week_year_into_db(week_year):

    start_time = time.time()
    print('Starting Week/Year insert.')
    
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

    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        execution_time = time.time() - start_time
        print(f'Insert Week/Year script took {(round(execution_time, 2))} seconds to complete.')
