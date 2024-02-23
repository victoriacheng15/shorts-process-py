.PHONY: init start format

init:
	@pip install -r requirements.txt

start:
	@python3 main.py

format:
	@black main.py utils settings.py