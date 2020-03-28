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
import os
import signal
import subprocess

try:
    import typing as t

    if t.TYPE_CHECKING:
        from types import FrameType
except ImportError:
    pass

END_TIMEOUT: int

_logger: logging.Logger

class StatusCode:

    SUCCESS: int
    SEGFAULT: int = -11

class DcRPMException(Exception): ...
class DBNeedsRecovery(DcRPMException): ...
class DBIndexNeedsRebuild(DcRPMException): ...
class DBNeedsRebuild(DcRPMException): ...
class TimeoutExpired(Exception): ...

class CompletedProcess:
    def __init__(
        self, stdout: str = "", stderr: str = "", returncode: int = 0
    ) -> None: ...

class RepairAction:

    NO_ACTION: int
    DB_RECOVERY: int
    TABLE_REBUILD: int
    KILL_LOCK_PIDS: int
    STUCK_YUM: int
    CLEAN_YUM_TRANSACTIONS: int
    INDEX_REBUILD: int
    KILL_DB001_PIDS: int

class Result:

    OK: int
    FAILED: int

# Human readable names for different cleanup actions.
ACTION_NAMES: t.Dict[int, str]

# pyre-ignore[2,3]: workaround pyre bug
def memoize(
    f: t.Callable[..., t.TypeVar("RT")]
) -> t.Callable[..., t.TypeVar("RT")]: ...
def alarm_handler(signum: int, frame: FrameType) -> None: ...
def call_with_timeout(
    func,  # type: t.Callable[..., t.TypeVar("RT")]
    timeout,  # type: int
    args=None,  # type: t.Optional[t.Iterable[str]]
    # pyre-ignore[2]: kwargs has type dict[str, Any]
    kwargs=None,  # type: t.Optional[t.Dict[str, t.Any]]
) -> t.TypeVar("RT"): ...
def run_with_timeout(
    cmd: t.Sequence[str],
    timeout: int,  # type: int
    raise_on_nonzero: bool = True,
    raise_on_timeout: bool = True,
    exception_to_raise: t.Type[Exception] = DcRPMException,
) -> CompletedProcess: ...
def kindly_end(proc: subprocess.Popen, timeout: int = END_TIMEOUT) -> int: ...
@memoize
def which(cmd: str) -> str: ...
@memoize
def read_os_name(): ...
@memoize
def read_os_release() -> Dict[str, str]: ...
