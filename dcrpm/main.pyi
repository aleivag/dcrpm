#!/usr/bin/env python
#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the GPLv2 license found in the LICENSE
# file in the root directory of this source tree.
#
# pyre-strict

import argparse

from typing import Dict, Any

DEFAULT_MAX_PASSES: int

DEFAULT_MIN_REQUIRED_FREE_SPACE: int

LOG_FORMAT: str
DEFAULT_LOGGING_CONFIG: Dict[str, Any]

def parse_args() -> argparse.Namespace: ...
def main() -> int: ...
