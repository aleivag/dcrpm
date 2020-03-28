#!/usr/bin/env python
#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the GPLv2 license found in the LICENSE
# file in the root directory of this source tree.
#
# pyre-strict

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import signal
import time

from . import pidutil
from .util import (
    DBNeedsRebuild,
    DcRPMException,
    RepairAction,
    read_os_name,
    run_with_timeout,
    which,
)

YUM_PID_PATH = "/var/run/yum.pid"  # type: str
YUM_TIMEOUT_SEC = 30  # type: int
# 6 hours
MIN_YUM_AGE = 3600 * 6  # type: int
YUM_CMD_NAME = "yum"  # type: str
DNF_CMD_NAME = "dnf"  # type: str
KILL_TIMEOUT = 5  # type: int

class Yum:
    def __init__(self) -> None: ...
    def check_stuck(self, dry_run: bool = False) -> bool: ...
    def run_yum_clean(self) -> None: ...
    def run_yum_check(self) -> None: ...
