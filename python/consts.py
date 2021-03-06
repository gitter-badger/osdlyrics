# -*- coding: utf-8 -*-
#
# Copyright (C) 2011  Tiger Soldier
#
# This file is part of OSD Lyrics.
#
# OSD Lyrics is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OSD Lyrics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OSD Lyrics.  If not, see <http://www.gnu.org/licenses/>.
#

# DBus names, interfaces and object paths

DAEMON_BUS_NAME = 'org.osdlyrics.Daemon'
CONFIG_BUS_NAME = 'org.osdlyrics.Config'
CONFIG_OBJECT_PATH = '/org/osdlyrics/Config'
PLAYER_PROXY_INTERFACE = 'org.osdlyrics.PlayerProxy'
PLAYER_PROXY_OBJECT_PATH_PREFIX = '/org/osdlyrics/PlayerProxy/'
MPRIS2_PLAYER_INTERFACE = 'org.mpris.MediaPlayer2.Player'
MPRIS2_OBJECT_PATH = '/org/mpris/MediaPlayer2'
LYRIC_SOURCE_PLUGIN_INTERFACE = 'org.osdlyrics.LyricSourcePlugin'
LYRIC_SOURCE_PLUGIN_OBJECT_PATH_PREFIX = '/org/osdlyrics/LyricSourcePlugin/'

# Metadata keys
METADATA_TITLE = 'title'
METADATA_ARTIST = 'artist'
METADATA_ALBUM = 'album'
METADATA_TRACKNUM = 'tracknumber'
METADATA_URI = 'location'
