import os

def cd(tokens):
    # check if a directory has been passed in to cd to
    if len(tokens) > 0:
	os.chdir(tokens[0])
    else:
	# change to $HOME if no args passed
	os.chdir(os.getenv['HOME'])
    return 1
