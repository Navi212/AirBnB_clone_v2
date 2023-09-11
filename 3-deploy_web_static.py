#!/usr/bin/python3
"""
The `3-deploy_web_static` module supplies a function `deploy` that creates and
distributes an archive to web servers based on `2-do_deploy_web_static` module
"""


from fabric.api import *


env.user = "ubuntu"
env.hosts = ['52.86.24.88', '100.26.20.84']

@task
def deploy():
    """
    :Defines a function that creates and distributes an archive to your web servers
    Requirements:
    The script should take the following steps:
        Call the do_pack() function and store the path of the created archive
    Return False if no archive has been created
    Call the do_deploy(archive_path) function, using the new path of the new archive
    Return the return value of do_deploy
    """
    ret_path = do_pack()
    if ret_path is None or ret_path.failed:
        return False
    ret_val = do_deploy(ret_path)
    if ret_val.succeeded:
        return ret_val
