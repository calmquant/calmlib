from .execution import run_cmd, run_bg
from .unsorted import fix_path
from .read_write import load, dump, load_json, dump_json, load_pickle, dump_pickle
from .autocast import autocast_args
from .logging_utils import get_personal_logger


def format_date(ts):
    return ts.strftime('%Y-%m-%d')
