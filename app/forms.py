from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired,Email

class ContactForm(FlaskForm):
    name=StringField('Name', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(),Email()])
    subject=StringField('Subject', validators=[DataRequired()])
    message=StringField('Message', validators=[DataRequired()])