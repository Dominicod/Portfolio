#!/venv/bin/python
import os
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/dominwrites.com/")

from webApp import app as application

application.secret_key = '#'
