from prefect import flow, task


@flow(retries=1)
def testing_retries():
    successful_task()
    failing_task()


@task
def successful_task():
    return True


@task
def failing_task():
    raise Exception("bad")


if __name__ == "__main__":
    testing_retries()
