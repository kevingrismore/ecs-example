from prefect import flow

@flow(log_prints=True)
def hello():
    print("Hello Prefect!")

if __name__=="__main__":
    hello()