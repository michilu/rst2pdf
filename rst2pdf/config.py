# -*- coding: utf-8 -*-
# See LICENSE.txt for licensing terms
"""Singleton config object"""


import ConfigParser
import os
try:
    from json import loads
except ImportError:
    from simplejson import loads

cfdir = os.path.join(os.path.expanduser('~'), '.rst2pdf')
cfname = os.path.join(cfdir, 'config')


def getValue(section, key, default=None):
    section = section.lower()
    key = key.lower()
    try:
        return loads(conf.get(section, key))
    except Exception:
        return default


class ConfigError(Exception):

    def __init__(self, modulename, msg):
        self.modulename = modulename
        self.msg = msg


conf = ConfigParser.SafeConfigParser()
conf.read(["/etc/rst2pdf.conf", cfname])
