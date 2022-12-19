from email import message
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64, min=4)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=50)])
    submit = SubmitField('Save')