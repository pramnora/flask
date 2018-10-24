# Routing using Flask...
# In order to see the 'default' route type: localhost:5000
# In order to see the 'user defined' route type: localhost:5000/route2

from flask import *

app = Flask(__name__)

@app.route('/')

def message1():
 return "This is the 'default' route."
 
@app.route('/route2')

def message2():
 return "This is the 'user defined' route."

if __name__ == '__main__':
 app.run()
