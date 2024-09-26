from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file_path: str) -> List[Dict]:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.jobs_list = list(reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = {
            job['job_type'] for job in self.jobs_list
            if 'job_type' in job and job['job_type']
        }
        return list(job_types)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
