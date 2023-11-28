from prefect import flow
from prefect.deployments.runner import DeploymentImage
from git import Repo


@flow(log_prints=True)
def hello():
    print("Hello Prefect!")


if __name__ == "__main__":
    repo = Repo()
    commit_hash = repo.git.rev_parse("HEAD")

    hello.deploy(
        name="ecs-hello-example",
        work_pool_name="my-ecs-pool",
        image=DeploymentImage(
            name="455346737763.dkr.ecr.us-east-2.amazonaws.com/kevin-test-repo",
            tag=commit_hash,
            dockerfile="Dockerfile",
            platform="linux/amd64",
        ),
    )
