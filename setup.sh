#!/bin/bash

# Install PipEnv
python3 -m pip install --user pipenv
# Install Dependencies
python3 -m pipenv install
# Sync Dev Dependencies
python3 -m pipenv sync -d 
# Enter Shell
python3 -m pipenv shell 
