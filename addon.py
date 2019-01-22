# -*- coding: utf-8 -*-

from resources.lib import kodilogging
from resources.lib import plugin

import logging
import xbmcaddon
import os

# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
ADDON = xbmcaddon.Addon()
kodilogging.config()
from_plugin_path = os.path.dirname(os.path.realpath(__file__))

plugin.launch_parsec(from_plugin_path)
