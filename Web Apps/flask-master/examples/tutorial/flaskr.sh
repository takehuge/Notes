#!/bin/bash

cd "$(dirname "$0")"
echo Starting Flaskr...

export FLASK_APP=flaskr
export FLASK_ENV=development
flask init-db
flask run --host=127.0.0.1 --port=5777
