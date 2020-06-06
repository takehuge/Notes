#!/bin/bash

cd "$(dirname "$0")"
echo Starting Flasksql...

export FLASK_APP=Flasksql
export FLASK_ENV=development

flask run --host=127.0.0.1 --port=5777
