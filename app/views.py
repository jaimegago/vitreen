from flask import render_template, flash, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from app import app
from .forms import CreateEventForm
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = CreateEventForm()
    if form.validate_on_submit():
      create_event_url = 'http://10.90.0.128/events/'
      event_payload = {'what': form.title.data,
          'tags': form.tags.data,
          'data': form.desc.data}
      post_request = requests.post('http://10.90.0.128/events/',
          data=json.dumps(event_payload))
      flash('Creating graphite event with tags="%s", title=%s description=%s' % (
          form.tags.data, form.title.data, form.desc.data))
      return redirect(url_for('index'))
    return render_template('create_event.html',form=form)

@app.route('/events')
def events():
    events_data = requests.get('http://10.90.0.128/events/get_data')
    events = events_data.json()
    return render_template('events_listing.html', events=events)


