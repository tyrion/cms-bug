#|/usr/bin/env bash
rm db.sqlite
python manage.py syncdb --all --noinput
python manage.py migrate --fake
