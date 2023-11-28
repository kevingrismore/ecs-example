FROM prefecthq/prefect:2.14.6-python3.11
COPY . /opt/prefect/ecs-example/
RUN pip install -r requirements.txt
WORKDIR /opt/prefect/ecs-example/
