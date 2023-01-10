#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
using the function do_pack."""

import os
from pathlib import Path
from fabric.api import local, env, run, put
from datetime import datetime

env.hosts = ["18.206.208.218", "52.201.228.174"]


def do_pack():
    """ generating a .tgz archive"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(path))

    if result.succeeded:
        return path
    else:
        return None


def do_deploy(archive_path):
    """Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy"""
    if os.path.exists(archive_path):
        archive_file = os.path.basename(archive_path)
        archive_folder = Path(archive_path).stem
        archived_path = "/data/web_static/releases/{}/".format(archive_folder)

        put(archive_path, "/tmp/{}".format(archive_file))
        run("mkdir - p {}".format(archived_path))
        run("tar -xvzf /tmp/{} -C {}".format(archive_file, archived_path))
        run("rm -rf /tmp/{}".format(archive_file))
        run("mv {}/web_static/* {}".format(archived_path, archived_path))
        run("rm -rf {}/web_static".format(archived_path))
        run("rm -rf /data/web-static/current")
        run("ln -s {} /data/web_static/current".format(archived_path))

        print("New version deployed!")
        return True
    return False
