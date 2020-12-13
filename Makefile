.DEFAULT: help

PYTHON = python3
PIP = pip3
UNAME_S := $(shell uname -s) 
ifeq ($(UNAME_S), Darwin) 
MAC_INSTALL = brew install ffmpeg gpg git-secret
endif
ifeq ($(UNAME_S), Linux) 
LINUX_UPDATE = sudo apt-get update
LINUX_INSTALL = sudo apt install python-pip ffmpeg gpg git-secret
endif


help:
	@echo "uso: make [build | run | help]"
	@echo "build: Installs all external tools to run the application"
	@echo "run: execute de application"

build:
	@echo "Build started"
	$(MAC_INSTALL)
	$(LINUX_UPDATE)
	$(LINUX_INSTALL)
	$(PIP) install --upgrade pip
	$(PIP) install --requirement requirements.txt

	@echo "\n\nAll external tools has been installed!"
	@echo "\nRequest permission to decrypt files in /secrets pathi\n"

run:
	${PYTHON} main.py
