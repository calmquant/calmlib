from .execution import run_cmd
from pandas import Timestamp, Timedelta


def format_date(ts):
    return ts.strftime('%Y-%m-%d')
