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
                 font: str,
                 **kwargs):

        super().__init__(*args, **kwargs)

        # =================== widget configuration ======================

        self.font = font
        self.corner_button = 0
        self.height_button = 40
        self.width_label = 50

        self.corner_radius = 0

        # ===================== Make components =========================

        self.title_label = ctk.CTkLabel(
            master=self,
            text_font=(self.font, 16)
        )

        self.version_label = ctk.CTkLabel(
            master=self,
            text_font=(self.font, -10),
            text="",
            width=self.width_label
        )

        self.new_registry_button = ctk.CTkButton(
            master=self,
            text_font=(self.font, 11),
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.update_button = ctk.CTkButton(
            master=self,
            text_font=(self.font, 12),
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.configuration_button = ctk.CTkButton(
            master=self,
            text_font=(self.font, 12),
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.about_button = ctk.CTkButton(
            master=self,
            text_font=(self.font, 12),
            height=self.height_button,
            corner_radius=self.corner_button
        )

        self.exit_button = ctk.CTkButton(
            master=self,
            text_font=(self.font, 14),
            height=self.height_button,
            corner_radius=self.corner_button
        )

        # ======================= Grid set ==============================

        # <<< COLUMN 0 >>>

        self.grid_rowconfigure(
            0, minsize=20
        )

        self.grid_rowconfigure(
            2, minsize=20
        )

        self.grid_rowconfigure(
            6, minsize=10,
            weight=1
        )

        self.grid_rowconfigure(
            8, minsize=10
        )

        self.grid_rowconfigure(
            10, minsize=30
        )

        self.title_label.grid(
            row=1, column=0,
            pady=10
        )

        self.new_registry_button.grid(
            row=3, column=0,
            padx=15, pady=5,
            sticky="ew"
        )

        self.update_button.grid(
            row=4, column=0,
            padx=15, pady=5,
            sticky="ew"
        )
        self.configuration_button.grid(
            row=5, column=0,
            padx=15, pady=5,
            sticky="ew"
        )

        self.about_button.grid(
            row=7, column=0,
            padx=15,
            sticky="ew"
        )

        self.exit_button.grid(
            row=9, column=0,
            padx=15,
            ipady=2,
            sticky="ew"
        )

        self.version_label.grid(
            row=11, column=0,
            padx=5,
            sticky="e"
        )
