from flask import Flask
import json
import sys

app = Flask(__name__)
VITREEN_VERSION = '0.0.1'
# TODO
# Look for config files in multiple places
# Handle prod vs dev config

VITREEN_CONF_FILE = './vitreen-config.json'
try:
  with open(VITREEN_CONF_FILE, 'r') as f:
    json_config = json.load(f)
except Exception as e:
  print 'Could not load config file: %s' % VITREEN_CONF_FILE
  print e
  sys.exit(1)

for key in json_config:
  if key.isupper() != True:
    print 'all config keys in %s must be UPPERCASE!' % VITREEN_CONF_FILE
    print '%s is not all UPPERCASE!' % key
    sys.exit(1)

app.config.update(json_config)
app.config['VITREEN_VERSION'] = VITREEN_VERSION

from app import views
