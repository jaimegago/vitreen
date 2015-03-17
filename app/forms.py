from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateEventForm(Form):
  tags  = StringField('Tags', validators=[DataRequired()])
  title = StringField('Title', validators=[DataRequired()])
  desc  = StringField('Description', validators=[DataRequired()])
  submit = SubmitField('Submit')
