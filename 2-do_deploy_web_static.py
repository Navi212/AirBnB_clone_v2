#!/usr/bin/python3
"""
The `2-do_deploy_web_static` module supplies a function `do_deploy` that creates
and distributes an archive to our web servers based on `1-pack_web_static` module
"""


from fabric.api import *
from datetime import datetime
import os


env.user = "ubuntu"
env.hosts = ['52.86.24.88', '100.26.20.84']

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
        All remote commands must be executed on your both web servers (using env.hosts
            = ['<IP web-01>', 'IP web-02'] variable in your script)
        Returns True if all operations have been done correctly, otherwise False
    """
    if not path.exists(archive_path):
        return False
    symlink = "/data/web_static/current"
    file_name = archive_path.split("/")[-1]
    file_dir = file_name.split(".")[0]
    dir_path = "/data/web_static/releases"

    if put(f"{archive_path}", "/tmp/").failed:
        return False
    if run(f"mkdir -p {dir_path}/{file_dir}").failed:
        return False
    if run(f"tar -xvzf /tmp/{file_name} -C {dir_path}/{file_dir}").failed:
        return False
    if run(f"mv {dir_path}/{file_dir}/web_static/* {dir_path}/{file_dir}").failed:
        return False
    if run(f"ln -sf {dir_path}/{file_dir} {symlink}").failed:
        return False
    return True
