#!/bin/bash
set -e

while ! (timeout 3 bash -c "</dev/tcp/${POSTGRES_HOST}/${POSTGRES_PORT}") &> /dev/null;
do
  echo waiting for PostgreSQL to start...;
  sleep 3;
done;

./manage.py migrate  --no-input --traceback
./manage.py collectstatic --no-input --traceback
./manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.filter(username='materialadmin').exists() or \
                           User.objects.create_superuser('materialadmin',
                          'materialadmin@example.com', 'password123')"
./manage.py runserver 0.0.0.0:8000
