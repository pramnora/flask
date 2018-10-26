# Displaying web pages using Flask.

# First, create a sub-directiory folder called: templates;
# and, inside of the 'templates' folder...;
# create a web page file called: web01.html.

# After running the following code...; 
# go to your web browser software; and, in the address bar type in: 
# localhost:5000
# ...next, press the [Enter] key;
# and, the 'web01.html' web page should, automatically, show. 

from flask import *

app = Flask(__name__)

@app.route('/')

def showWebPage():
 return render_template("web01.html")

if __name__=="__main__":
 app.run()
