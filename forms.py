from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , DateField
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    """Form for registering a user."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class LoginForm(FlaskForm):
    """Form for registering a user."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
     

class bdayForm(FlaskForm):
    """Bday Questions Form"""
    
    question_1 = StringField("What was your favorite food?")
    question_2 = StringField("Where was your favorite place that you visited?")
    question_3 = StringField("One thing in nature that humbled you?")
    question_4 = StringField("A new skill you attained?")
    question_5 = StringField("Something that you were proud of?")
    question_6 = StringField("A goal you worked hard to achieve?")
    question_7 = StringField("An animal friend that really stood out?")
    question_8 = StringField("New friend you made?")
    
    
    

    

