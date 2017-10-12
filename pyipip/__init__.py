__version__ = '0.1.1'

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

from .ipipdb import IPIPDatabase

