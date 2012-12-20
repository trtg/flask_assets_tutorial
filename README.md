taken from here with some miscellaneous bug fixes:

http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/

you'll need the mincss and closure python packages to play with Flask-Assets 
pip install mincss 
pip install closure

Note you'll also need to install the less compiler (lessc) if you haven't already

-g flag below to install in a globally available path

sudo npm install less -g

or you could probably stick a symlink in your virtualenv's bin directory maybe(?)

To use Flask-Assets from the manage.py script:
./manage.py assets build

To run the included webserver using the development environment (which uses sqlite and asset debugging):
EXAMPLE_ENV='dev' ./manage.py runserver
