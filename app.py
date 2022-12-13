from flask import Flask , render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECERET_KEY'] = "ImGlutenIntolerant"

@app.route('/')

def home_page():
   
   return render_template("index.html") 
