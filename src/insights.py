from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    all_jobs = read(path)

    job_type = set()

    for jobs in all_jobs:
        job_type.add(jobs["job_type"])

    return list(job_type)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    all_jobs = read(path)

    industry = set()

    for jobs in all_jobs:
        if jobs["industry"] != "":
            industry.add(jobs["industry"])

    return list(industry)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    all_jobs = read(path)

    max_salary = set()

    for jobs in all_jobs:
        if jobs["max_salary"].isnumeric() is True:
            max_salary.add(jobs["max_salary"])

    super_salary = 0

    max_salary_value = [int(val) for val in max_salary]

    for salary in max_salary_value:
        if salary > super_salary:
            super_salary = salary

    return super_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_jobs = read(path)

    min_salary = set()

    for jobs in all_jobs:
        if jobs["min_salary"].isnumeric() is True:
            min_salary.add(jobs["min_salary"])

    min_salary_value = [int(val) for val in min_salary]

    below_salary = min_salary_value[0]

    for salary in min_salary_value:
        if salary < below_salary:
            below_salary = salary

    return below_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []


# if __name__ == "__main__":
#     print(len(get_unique_industries("src/jobs.csv")))
#     print(get_max_salary("src/jobs.csv"))
