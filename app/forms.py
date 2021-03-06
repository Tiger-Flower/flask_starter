from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    firstname    = StringField('First Name', validators=[DataRequired()])
    lastname     = StringField('Last Name', validators=[DataRequired()])
    email        = StringField('Email', validators=[DataRequired(), Email()])
    subject      = StringField('Subject', validators=[DataRequired()])
    text         = TextAreaField('Text', validators=[DataRequired()])
