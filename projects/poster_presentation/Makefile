SHELL := /bin/bash

all: install

install:
	@echo ">>> Installing dependencies"
	python3 -m venv .venv
	source .venv/bin/activate && \
			pip install -r requirements.txt && \
			deactivate

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
