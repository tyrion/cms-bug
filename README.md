cms-bug
=======

virtualenv env
. env/bin/activate
pip install -r requirements.txt
export SECRET_KEY=lolololol
./manage.py syncdb --all
./manage.py migrate --fake
./manage.py runserver

goto /en/admin and add a new page
then try to add the video plugin to the placeholder
