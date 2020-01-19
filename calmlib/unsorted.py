from pathlib import Path

from calmlib.autocast import autocast_args


@autocast_args
def fix_path(path: Path):
    return path.expanduser().absolute()
