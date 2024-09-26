from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        jobs_list = self.jobs_list
        salaries = [
            int(job['max_salary']) for job in jobs_list
            if job['max_salary'] and job['max_salary'].isdigit()
            ]
        return max(salaries)

    def get_min_salary(self) -> int:
        jobs_list = self.jobs_list
        salaries = [
            int(job['min_salary']) for job in jobs_list
            if job['min_salary'] and job['min_salary'].isdigit()
            ]
        return min(salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
