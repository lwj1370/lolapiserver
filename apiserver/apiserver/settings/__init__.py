import os
from ._base import *

if os.environ['config'] == 'prod':
    from .prod import *
else : 
    from .dev import *
