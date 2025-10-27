SHELL := /bin/bash

all: install

install:
	@echo ">>> Installing dependencies"
	python3 -m venv .venv
	source .venv/bin/activate && \
			pip install -r pip-requirements.txt && \
			pip install -r dev-requirements.txt && \
			pip install -r requirements.txt && \
			pre-commit install && \
			deactivate

format:
	@echo ">>> Formatting files using isort and Black"
	python3 -m venv .venv
	source .venv/bin/activate && \
			isort . && \
			black .

lint:
	@echo ">>> Linting Python files"
	python3 -m venv .venv
	source .venv/bin/activate && \
			flake8 .

run_electro:
	@echo ">>> Running electro data analysis"
	python3 -m venv .venv
	source .venv/bin/activate && \
			jupyter notebook electro_data_analysis.ipynb && \
			deactivate

run_physics:
	@echo ">>> Running physics data analysis"
	python3 -m venv .venv
	source .venv/bin/activate && \
			jupyter notebook physics_data_analysis.ipynb && \
			deactivate
