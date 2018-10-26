# Displaying web pages using Flask.

# First, create a sub-directiory folder called: templates;
# and, inside of the 'templates' folder...;
# create a web page file called: web01.html.

# When you run the following code...; 
# by typing into your web browser software address bar: 
# localhost:5000
# ...then, pressing the [Enter] key;
# the 'web01.html' web page should, automatically, display. 

from flask import *

app = Flask(__name__)

@app.route('/')

def showWebPage():
 return render_template("web01.html")

if __name__=="__main__":
 app.run()
