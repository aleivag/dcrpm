#!/usr/bin/env python
#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the GPLv2 license found in the LICENSE
# file in the root directory of this source tree.
#
# pyre-strict

import logging
import enum
import psutil

from typing import Optional, Set, Iterable

DEFAULT_TIMEOUT: int
LSOF_TIMEOUT: int = 60
MIN_PID: int
logger: logging.Logger

def process(pid: int) -> Optional[psutil.Process]: ...
def _pids_holding_file(lsof: str, path: str) -> Set[int]: ...
def procs_holding_file(path: str) -> Set[psutil.Process]: ...
def pidfile_info(pidfile: str) -> Tuple[int, int]: ...
def send_signal(proc: psutil.Process, sig: enum.IntEnum, timeout: int): ...
def send_signals(
    procs: Iterable[psutil.Process], signal: enum.IntEnum, timeout: int,
) -> bool: ...
