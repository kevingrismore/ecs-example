FROM prefecthq/prefect:2.14.0-python3.11
COPY . /opt/prefect/ecs-example/
WORKDIR /opt/prefect/ecs-example/
