import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        results = csv.DictReader(file)
        data = [result for result in results]
        return data


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    type_jobs = []
    for job in data:
        if job["job_type"] not in type_jobs:
            type_jobs.append(job["job_type"])
    return sorted(type_jobs)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_type = [job for job in jobs if job["job_type"] == job_type]

    return jobs_type
