#!/usr/bin/python3
"""
The `3-deploy_web_static` module supplies a function `deploy` that creates and
distributes an archive to web servers based on `2-do_deploy_web_static` module
"""


from fabric.api import *
from datetime import datetime
import os


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
    if local("mkdir -p versions").failed:
        return None
    time_fm = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"web_static_{time_fm}.tgz"
    dest_folder = f"versions/{file_name}"
    if local(f"tar -cvzf {dest_folder} web_static").failed:
        return None
    return file_name


@task
def do_deploy(archive_path):
    """
    Defines a function that distributes an archive to your web servers
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
        (using env.hosts=['<IP web-01>','IP web-02'] variable in your script)
        Returns True if all operations executed successfully, otherwise False
    """

    if not os.path.exists(archive_path):
        return False
    symlink = "/data/web_static/current"
    file_name = archive_path.split("/")[-1]
    file_d = file_name.split(".")[0]
    dir_pt = "/data/web_static/releases"

    if put(f"{archive_path}", "/tmp/").failed:
        return False
    if run(f"mkdir -p {dir_pt}/{file_d}").failed:
        return False
    if run(f"tar -xzf /tmp/{file_name} -C {dir_pt}/{file_d}").failed:
        return False
    if run(f"rm /tmp/{file_name}").failed:
        return False
    if run(f"mv {dir_pt}/{file_d}/web_static/* {dir_pt}/{file_d}").failed:
        return False
    if run(f"rm -rf {dir_pt}/{file_d}/web_static").failed:
        return False
    if run(f"rm -rf {symlink}").failed:
        return False
    if run(f"ln -s {dir_pt}/{file_d} {symlink}").failed:
        return False
    return True


@task
def deploy():
    """
    :Defines a function that creates and distributes an archive to web servers
    Requirements:
    The script should take the following steps:
        Call the do_pack() function and store the path of the created archive
    Return False if no archive has been created
    Call the do_deploy(archive_path) function, using the new path of the new
    archive
    Return the return value of do_deploy
    """
    ret_path = do_pack()
    if ret_path is None:
        return False
    return do_deploy(ret_path)
