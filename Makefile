.PHONY: init start

init:
	@pip install -r requirements.txt

start:
	@python3 main.py