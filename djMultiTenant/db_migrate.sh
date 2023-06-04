#!/bin/bash

cd ../

python manage.py makemigrations 
wait

python manage.py migrate &
python manage.py migrate --database=authors &
python manage.py migrate --database=books &

jobs -l

wait

jobs -l