NAME ?= teste

venv:
	virtualenv -p /usr/bin/python3.10 .venv

init:
	pip install -r infra/libs/requirements.txt

run:
	python3 "src/app.py"

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +

container:
	docker compose -f infra/dockerfiles/docker-compose.yaml -p a up --build

gen:
	python3 scripts/gen_module.py ${NAME}

runcontainer:
	docker run api-clsa-docker

.PHONY: tests
tests:
	PYTHONPATH=src pytest -v