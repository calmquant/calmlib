import sys
import os
sys.path.append(os.path.expanduser('~/repos/calmlib'))
sys.path.append(os.path.expanduser('~/repos/simple-proto-db'))
sys.path.append(os.path.expanduser('~/repos/simple-task-repeater'))

from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns

import math

# todo: time
#  1) parse date
#  2) create timedelta
#  3) now - date, datetime
#  4) formatting - date, date with time
import time

import sys
import os

# todo: help - easily remembered method to remind everything else. Do modules have docstrings? Oh its not a module

# calmlib
import calmlib
from calmlib import run_cmd
