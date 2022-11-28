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
"""Defines functions that load external data."""

import json


def text_loader(file: str, lang: str) -> dict:
    """Load text entries from json file."""

    with open(file, "rt") as json_file:
        json_content = json.load(json_file)

    lang_text = json_content["lang"].get(lang)

    if lang_text is None:
        lang_text = json_content["es"]  # Default

    return lang_text
