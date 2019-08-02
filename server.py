""" This is used so that scheduler can function
--Russell 
"otherwise, Heroku will think your app isn't working and it will be in the 'crashed' state"
"""

from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))