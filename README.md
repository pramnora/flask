# flask
Python Flask (3rd party module)

-----

## What does it do? 

Flask, allows Python developers to both create/run their own 'server side' web pages.

-----

## In order to run Flask/first, you must download and set up the Python language itself...

First, make sure you have the Python language already installed on your computer system.

Python language is a FREE downloaded from:    
http://www.python.org  
...just click on the top menu link: Downloads (the lastest version is: 3.7.1)

## How to download/set up Flask...

C:\Windows\system32>pip install flask

(NOTE: There may be some further instructions given in order to update Flask to the latest version; please, follow those instructions.)

-----

## How to check that Flask has been installed; after opening Python...at the prompt type in...

>import flask  
>dir(flask)  
['Blueprint', 'Config', 'Flask', 'Markup', 'Request', 'Response', 'Session', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_app_ctx_stack', '_compat', '_request_ctx_stack', 'abort', 'after_this_request', 'app', 'appcontext_popped', 'appcontext_pushed', 'appcontext_tearing_down', 'before_render_template', 'blueprints', 'cli', 'config', 'copy_current_request_context', 'ctx', 'current_app', 'escape', 'flash', 'g', 'get_flashed_messages', 'get_template_attribute', 'globals', 'got_request_exception', 'has_app_context', 'has_request_context', 'helpers', 'json', 'json_available', 'jsonify', 'logging', 'make_response', 'message_flashed', 'redirect', 'render_template', 'render_template_string', 'request', 'request_finished', 'request_started', 'request_tearing_down', 'safe_join', 'send_file', 'send_from_directory', 'session', 'sessions', 'signals', 'signals_available', 'stream_with_context', 'template_rendered', 'templating', 'url_for', 'wrappers']

-----

## Writing you first Flask 'Hello, world!' program...

from flask import *

app = Flask(__name__)

@app.route('/')

def hw():

return "Hello, world! - From Flask"

if __name__ == '__main__':
 app.run()
 
 ...save the above file as being called: hw01.py; then, left double click on it to RUN...
 
 ...next, switch to your web browser: and, type in...  
 http://127.0.0.1:5000  
 ...or, alternatively...  
 localhost:5000  
 ...you should see the output shown as follows...  
 Hello, world! - From Flask  
 
 (_NOTE_: Press [CTRL]+[C] to stop the server running.)
 
 ...warmest congratulations; you've just created and run you very first Flask web page.
 
 Now, all that's left to do is follow along some tutorials in order to go learn more...
 
 -----
 
 Flask online tutorials...
 
## YouTube
 
YouTube Channel: RaunakJoshi  
https://www.youtube.com/watch?v=eFksV6rqdTU&list=PLT_6xP6jAq8j_m9OWFWlx1snf5uco6_m5&index=1  


 
 
