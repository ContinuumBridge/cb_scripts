#!/usr/bin/env python
# makeapp.py
# Copyright (C) ContinuumBridge Limited, 2013-14 - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Peter Claydon
#
# It is assumed that all apps and adaptors will be in directories ~/cb_apps and ~/cb_adaptors

import time, sys, os
#
if len(sys.argv) < r32:
    print "Usage: makeapp.py <type> <name>, where type is app or adaptor"
    exit()
else:
    element = sys.argv[1]
    name = sys.argv[2]

git describe > cb_version
