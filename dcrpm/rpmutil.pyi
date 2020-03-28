#!/usr/bin/env python
#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the GPLv2 license found in the LICENSE
# file in the root directory of this source tree.
#
# pyre-strict

from .util import CompletedProcess
from typing import Iterable, Callable, Dict, List, Sequence

RPM_CHECK_TIMEOUT_SEC: int
YUM_COMPLETE_TIMEOUT_SEC: int
VERIFY_TIMEOUT_SEC: int
RECOVER_TIMEOUT_SEC: int
REBUILD_TIMEOUT_SEC: int
MIN_ACCEPTABLE_PKG_COUNT: int

class RPMUtil:

    tables: List[str]
    def __init__(
        self,
        dbpath: str,
        rpm_path: str,
        recover_path: str,
        verify_path: str,
        stat_path: str,
        yum_complete_transaction_path: str,
        blacklist: List[str],
        forensic: bool,
    ) -> None: ...
    def populate_tables(self) -> None: ...
    def db_stat(self) -> None: ...
    def _poke_index(
        self, cmd: Sequence[str], checks: Iterable[Callable[[CompletedProcess], bool]],
    ) -> CompletedProcess: ...
    def check_rpmdb_indexes(self) -> None: ...
    def check_rpm_qa(self) -> None: ...
    def query(self, rpm_name: str) -> None: ...
    def recover_db(self) -> None: ...
    def rebuild_db(self) -> None: ...
    def check_tables(self) -> None: ...
    def verify_tables(self) -> None: ...
    def clean_yum_transactions(self) -> None: ...
    def kill_spinning_rpm_query_processes(
        self, kill_after_seconds: int, kill_timeout: int
    ) -> None: ...
    def _get_macros(self) -> Dict[str, str]: ...
    def get_db_backend(self) -> None: ...
