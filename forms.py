from flask_wtf import FlaskForm
from wtforms import StringField , EmailField , DateField

class register_new_user(FlaskForm):
    """Register User Form"""
    
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = EmailField("Email")
    birthday = DateField("Birthday")
    