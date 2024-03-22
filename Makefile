SHELL = /bin/bash
create-venv:
	( \
	python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip install -r requirements.txt; \
	)

download:
	( \
	source .venv/bin/activate; \
	python nyc_taxi_download.py \
	)
delete_existing:
	rm -rf nyc_taxi_data/;
activate:
	source .venv/bin/activate;
