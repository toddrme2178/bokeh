#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2017, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' Provide tools for interacting with git.

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
import subprocess
import sys

# External imports

# Bokeh imports
from bokeh.util.terminal import write
from bokeh._version import get_versions

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def version_from_git(ref):
    ''' Get the git-version of a specific ref, e.g. HEAD, origin/master.

    '''
    cmd = ["git", "describe", "--tags", "--always", ref]

    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        code = proc.wait()
    except OSError:
        OSError("Failed to run: %s" % " ".join(cmd))

    if code != 0:
        OSError("Failed to get version for %s" % ref)

    version = proc.stdout.read().decode('utf-8').strip()

    try:
        # git-version = tag-num-gSHA1
        tag, _, sha1 = version.split("-")
    except ValueError:
        return version
    else:
        return "%s-%s" % (tag, sha1[1:])

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

try:
    __version__ = version_from_git('HEAD')
except OSError:
    __version__ = get_versions()['version']

