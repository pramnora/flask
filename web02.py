# Displaying web pages using Flask.

# First, create a sub-directory folder called: templates;
# and, inside of the 'templates' folder...;
# create a web page file called: web02.html.

# When you run the following code...; 
# the 'web02.html' web page should, automatically, 
# load up and display itself inside of your web browser software.

# The variables strName/intIDNumber values will show inside of the web page: web02.html;
# in the web page itself these variables are referred to as: {{name}} {{id}}

from flask import *

app = Flask(__name__)

@app.route('/')

def showWebPage():
 strName = "John Doe"
 intIDNumber = 123
 return render_template("web02.html",name=strName,id=intIDNumber)

if __name__=="__main__":
 app.run()
