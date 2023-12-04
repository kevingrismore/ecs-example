from prefect import flow
import time


@flow(log_prints=True)
def hello():
    for i in range(65):
        time.sleep(60)
        print(f"Running for {i + 1} minute(s)")


if __name__ == "__main__":
    hello()
