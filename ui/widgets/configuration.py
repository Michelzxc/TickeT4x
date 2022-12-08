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
                 transparent_frame=False,
                 color_separator="#000000",
                 color_enlb="#ffffff",
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

        self.color_separator = color_separator
        self.color_enlb = color_enlb
        self.font = font
        self.font_size = 14
        self.height_ = 8
        self.width_ = 80
        self.button_height = 40
        self.button_width = 150
        self.values_width = 60
        self.row_separator_size = 5
        self.col_separator_size = 5

        # ======================= make widgets ==========================
        # frames
        self.directories_frame = ctk.CTkFrame(
            master=self,
            corner_radius=self.corner_radius_frames,
            fg_color=self.color_separator
        )

        self.values_frame = ctk.CTkFrame(
            master=self,
            corner_radius=self.corner_radius_frames,
            fg_color=self.color_separator
        )

        self.buttons_frames = ctk.CTkFrame(
            master=self,
            corner_radius=self.corner_radius_frames,
            fg_color=self.cget("fg_color")
        )

        # directories_frame content
        self.label_dir_conf = ctk.CTkLabel(
            master=self.directories_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.entry_dir_conf = ctk.CTkEntry(
            master=self.directories_frame,
            font=(self.font, self.font_size, "italic"),
            # justify="center",
            height=self.height_,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )
        self.label_dir_usr = ctk.CTkLabel(
            master=self.directories_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.entry_dir_usr = ctk.CTkEntry(
            master=self.directories_frame,
            font=(self.font, self.font_size, "italic"),
            # justify="center",
            height=self.height_,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )

        # values_frame content
        self.label_diurn_flag = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_nightly_flag = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_diurn_token = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_nightly_token = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_salary_chunk = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_apport_chunk = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )

        self.entry_diurn_flag = ctk.CTkEntry(
            master=self.values_frame,
            font=(self.font, self.font_size, "italic"),
            justify="right",
            height=self.height_,
            width=self.values_width,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )
        self.entry_nightly_flag = ctk.CTkEntry(
            master=self.values_frame,
            font=(self.font, self.font_size, "italic"),
            justify="right",
            height=self.height_,
            width=self.values_width,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )
        self.entry_diurn_token = ctk.CTkEntry(
            master=self.values_frame,
            font=(self.font, self.font_size, "italic"),
            justify="right",
            height=self.height_,
            width=self.values_width,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )
        self.entry_nightly_token = ctk.CTkEntry(
            master=self.values_frame,
            font=(self.font, self.font_size, "italic"),
            justify="right",
            height=self.height_,
            width=self.values_width,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )
        self.entry_salary_chunk = ctk.CTkEntry(
            master=self.values_frame,
            font=(self.font, self.font_size, "italic"),
            justify="right",
            height=self.height_,
            width=self.values_width,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )
        self.entry_apport_chunk = ctk.CTkEntry(
            master=self.values_frame,
            font=(self.font, self.font_size, "italic"),
            justify="right",
            height=self.height_,
            width=self.values_width,
            fg_color=self.color_enlb,
            border_width=0,
            corner_radius=0
        )

        self.label_diurn_flag_unit = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_nightly_flag_unit = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_diurn_token_unit = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_nightly_token_unit = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_salary_chunk_unit = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )
        self.label_apport_chunk_unit = ctk.CTkLabel(
            master=self.values_frame,
            font=(self.font, self.font_size),
            width=self.width_,
            fg_color=self.color_enlb
        )

        # buttons_frames content
        self.apply = ctk.CTkButton(
            master=self.buttons_frames,
            font=(self.font, 16),
            height=self.button_height,
            width=self.button_width,
            corner_radius=0,
            border_width=0,
            border_color=self.color_separator
        )
        self.exit = ctk.CTkButton(
            master=self.buttons_frames,
            font=(self.font, 16),
            height=self.button_height,
            width=self.button_width,
            corner_radius=0,
            border_width=0,
            border_color=self.color_separator
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

        self.directories_frame.grid_columnconfigure(3, weight=1)
        self.directories_frame.grid_columnconfigure(
            0, minsize=self.col_separator_size
        )
        # self.directories_frame.grid_columnconfigure(
        #     2, minsize=self.col_separator_size
        # )
        self.directories_frame.grid_columnconfigure(
            4, minsize=self.col_separator_size
        )
        self.directories_frame.grid_rowconfigure(
            0, minsize=self.row_separator_size
        )
        self.directories_frame.grid_rowconfigure(
            2, minsize=self.row_separator_size
        )
        self.directories_frame.grid_rowconfigure(
            4, minsize=self.row_separator_size
        )
        self.label_dir_conf.grid(
            row=1, column=1,
            sticky="nsew"
        )
        self.entry_dir_conf.grid(
            row=1, column=3,
            sticky="nsew"
        )
        self.label_dir_usr.grid(
            row=3, column=1,
            sticky="nsew"
        )
        self.entry_dir_usr.grid(
            row=3, column=3,
            sticky="nsew"
        )

        self.values_frame.grid_rowconfigure(
            0, minsize=self.row_separator_size
        )
        self.values_frame.grid_rowconfigure(
            2, minsize=self.row_separator_size
        )
        self.values_frame.grid_rowconfigure(
            4, minsize=self.row_separator_size
        )
        self.values_frame.grid_rowconfigure(
            6, minsize=self.row_separator_size
        )
        self.values_frame.grid_columnconfigure(
            0, minsize=self.col_separator_size
        )
        # self.values_frame.grid_columnconfigure(
        #     2, minsize=self.col_separator_size
        # )
        self.values_frame.grid_columnconfigure(
            4, minsize=self.col_separator_size
        )
        self.values_frame.grid_columnconfigure(
            6, minsize=self.col_separator_size + 5
        )
        # self.values_frame.grid_columnconfigure(
        #     8, minsize=self.col_separator_size
        # )
        self.values_frame.grid_columnconfigure(
            10, minsize=self.col_separator_size
        )
        self.values_frame.grid_columnconfigure(
            12, minsize=self.col_separator_size
        )

        self.label_diurn_flag.grid(
            row=1, column=1,
            sticky="nsew"
        )
        self.entry_diurn_flag.grid(
            row=1, column=3,
            sticky="nsew"
        )
        self.label_diurn_flag_unit.grid(
            row=1, column=5,
            sticky="nsew"
        )
        self.label_nightly_flag.grid(
            row=3, column=1,
            sticky="nsew"
        )
        self.entry_nightly_flag.grid(
            row=3, column=3,
            sticky="nsew"
        )
        self.label_nightly_flag_unit.grid(
            row=3, column=5,
            sticky="nsew"
        )
        self.label_diurn_token.grid(
            row=1, column=7,
            sticky="nsew"
        )
        self.entry_diurn_token.grid(
            row=1, column=9,
            sticky="nsew"
        )
        self.label_diurn_token_unit.grid(
            row=1, column=11,
            sticky="nsew"
        )
        self.label_nightly_token.grid(
            row=3, column=7,
            sticky="nsew"
        )
        self.entry_nightly_token.grid(
            row=3, column=9,
            sticky="nsew"
        )
        self.label_nightly_token_unit.grid(
            row=3, column=11,
            sticky="nsew"
        )

        self.label_salary_chunk.grid(
            row=5, column=1,
            sticky="nsew"
        )
        self.entry_salary_chunk.grid(
            row=5, column=3,
            sticky="nsew"
        )
        self.label_salary_chunk_unit.grid(
            row=5, column=5,
            sticky="nsew"
        )
        self.label_apport_chunk.grid(
            row=5, column=7,
            sticky="nsew"
        )
        self.entry_apport_chunk.grid(
            row=5, column=9,
            sticky="nsew"
        )
        self.label_apport_chunk_unit.grid(
            row=5, column=11,
            sticky="nsew"
        )

        self.buttons_frames.grid_columnconfigure(
            1, weight=1
        )
        self.apply.grid(
            row=0, column=0,
            padx=0, pady=2,
            sticky="nsw"
        )
        self.exit.grid(
            row=0, column=2,
            padx=0, pady=2,
            sticky="nse"
        )
