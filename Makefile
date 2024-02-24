.PHONY: init format opening video clean

init:
	@pip install -r requirements.txt

format:
	@black main.py utils settings.py

opening:
	@python3 main.py opening

video:
	@python3 main.py video

clean:
	@python3 main.py clean