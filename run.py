#!/usr/bin/env python
# TODO
# Move this to a script dir and make it smarter
# see https://github.com/jaimegago/food_truck/blob/master/food_trucks/scripts/run_server.py
from app import app
from flask.ext.bootstrap import Bootstrap

import sys
if len(sys.argv) > 1 and sys.argv[1] == 'version':
  print '%s' % app.config['VITREEN_VERSION']
  sys.exit(0)

bootstrap = Bootstrap(app)
app.run(host='0.0.0.0', debug=True)
