# fullstackpy

The Python Flask Template you wish you had

Setting up your virtualenv
Open up a new Bash console from your Dashboard and run

mkvirtualenv --python=/usr/bin/python3.6 my-virtualenv # use whichever python version you prefer
pip install flask
You'll see the prompt changes from a $ to saying (my-virtualenv)$ -- that's how you can tell your virtualenv is active. Whenever you want to work on your project in the console, you need to make sure the virtualenv is active. You can reactivate it at a later date with

$ workon my-virtualenv
(my-virtualenv)$
You can also install any other dependencies you may have at this point, like Sqlalchemy, using pip install flask-sqlalchemy, or pip install -r requirements.txt, if you have a requirements.txt
