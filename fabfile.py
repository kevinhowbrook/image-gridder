from invoke import run as local
from invoke.tasks import task


@task
def run_tests(c):
    return local(
        "poetry run coverage run -m pytest && " "poetry run coverage report -m"
    )
