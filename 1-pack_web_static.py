#!/usr/bin/python3
"""
Generate a .tgz archive from the contents
of the web_static folder.
"""

from fabric.api import local
import os
from datetime import datetime


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
