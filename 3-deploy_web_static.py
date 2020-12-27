#!/usr/bin/python3
"""Deploy archive."""
import os
from fabric import api
import tarfile
from datetime import datetime

api.env.hosts = ['35.227.13.38', '35.231.175.126']
api.env.user = "ubuntu"


def deploy():
    """Deploy archive to webservs."""
    tar = do_pack()
    if not tar:
        return False
    return do_deploy(tar)


def do_pack():
    """ Creates tar archive"""
    savedir = "versions/"
    filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    with tarfile.open(savedir + filename, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(savedir + filename):
        return savedir + filename
    else:
        return None


def do_deploy(archive_path):
    """Distribute an archive to your web servers."""

    if not os.path.exists(archive_path):
        return False

    results = []

    upload = api.put(archive_path, '/tmp')
    results.append(upload.succeeded)

    basename = os.path.basename(archive_path)
    if basename[-4:] == '.tgz':
        name = basename[:-4]
    newdir = '/data/web_static/releases/' + name
    api.run('mkdir -p {}'.format(newdir))
    api.run("tar -xzf /tmp/{} -C {}".format(basename, newdir))

    api.run("rm /tmp/{}".format(basename))
    api.run("mv {}/web_static/* {}".format(newdir, newdir))
    api.run("rm -rf {}/web_static".format(newdir))
    api.run("rm -rf /data/web_static/current")
    api.run("ln -s {} /data/web_static/current".format(newdir))

    return True
