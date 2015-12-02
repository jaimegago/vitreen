from flask import render_template, flash, redirect, url_for, jsonify
from flask.ext.bootstrap import Bootstrap
from app import app
from .forms import CreateEventForm
import requests
import json
import urlparse
import time

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
  form = CreateEventForm()
  if form.validate_on_submit():
    event_payload = {
        'what': form.title.data,
        'when': time.mktime(form.when.data.timetuple()),
        'tags': form.tags.data,
        'data': form.desc.data
      }
    post_request = requests.post(
        urlparse.urljoin(app.config['GRAPHITE_SERVER_URL'], 'events/'),
        data=json.dumps(event_payload)
      )
    flash('Creating graphite event with tags="%s", title=%s description=%s' % (
      form.tags.data, form.title.data, form.desc.data))
    return redirect(url_for('index'))
  return render_template('create_event.html',form=form)

@app.route('/events')
def events():
  events_data = requests.get(urlparse.urljoin(app.config['GRAPHITE_SERVER_URL'],
    'events/get_data'))
  events = events_data.json()
  return render_template('events_listing.html', events=events)

@app.route('/status')
def status():
  status = {}
  status['vitreen_version'] = app.config['VITREEN_VERSION']
  status['graphite_events_endpoint'] = app.config['GRAPHITE_SERVER_URL']
  now = int(time.time())
  graphite_events_api_response = requests.get(urlparse.urljoin
      (app.config['GRAPHITE_SERVER_URL'],'events/?from=' + str(now)))
  if graphite_events_api_response.status_code == 200:
    status['graphite_events_api_available'] = True
  else:
    status['graphite_events_api_available'] = False
  return jsonify(status)
    

