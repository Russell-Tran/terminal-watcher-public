""" This is used so that scheduler can function
--Russell 
"otherwise, Heroku will think your app isn't working and it will be in the 'crashed' state"
"""

#from os import environ

import os
from flask import Flask

app = Flask(__name__)


# app.run(environ.get('PORT'))
port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)

print("Hello world I love you!")