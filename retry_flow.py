from prefect import flow, task


@flow
def testing_retries():
    successful_task()
    failing_task()


@task
def successful_task():
    print("good")


@task
def failing_task():
    raise Exception("bad")


if __name__ == "__main__":
    testing_retries()
