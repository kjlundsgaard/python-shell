import os
import sys
import cmd
import shlex
import subprocess
import signal
def handler_kill(signum, frame):
    raise OSError("Killed")

def shell():
    """executes the shell"""
    status = 1
    while status == 1:
	show_prompt()
	try:
	    # reads line from user input and stores input in cmd
	    cmd = sys.stdin.readline()
	    # determines if user has typed a program interrupt
	    signal.signal(signal.SIGINT, handler_kill) 
	    # uses shell-like syntax to split the input
	    # store in a tokens
	    tokens = shlex.split(cmd)
	    # creates a child process
	    process = subprocess.Popen(tokens)
	    # wait for process to terminate
	    status = process.communicate()
	except:
            _, err, _ = sys.exc_info()
            print(err)
    return 1

def show_prompt():
    """shows prompt"""
    sys.stdout.write("$ ")
    sys.stdout.flush()

shell()
