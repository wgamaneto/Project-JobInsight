from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries = []
    for industry in data:
        if industry["industry"] not in industries:
            if industry["industry"] != "":
                industries.append(industry["industry"])

    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    jobs = [job for job in jobs if job["industry"] == industry]

    return jobs
