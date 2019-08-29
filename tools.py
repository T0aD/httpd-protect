
import subprocess, shlex
import os

def run(cmd, cwd=False):
    if not cwd is False:
        os.chdir(cwd)
    print os.getcwd(), '$', cmd

    p = subprocess.Popen(shlex.split(cmd), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
    try:
        stdout, stderr = p.communicate()
    except Exception as e:
        print 'Unknown exception:', e
        raise

    if len(stdout) != 0:
        print 'stdout>', stdout
    if len(stderr) != 0:
        print 'stderr>', stderr

    if p.returncode != 0:
        print 'rv not 0:', p.returncode

    return p.returncode

