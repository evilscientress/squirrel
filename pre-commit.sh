#!/usr/bin/env bash

set -eu

if [ ! -d venv ]; then
   python3.6 -m virtualenv venv
fi

source venv/bin/activate

pip install -r requirements.txt 1>/dev/null
pip install -r requirements-dev.txt 1>/dev/null

# Commitlint
npm install @commitlint/cli@8.2.0 @commitlint/config-conventional@8.2.0

# Lint last commit from history
./node_modules/.bin/commitlint .

# Run linting
flake8 squirrel/

# Run python tests
cd squirrel
python manage.py test 1>/dev/null