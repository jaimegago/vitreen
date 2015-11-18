from flask import render_template, flash, redirect, url_for
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
