#!/usr/bin/python3
""" Fabric script to create tarball"""

import tarfile
import os
from datetime import datetime


def do_pack():
    """ Creates tar archive"""
    folder = "versions/"
    filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(folder):
        os.mkdir(folder)
    with tarfile.open(folder + filename, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(folder + filename):
        return folder + filename
    else:
        return None
