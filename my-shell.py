import os
import sys
import cmd
import shlex
import subprocess
import signal
def handler_kill(signum, frame):
    raise OSError("Killed")

def shell():
    """does the thing"""
    status = 1
    while status == 1:
#	import pdb;pdb.set_trace()
	show_prompt()
	try:
	    cmd = sys.stdin.readline()
	    signal.signal(signal.SIGINT, handler_kill) 
	    tokens = shlex.split(cmd)
	    process = subprocess.Popen(tokens)
	    status = process.communicate()
	except:
            _, err, _ = sys.exc_info()
            print(err)
    return 1

def show_prompt():
    """shows prompt and accepts input"""
    sys.stdout.write("$ ")
    sys.stdout.flush()

shell()
