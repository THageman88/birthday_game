from flask import Flask, render_template, redirect, session, flash 
# from flask_debugtoolbar import DebugToolbarExtension
from model import connect_db, db, User , Question_results
from forms import RegisterForm, LoginForm , bdayForm
import requests
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///bdayGame"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "ImGlutenFree"


connect_db(app)

with app.app_context():
    db.create_all()

# toolbar = DebugToolbarExtension(app)

 
@app.route("/")
def homepage():
    """Show homepage with links to site areas."""

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user: produce form & handle form submission."""

    form = RegisterForm()

    if form.validate_on_submit():
        
        
        name = form.username.data
        pwd = form.password.data

        user = User.register(name, pwd)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        # on successful login, redirect to welcome page
        return redirect("/welcome.html")

    else:
        return render_template("users/register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form or handle login."""

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(name, pwd)

        if user:
            session["user_id"] = user.id  # keep logged in
            return redirect("/welcome")

        else:
            form.username.errors = ["incorrect name or password"]

    return render_template("users/login.html", form=form)
# end-login


@app.route("/welcome")
def logedin():
    """Welcome page"""

    if "user_id" not in session:
        flash("You must be logged in to play!")
        return redirect("/")

    else:
        return render_template("welcome.html")


@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")

@app.route("/newgame", methods=['GET','POST'])
def new_game():
    """Renders form and handles answer input"""
    form = bdayForm()
    if form.validate_on_submit():
    
        question_1 = form.question_1.data 
        question_2 = form.question_2.data
        question_3 = form.question_3.data
        question_4 = form.question_4.data
        question_5 = form.question_5.data
        question_6 = form.question_6.data
        question_7 = form.question_7.data
        question_8 = form.question_8.data
        
        question_results = Question_results(question_1=question_1 ,
                                   question_2=question_2 ,
                                   question_3=question_3,
                                   question_4=question_4,
                                   question_5=question_5,
                                   question_6=question_6,
                                   question_7=question_7,
                                   question_8=question_8)
        
        db.session.add(question_results)
        db.session.commit()
        
        return redirect('/success')
    else:
        return render_template("/newgame.html" , form=form)
    
@app.route("/success", methods=["GET"])
def success_submission():

    cat_pic = requests.get('https://api.thecatapi.com/v1/images/search?api_key=live_JEVI7m2hEzE9hbDB1Ob0N8syy13o7OT2YCXReRfjtc7qT9zmKE9qEKh7rK5uWWg9')
    data=json.loads(cat_pic.content)
    
    return render_template("/success.html" , data=data)

    
@app.route("/previousgames",methods=['GET'])
def old_results():
    
    res = Question_results.query.all()
    return render_template("/previousgames.html", res=res)




