import sys
import os

from pathlib import Path


# dir_root = location of this file / .. / ..
def get_git_root():
    return Path(__file__).resolve().parent.parent.parent


git_root = get_git_root()

sys.path.append(os.path.expanduser(git_root / 'calmlib'))
sys.path.append(os.path.expanduser(git_root / 'simple-proto-db'))
sys.path.append(os.path.expanduser(git_root / 'simple-task-repeater'))

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
# from calmlib import run_cmd
# from calmlib import load_json
from calmlib import *
