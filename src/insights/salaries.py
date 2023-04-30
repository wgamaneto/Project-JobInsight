from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    salaries = [
        int(salary["max_salary"])
        for salary in data
        if salary["max_salary"].isnumeric()
    ]
    return max(salaries)


def get_min_salary(path: str) -> int:
    data = read(path)
    salaries = [
        int(salary["min_salary"])
        for salary in data
        if salary["min_salary"].isnumeric()
    ]
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (KeyError, TypeError, ValueError):
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    else:
        return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    jobs_filtered = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)

        except ValueError:
            pass

    return jobs_filtered
