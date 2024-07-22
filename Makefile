# Variables
PYTHON=python
DOCKER_COMPOSE=docker-compose
IMAGES=distributed-systems-project-server

# Targets
build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up --scale server1=1 --scale server2=1 --scale server3=1 --scale server4=1 --scale server5=1 --scale server6=1 -d

down:
	$(DOCKER_COMPOSE) down

run-async:
	$(PYTHON) async_requests.py

logs:
	$(DOCKER_COMPOSE) logs -f

clean:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

.PHONY: build up down run-async logs clean
