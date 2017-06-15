#! /bin/bash
rm -f tmp.db music/tmp.db db.sqlit3
rm -r music/propose/migrations
python3 music/manage.py makemigrations propose
python3 music/manage.py migrate
python3 music/manage.py runserver http://127.0.0.1:8000/
python3 test.py exp1 http://127.0.0.1:8000/ 
