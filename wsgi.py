#!/venv/bin/python
import os
import sys
import logging
from webApp import app as application

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/dominwrites.com/")

application.secret_key = '#'
