# 1) run external binary - basically any bash command
import subprocess
def run_cmd(cmd, stdin=''):
    from subprocess import Popen, PIPE

    p = Popen(cmd.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(stdin.encode())
    rc = p.returncode
    if rc:
        raise Exception(err)
    return output.decode()
# 2) run python code - eval
# 3) run python function in backgroud - threading, subprocess etc.