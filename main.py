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
from app import system_, refactor
from ui_object import UserInterface

__version__ = "0.3.0"
__date__ = "2022-12-07"

ALLOW_DEBUG = False  # Enable checkout tools


def main():
    app_version = refactor.make_version(
        version=__version__,
        date=__date__
    )

    application = UserInterface(
        app_version=app_version
    )

    return application


if __name__ == "__main__":
    system_.run_isplatform("win32", "linux")

    # ======================= Testing Block =============================
    if ALLOW_DEBUG:
        try:
            import __debug as debug
            debug.test_a1()
            debug.check_date_version(
                date=__date__,
                version=__version__
            )

        except ImportError:
            print("_debug module is not available, "
                  "debug process aborted.")
            print("Application is run.\n")

    # ======================= Main Application ==========================
    main().mainloop()
