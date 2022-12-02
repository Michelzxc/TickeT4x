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
import customtkinter as ctk


class ConfigurationFrame(ctk.CTkFrame):
    def __init__(self, *args,
                 font: str | None,
                 transparent_frame=True,
                 **kwargs):

        super().__init__(*args, **kwargs)

        # ==================== frame configuration ======================

        self.corner_radius_frames = 0

        if transparent_frame:
            self.configure(
                fg_color=self.master.cget("fg_color")
            )

        self.configure(
            corner_radius=self.corner_radius_frames
        )

        # =================== widget configuration ======================

        self.font = font

        # ======================= make widgets ==========================

        self.directories_frame = ctk.CTkFrame(
            master=self,
            corner_radius=self.corner_radius_frames
        )

        self.values_frame = ctk.CTkFrame(
            master=self,
            corner_radius=self.corner_radius_frames
        )

        self.buttons_frames = ctk.CTkFrame(
            master=self,
            corner_radius=self.corner_radius_frames
        )

        # ===============================================================

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, minsize=10)
        self.grid_rowconfigure(2, minsize=10)
        self.grid_rowconfigure(4, minsize=10)
        self.grid_rowconfigure(6, minsize=10)
        self.directories_frame.grid(
            row=1, column=0,
            padx=10,
            sticky="ew"
        )
        self.values_frame.grid(
            row=3, column=0,
            padx=10,
            sticky="ew"
        )
        self.buttons_frames.grid(
            row=5, column=0,
            padx=10,
            sticky="ew"
        )
