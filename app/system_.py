# Copyright 2022 Michael Da Rosa (micheldarosazxc@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------
"""Implements functions that refer to system."""

import sys


def run_isplatform(*args: str) -> None:
    """Close application if system platform not in input function."""

    for arg in args:
        if sys.platform.startswith(arg):
            print("platform is: [{}]".format(sys.platform))
            return None

    print("[{}] is incompatible system.".format(sys.platform))
    sys.exit()


def default_directories() -> dict:
    """Return default directories for platform."""

    if sys.platform.startswith("linux"):
        linux_dirs = {
            "dir_conf": "directorio usuario y .carpeta del programa",
            "dir_user": "directorio usuario y documentos"
        }

        return linux_dirs

    elif sys.platform.startswith("win32"):
        win32_dirs = {
            "dir_conf": "appdata/local/carpeta de programa",
            "dir_user": "directorio usuario y documentos"
        }

        return win32_dirs
