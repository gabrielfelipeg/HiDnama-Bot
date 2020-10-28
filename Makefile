.DEFAULT: help

PYTHON = python3
PIP = pip

help:
	@echo "uso: make [build | run | help]"
	@echo "build: Installs all external tools to run the application"
	@echo "run: execute de application"

build:
	@echo "Build started"

	sudo apt-get update
	sudo apt install python-pip

	$(PIP) install --upgrade pip
	$(PIP) install --requirement requirements.txt


	@echo "\n\nAll external tools has been installed!" 
	@echo "Now, Create the follow files:\n"
	@echo "credentials.json: with credentials to use google drive api"
	@echo "token.key: with the token of discord bot"
	@echo "After Create the files, execute: make run\n"

run:
	${PYTHON} main.py