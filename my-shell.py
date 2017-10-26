import os
import sys
import cmd
import shlex
import subprocess
import signal
from builtins import *
builtins = {
    'cd': cd,
    'exit': exit
}
def handler_kill(signum, frame):
    raise OSError("Killed")

def shell():
    """executes the shell"""
    status = 1
    while status == 1:
	# ignore ctrl C
	signal.signal(signal.SIGINT, signal.SIG_IGN)
	show_prompt()
	try:
	    # reads line from user input and stores input in cmd
	    cmd = sys.stdin.readline()
	    # uses shell-like syntax to split the input
	    # store in a tokens
	    tokens = shlex.split(cmd)
	    status = execute(tokens)
	except:
            _, err, _ = sys.exc_info()
            print(err)
    return 1

def execute(tokens):
    # determines if user has typed a program interrupt	   
    signal.signal(signal.SIGINT, handler_kill) 
    if tokens[0] in builtins:
	builtins[tokens[0]](tokens[1:])
    else:
	# creates a child process
	process = subprocess.Popen(tokens)
        # wait for process to terminate
        status = process.communicate()
    return 1

def show_prompt():
    """shows prompt"""
    sys.stdout.write("$ ")
    sys.stdout.flush()

shell()
