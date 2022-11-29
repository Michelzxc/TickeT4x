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
"""Defines functions to refactor data."""


def make_version(version, date, *args) -> str:
    """Create new string in fotmat: {yyyymmdd}-{version}:[others].

    All input parameters in type String, version is vx.y.z and date in
    format standard yyyy/mm/dd or yyyy-mm-dd or yyyymmdd.
    """

    if "/" in date:
        std_date = date.replace("/", "")

    elif "-" in date:
        std_date = date.replace("-", "")

    else:
        std_date = date[:]

    if len(args) == 0:
        output = "{}-v{}".format(std_date, version)
    else:
        output = "{}-v{}:".format(std_date, version)
        for arg in args:
            output += "{}".format(arg)

    return output
