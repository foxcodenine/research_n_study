#!/usr/bin/python
activate_this = '/home/ubuntu/.local/share/virtualenvs/mfp-tvtPaMX2/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/mfp/")

from coin_manager import app as application