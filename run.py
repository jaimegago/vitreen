#!/usr/bin/python -tt
from app import app
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)
app.run(host='0.0.0.0', debug=True)
