# Displaying web pages using Flask.

# First, create a sub-directiory folder called: templates;
# and, inside of the 'templates' folder...;
# create a web page file called: test01.html.

# When you run the following code...; 
# the 'test01.html' web page should, automatically, 
# load up and display itself inside of your web browser software.

from flask import *

app = Flask(__name__)

@app.route('/')

def showWebPage():
 return render_template("test01.html")

if __name__=="__main__":
 app.run()
