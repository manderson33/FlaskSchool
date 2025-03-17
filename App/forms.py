from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   submit = SubmitField('Submit')


class AddRectangle(FlaskForm):
    length = StringField('Length', validators=[DataRequired()])
    width = StringField('Width', validators=[DataRequired()])
    area = SubmitField('Calculate Area')
    perimeter = SubmitField('Calculate Perimeter')

