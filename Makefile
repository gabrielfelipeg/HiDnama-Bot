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


	@echo "All external tools has been installed!" 

run:
	${PYTHON} main.py