from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import SubmitField
from bcrypt import hashpw, checkpw, gensalt

class loginForm(FlaskForm):
    username = StringField(label='Username')
    password = PasswordField(label='Password')
    login = SubmitField('Login')
