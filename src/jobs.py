from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as jobs_file:
        jobs_reader = csv.DictReader(jobs_file)
        jobs_list = []
        for jobs in jobs_reader:
            jobs_list.append(jobs)
        return jobs_list


# if __name__ == "__main__":
#     print(read("src/jobs.csv"))
