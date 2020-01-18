from .execution import run_cmd
from pandas import Timestamp, Timedelta
from .read_write import load, dump, load_json, dump_json, load_pickle, dump_pickle


def format_date(ts):
    return ts.strftime('%Y-%m-%d')
