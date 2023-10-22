#!/usr/bin/python3
"""
deploying web_static to a server
"""
from fabric.api import env, local, put, run, task
from os.path import exists, splitext
from datetime import datetime

env.hosts = ['52.86.89.214', '52.3.254.204']


@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    local("mkdir -p versions")
    created = datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(created))
    return ("versions/web_static_{}.tgz".format(created))


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        base_name = archive_path.split("/")[-1]
        file_name = base_name.split(".")[0]
        dest_path = "/data/web_static/releases/{}/".format(file_name)

        run("mkdir -p {}".format(dest_path))
        run("tar -xzf /tmp/{} -C {}".format(base_name, dest_path))

        run("rm /tmp/{}".format(base_name))

        run("mv {0}web_static/* {0}".format(dest_path))

        run("rm -rf {}web_static".format(dest_path))
        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(dest_path))

        print("New version deployed!")

    except Exception:
        return False

    return True


def deploy():
    """Creates and distributes an archive to your web servers"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
