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

class ForensicLogger(logging.Handler):
    def __init__(self, logdir: str, level: int = logging.NOTSET) -> None: ...
    def debug(self, record: logging.LogRecord) -> None: ...
    def emit(self, record: logging.LogRecord) -> None: ...
