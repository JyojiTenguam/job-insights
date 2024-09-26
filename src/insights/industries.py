from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        jobs_list = self.jobs_list
        industries = [job['industry'] for job in jobs_list if job['industry']]
        unique_industries = list(set(industries))
        return unique_industries
