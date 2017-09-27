#!/usr/bin/env python3

"""
PaStA - Patch Stack Analysis

Copyright (c) OTH Regensburg, 2017

Author:
  Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>

This work is licensed under the terms of the GNU GPL, version 2.  See
the COPYING file in the top-level directory.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PaStA import *


def web(config, prog, argv):
    print('Hello, %s!' % prog)


if __name__ == '__main__':
    config = Config(sys.argv[1])
    web(config, sys.argv[0], sys.argv[2:])
