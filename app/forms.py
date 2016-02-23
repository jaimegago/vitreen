from flask.ext.wtf import Form
from wtforms import TextField, StringField, SubmitField
from wtforms.fields.html5 import DateTimeField
from wtforms.validators import DataRequired
from wtforms_components import DateRange
from datetime import datetime

class CreateEventForm(Form):
  tags  = StringField('Tags', validators=[DataRequired()])
  event_title = StringField('Title', validators=[DataRequired()])
  desc  = StringField('Description', validators=[DataRequired()])
  when  = DateTimeField('When', default=datetime.now(), validators=[
    DataRequired(), DateRange(
          min=datetime(2000, 1, 1),
          max=datetime.now()
        )
      ])
  submit = SubmitField('submit')
