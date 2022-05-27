#!/usr/bin/python3.10.4
import sys
import logging
import os
logging.basicConfig(stream=sus/stderr)
sys.path.insert(0, "/var/www/webApp/")

from webApp import app as application
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
application.secret_key = app.config['SECRET_KEY']