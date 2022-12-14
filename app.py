from flask import Flask , render_template
from flask_debugtoolbar import DebugToolbarExtension
from forms import register_new_user


app = Flask(__name__)

app.config['SECRET_KEY'] = "ImGlutenIntolerant"
debug= DebugToolbarExtension(app)

@app.route('/')

def home_page():
   
   return render_template("index.html") 

@app.route('/users/login')
def login():
   
   return render_template("users/login.html")

@app.route("/users/register", methods=["GET","POST"])
def register():
   form = register_new_user() 
   
   return render_template('users/register.html', form=form)
