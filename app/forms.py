from flask.ext.wtf import Form
from wtforms import TextField, Passwordfield
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('name', validators = [Required()])
    password = Passwordfield('password', validators = [Required()])
    
