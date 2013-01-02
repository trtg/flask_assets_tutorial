taken from here with some miscellaneous bug fixes:

http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/

The full list of packages I installed in the virtualenv used during this tutorial are as follows:

```
Flask==0.9
Flask-Assets==0.8
Flask-SQLAlchemy==0.16
Flask-Script==0.5.1
Jinja2==2.6
SQLAlchemy==0.8.0b2
Werkzeug==0.8.3
closure==20120305
cssmin==0.1.4
webassets==0.8
wsgiref==0.1.2
```

you'll need the cssmin and closure python packages if you want to play with Flask-Assets (these packages will not automatically be picked up as dependencies)

```
pip install Flask Flask-Assets SQLAlchemy Flask-SQLAlchemy Flask-Script
pip install cssmin
pip install closure
```


Note you'll also need to install the less compiler (lessc) if you haven't already

-g flag below will install in a globally available path

```
sudo npm install less -g
```

or you could probably stick a symlink in your virtualenv's bin directory maybe(?)

To use Flask-Assets from the manage.py script:

```
./manage.py assets build
```

To run the included webserver using the development environment (which uses sqlite and asset debugging):

```
EXAMPLE_ENV='dev' ./manage.py runserver
```
