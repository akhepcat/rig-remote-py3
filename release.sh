#!/bin/bash

echo "This script will perform the unit tests, check the code with flake8 and build the egg. It will ask for confirmation before starting the upload."

python -m pytest -s --cov-report term-missing --cov ./rig_remote
python setup.py flake8

python setup.py develop  && python setup.py sdist && python setup.py bdist_egg 
echo "egg generated. Press enter if you are ready to upload?"

read a

python setup.py sdist upload


echo "Upload should be completed, please review it at https://pypi.python.org/pypi/rig-remote"
