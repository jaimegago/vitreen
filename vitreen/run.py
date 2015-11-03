#!/usr/bin/env python
# TODO
# Move this to a script dir and make it smarter
# see https://github.com/jaimegago/food_truck/blob/master/food_trucks/scripts/run_server.py
from app import app
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)
app.run(host='0.0.0.0', debug=True)
