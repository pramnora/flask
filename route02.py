# Routing using Flask...
# In order to see the 'default' route/and, text, type:
# localhost:5000
# In order to see the 'user defined' route/along with parameter passing, type: 
# localhost:5000/route2/anyTextGoesHere

from flask import *

app = Flask(__name__)

@app.route('/')

def message1():
 return "Parameter passing using routes."
 
@app.route('/route2/<myparameter>')

def message2(myparameter):
 return "User defined text: " + myparameter

if __name__ == '__main__':
 app.run()
