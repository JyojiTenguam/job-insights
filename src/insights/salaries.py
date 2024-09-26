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
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError(
                "Missing min_salary or max_salary in job dictionary"
                )

        try:
            min_salary = int(job['min_salary'])
            max_salary = int(job['max_salary'])
            salary = int(salary)
        except (ValueError, TypeError):
            raise ValueError(
                "Non-numeric value found in min_salary, max_salary, or salary"
                )

        if min_salary > max_salary:
            raise ValueError(
                "min_salary is greater than max_salary"
                )

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        valid_jobs = []
        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    valid_jobs.append(job)
            except ValueError:
                continue
        return valid_jobs
