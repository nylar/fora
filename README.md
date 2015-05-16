# Shrtn

[![Build Status](https://travis-ci.org/nylar/fora.svg?branch=master)](https://travis-ci.org/nylar/fora)
[![Coverage Status](https://coveralls.io/repos/nylar/fora/badge.svg?branch=master)](https://coveralls.io/r/nylar/fora?branch=master)
[![License](https://img.shields.io/badge/license-CC0-blue.svg)](LICENSE)

A Django forum.

## Installation

Grab the code.
```shell
git clone git@github.com:nylar/fora.git
cd fora
```

Install the requirements.
```shell
pip install -r requirements.txt
```

Setup the database.
```shell
python manage.py syncdb --noinput
python manage.py migrate --noinput
```

To run the local server
```shell
python manage.py runserver
```

To run the tests (with code coverage).
```shell
py.test --cov forums --cov threads --cov-report term-missing
```