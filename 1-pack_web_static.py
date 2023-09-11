#!/usr/bin/python3
"""
The `2-do_deploy_web_static` module supplies a function `do_pack`
that generates a .tgz archive from the contents of the web_static
folder of our AirBnB Clone v2 repo
"""


from fabric.api import *
from datetime import datetime
from os import path


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
