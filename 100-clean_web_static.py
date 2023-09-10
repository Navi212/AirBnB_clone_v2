#!/usr/bin/python3
"""
The `100-clean_web_static` module supplies a function `do_clean`that deletes
out-of-date archives from the versions/ and /data/web_static/releases folders
on our webservers based on `3-deploy_web_static` module
"""


from __future__ import with_statement
from fabric.api import *
from datetime import datetime
from os import path


env.user = "ubuntu"
env.hosts = ['52.86.24.88', '100.26.20.84']


@task
def do_pack():
    """
    :Defines a function that generates a .tgz archive from the contents
    of the web_static folder of AirBnB Clone repo
    Requirements:
        All files in the folder web_static must be added to the final archive
        All archives must be stored in the folder versions (your function
            should create this folder if it doesn’t exist)
        The name of the archive created must be
            web_static_<year><month><day><hour><minute><second>.tgz
        The function do_pack must return the archive path if the archive has
            been correctly generated. Otherwise, it should return None
    """
    with settings(warn_only=True):
        if local("mkdir -p versions", capture=True).failed:
            return None
        time_fm = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"web_static_{time_fm}.tgz"
        dest_folder = f"versions/{file_name}"
        if local(f"tar -cvzf {dest_folder} web_static", capture=True).failed:
            return None
        return file_name


@task
def do_deploy(archive_path):
    """
    :Defines a function that distributes an archive to your web servers
    Requirements:
        Returns False if the file at the path archive_path doesn’t exist
        The script should take the following steps:
            Upload the archive to the /tmp/ directory of the web server
            Uncompress the archive to the folder /data/web_static/releases
                /<archive filename without extension> on the web server
        Delete the archive from the web server
        Delete the symbolic link /data/web_static/current from the web server
        Create a new the symbolic link /data/web_static/current on the web
            server, linked to the new version of your code (/data/web_static
            /releases/<archive filename without extension>)
        All remote commands must be executed on your both web servers
        Returns True if all operations have been done correctly, otherwise
        False
    """
    if not path.exists(archive_path):
        return False
    if put("archive_path", "/tmp/").failed:
        return False
    file_name = f"web_static_{time_fm}"
    if run(f"tar -xvzf archive_path -C /data/web_static/releases/{file_name}").failed:
         return False
    if run("rm -f /tmp/archive_path").failed:
        return False
    if run("ln -sf /data/web_static/releases/{file_name} /data/web_static/current").failed:
        return False
    return True


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
    with settings(warn_only=True):
        ret_path = execute(do_pack, capture=True)
        if ret_path is None or ret_path.failed:
            return False
        ret_val = execute(do_deploy, capture=True)
        if ret_val.succeeded:
            return ret_val


@task
def do_clean(number=0):
    """Delete out-of-date archives.

    Requirements:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
