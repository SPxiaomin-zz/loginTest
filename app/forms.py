from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('name', validators = [Required()])
    password = PasswordField('password', validators = [Required()])

class RegistrationForm(Form):
    name = StringField('rname', validators = [Required()])
    password = PasswordField('rpassword', validators = [Required()])
    submit = SubmitField('Register')
