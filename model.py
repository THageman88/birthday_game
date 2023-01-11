from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)

    username = db.Column(db.Text, 
                         nullable=False, 
                         unique=True)

    password = db.Column(db.Text, 
                         nullable=False)
   

    # start_register
    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)
    # end_register

    # start_authenticate
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False
    # end_authenticate    
    
class Question_results(db.Model):
    """questionnaire"""
    
    __tablename__ = "Question_results"
     
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement = True)
    
    question_1 = db.Column(db.Text, nullable=True)
    question_2 = db.Column(db.Text, nullable=True)
    question_3 = db.Column(db.Text, nullable=True)
    question_4 = db.Column(db.Text, nullable=True)
    question_5 = db.Column(db.Text, nullable=True)
    question_6 = db.Column(db.Text, nullable=True)
    question_7 = db.Column(db.Text, nullable=True)
    question_8 = db.Column(db.Text, nullable=True)
