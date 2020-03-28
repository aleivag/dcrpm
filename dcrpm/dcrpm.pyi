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
from .rpmutil import RPMUtil
import argparse

class DcRPM:
    YUM_PATH: str
    YUM_TRANSACTION_BASE: str
    def __init__(self, rpmutil: RPMUtil, args: argparse.Namespace) -> None:
        self.rpmutil: RPMUtil
        self.args: argparse.Namespace
        self.logger: logging.Logger
        self.status_logger: logging.Logger
    def run(self) -> bool: ...
    def run_recovery(self) -> None: ...
    def run_rebuild(self) -> None: ...
    def hardlink_db001(self) -> str: ...
    def stale_yum_transactions_exist(self) -> bool: ...
    def has_free_disk_space(self) -> bool: ...
    def call_verify_tables(self) -> bool: ...
