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
"""Contain CTkFrame objects that defines menus."""

import customtkinter as ctk


class MainMenu(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 font: str | None,
                 **kwargs):

        super().__init__(*args, **kwargs)

        # ==================== frame configuration ======================

        self.configure(
            corner_radius=0
        )

        # =================== widget configuration ======================

        self.font = font
        self.corner_button = 0
        self.width_button = 200
        self.height_button = 50
        self.corner_radius = 0
        self.button_sep_row = 15
        self.button_sep_col = 15

        # ======================= make widgets ==========================

        self.new_registry_button = ctk.CTkButton(
            master=self,
            font=(self.font, 14),
            width=self.width_button,
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.update_button = ctk.CTkButton(
            master=self,
            font=(self.font, 14),
            width=self.width_button,
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.configuration_button = ctk.CTkButton(
            master=self,
            font=(self.font, 14),
            width=self.width_button,
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.about_button = ctk.CTkButton(
            master=self,
            font=(self.font, 14),
            width=self.width_button,
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.exit_button = ctk.CTkButton(
            master=self,
            font=(self.font, 14),
            width=self.width_button,
            height=self.height_button,
            corner_radius=self.corner_button
        )

        # ===============================================================

        self._set_grid()

    def _set_grid(self):
        # <<< COLUMN 0 >>>

        self.grid_rowconfigure(
            0, minsize=self.button_sep_row,
            weight=1
        )
        self.grid_rowconfigure(
            2, minsize=self.button_sep_row,
            weight=1
        )
        self.grid_rowconfigure(
            4, minsize=self.button_sep_row,
            weight=1
        )
        self.grid_columnconfigure(
            0, minsize=self.button_sep_col,
            weight=1
        )
        self.grid_columnconfigure(
            2, minsize=self.button_sep_col,
            weight=1
        )
        self.grid_columnconfigure(
            4, minsize=self.button_sep_col,
            weight=1
        )
        self.grid_columnconfigure(
            6, minsize=self.button_sep_col,
            weight=1
        )

        self.new_registry_button.grid(
            row=1, column=1,
            sticky="nsew"
        )

        # self.update_button.grid(
        #     row=1, column=3,
        #     sticky="nsew"
        # )
        self.configuration_button.grid(
            row=1, column=3,
            sticky="nsew"
        )

        self.about_button.grid(
            row=1, column=5,
            sticky="nsew"
        )

        self.exit_button.grid(
            row=3, column=5,
            sticky="nsew"
        )
