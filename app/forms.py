from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateEventForm(Form):
    tags = StringField('tags', validators=[DataRequired()])
