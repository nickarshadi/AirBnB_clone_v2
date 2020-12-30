#!/usr/bin/python3
"""Generate a .tgz archive from the contents of the web_static folder."""

from fabric.api import env, run, put
from os.path import exists
env.hosts = ['35.227.13.38', '35.231.175.126']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distribute an archive to your web servers."""
    if not exists(archive_path):
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
