# Displaying web pages using Flask.

# First, create a sub-directory folder called: templates;
# and, inside of the 'templates' folder...;
# create a web page file called: if01.html.

# When you run the following code...; 
# the 'if01.html' web page should, automatically, 
# load up and display itself inside of your web browser software.

# Inside of the web page itself variable: strUserDefinedText, is referred to as: {{text}}

# NOTE: This file is called using...
# http://localhost:5000/y
# http://localhost:5000/n
# http://localhost:5000/anytextyouplease

from flask import *

app = Flask(__name__)

@app.route('/<strUserDefinedText>')

def showWebPage(strUserDefinedText):
 return render_template("if01.html",text=strUserDefinedText)

if __name__=="__main__":
 app.run()
