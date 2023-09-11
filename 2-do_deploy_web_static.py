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
def do_pack():
    """
    Defines a function that generates a .tgz archive from the contents
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
        All remote commands must be executed on your both web servers (using env.hosts
            = ['<IP web-01>', 'IP web-02'] variable in your script)
        Returns True if all operations have been done correctly, otherwise False
    """
    try:
            if not (path.exists(archive_path)):
                    return False

            # upload archive
            put(archive_path, '/tmp/')

            # create target dir
            timestamp = archive_path[-18:-4]
            run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

            # uncompress archive and delete .tgz
            run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                .format(timestamp, timestamp))

            # remove archive
            run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

            # move contents into host web_static
            run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

            # remove extraneous web_static dir
            run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                .format(timestamp))

            # delete pre-existing sym link
            run('sudo rm -rf /data/web_static/current')

            # re-establish symbolic link
            run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
            return False

    # return True on success
    return True
