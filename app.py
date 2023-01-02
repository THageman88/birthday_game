from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_db, db, User , Question_results
from forms import RegisterForm, LoginForm , bdayForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///bdayGame"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "ImGlutenFree"

connect_db(app)

with app.app_context():
    db.create_all()

toolbar = DebugToolbarExtension(app)

 
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
        return redirect("/welcome")

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
    """Example hidden page for logged-in users only."""

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

@app.route("/newgame", methods=["GET","POST"])
def new_game():
    
    form = bdayForm()
    
    if form.validate_on_submit():

        q1 = form.question_1.data
        q2 = form.question_2.data
        q3 = form.question_3.data
        q4 = form.question_4.data
        q5 = form.question_5.data
        q6 = form.question_6.data
        q7 = form.question_7.data
        q8 = form.question_8.data
        
        question_results = Question_results(q1 , q2, q3 , q4 , q5, q6, q7, q8)
        db.session.add(question_results)
        db.session.commit()
        
        return render_template("/newgame.html")
    
    else:
        return redirect("/" , form=form)

@app.route("/previousgames")
def old_results():
    return render_template("/previousgames.html")
