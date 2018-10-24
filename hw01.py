#My 1st 'Hello, world!' program using Flask...

from flask import *

app = Flask(__name__)

@app.route('/')

def hw():
 return "Hello, world! - From Flask"
 
if __name__ == '__main__':
 app.run()
