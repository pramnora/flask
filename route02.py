# Routing, together with parameter passing using Flask...
# In order to see the 'default' route/and, text, type:
# localhost:5000/yourOwnTextGoesHere

from flask import *

app = Flask(__name__)

@app.route('/<myparameter>')

def message(myparameter):
 return "Parameter passing using routes: " + myparameter
 
if __name__ == '__main__':
 app.run()
