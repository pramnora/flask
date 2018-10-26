# This mimimal code example
# demonstrates how to use Python Flask framework to serve up either
# - a text message
# - a web page

# NOTE: If you are going to serve up a web page;
#       then, it's necessary to create a sub-directory folder called: Templates,
#       in which to store the web page file: anywebpagename.html.

# Otherwise, only a text message will get returned.

from flask import *
app = Flask(__name__)
@app.route('/')
def anyFunctionName():
 return "any output message" 
# return render_template('anywebpagename.html')
if __name__=='__main__':
 app.run()

