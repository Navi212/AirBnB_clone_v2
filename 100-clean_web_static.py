#!/usr/bin/python3
"""
The `100-clean_web_static` module supplies a function `do_clean`that deletes
out-of-date archives from the versions/ and /data/web_static/releases folders
on our webservers based on `3-deploy_web_static` module
"""


from fabric.api import *


env.user = "ubuntu"
env.hosts = ['52.86.24.88', '100.26.20.84']


@task
def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): Number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive.
    If number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1
    local(f"cd versions ; ls -t | tail -n +{number} | xargs rm -rf")
    path = "/data/web_static/releases"
    run(f"cd {path} ; ls -t | tail -n +{number} | xargs rm -rf")
