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


def text_loader(file: str, lang: str) -> tuple:
    """Load text entries from json file and global font type."""

    with open(file, "rt") as json_file:
        json_content = json.load(json_file)

    lang_text = json_content["lang"].get(lang)

    if lang_text is None:
        lang_text = json_content["es"]  # Default

    font = json_content["font"]

    return lang_text, font


def image_loader(file: str) -> dict:
    """Load path images of widgets from json file."""

    with open(file, "rt") as json_file:
        json_content = json.load(json_file)

    widget_images = json_content["images"]

    return widget_images


def color_loader(file: str) -> dict:
    """Load name and hex color from colors.json."""

    with open(file, "rt") as json_file:
        json_content = json.load(json_file)

    color_blocks = json_content["hex_colors"]

    return color_blocks
