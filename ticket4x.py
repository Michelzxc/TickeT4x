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
from app.system_ import run_isplatform
# from app.refactor import make_version
# from app.loaders import text_loader

__version__ = "0.1.1"
__date__ = "2022-11-28"


def main() -> None:
    """TickeT4x main execute function."""


if __name__ == "__main__":
    run_isplatform("win32", "linux")
    main()
