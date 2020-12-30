#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static folder."""

from datetime import datetime
import os
from fabric.api import env, run, put, local
env.hosts = ['35.227.13.38', '35.231.175.126']
env.user = 'ubuntu'


def do_pack():
    """tar -czvf web_static."""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = 'versions/web_static_{}.tgz'.format(date)
    try:
        if not os.path.isdir('versions'):
            os.mkdir('versions')
        local('tar -czvf {} web_static'.format(filename))
        return filename
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """Distribute an archive to your web servers."""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        name = filename.split('.')[0]
        """Complete Path."""
        cpth = '/data/web_static/releases/{}'.format(name)
        pth = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(pth))
        run("tar -xzf /tmp/{} -C {}/".format(filename, pth))
        run("mv {0}/web_static {0}/{1}".format(pth, name))
        run("rm /tmp/{}".format(filename))
        run("rm /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(cpth))
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Create and distribute an archive to your web server."""

    filepath = do_pack()
    if filepath is None:
        return False
    return do_deploy(filepath)
