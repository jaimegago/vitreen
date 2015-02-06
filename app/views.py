from flask import render_template, flash, redirect
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
    event_payload = {'what': 'test from flask',
        'tags': form.tags.data,
        'data': 'flask rocks!'}
    post_request = requests.post('http://10.90.0.128/events/',
        data=json.dumps(event_payload))
    flash('Creating graphite event with tags="%s"' % (form.tags.data))
    return redirect('/index')
  return render_template('create_event.html',form=form)
