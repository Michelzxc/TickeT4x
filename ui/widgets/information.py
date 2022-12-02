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
"""Contain CTKFrames for Information purposes."""

import customtkinter as ctk


class AboutFrame(ctk.CTkFrame):

    def __init__(self, *args,
                 font: str | None,
                 **kwargs):

        super().__init__(*args, **kwargs)

        # ==================== frame configuration ======================

        self.configure(
            corner_radius=0
        )

        # =================== widget configuration ======================

        self.font = font
        self.frame_color = self.cget("fg_color")

        # ======================= make widgets ==========================

        self.app_logo = ctk.CTkButton(
            master=self,
            corner_radius=0,
            fg_color=self.frame_color,
            border_width=0,
            text="",
            state="disabled"
        )

        self.app_name = ctk.CTkLabel(
            master=self,
            font=(self.font, 20, "bold")
        )

        self.version = ctk.CTkLabel(
            master=self,
            font=(self.font, 14)
        )

        self.description = ctk.CTkLabel(
            master=self,
            font=(self.font, 12)
        )

        self.source = ctk.CTkLabel(
            master=self,
            font=(self.font, 10, "italic")
        )

        self.licence = ctk.CTkButton(
            master=self,
            corner_radius=0,
            width=70,
            border_width=0
        )

        self.exit = ctk.CTkButton(
            master=self,
            corner_radius=0,
            width=70,
            border_width=0
        )

        # ======================== grid set =============================

        self.app_logo.grid(
            row=1, column=0,
            columnspan=2,
            padx=50, pady=25
        )

        self.app_name.grid(
            row=3, column=0,
            columnspan=2,
            sticky="ew"
        )

        self.description.grid(
            row=7, column=0,
            columnspan=2,
        )

        self.version.grid(
            row=5, column=0,
            columnspan=2,
            sticky="ew"
        )

        self.source.grid(
            row=9, column=0,
            columnspan=2,
            sticky="ew"
        )

        self.licence.grid(
            row=11, column=0,
            padx=10, pady=10,
            sticky="w"
        )

        self.exit.grid(
            row=11, column=1,
            padx=10, pady=10,
            sticky="e"
        )
