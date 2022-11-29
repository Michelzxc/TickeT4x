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
import tkinter as tk
import customtkinter as ctk

from app import system_, loaders, refactor
from ui.widgets import menus

__version__ = "0.1.2"
__date__ = "2022-11-28"
# -----------------------------------------------------------------------


class TickeT4x(ctk.CTk):

    def __init__(self, *args,
                 app_version=None,
                 **kwargs):

        super().__init__(*args, **kwargs)

        self.app_version = app_version

        self.global_font = "Roboto"
        self.text = None  # Application Texts
        self.images = None  # Application Images
        self.colors = None  # Hex colors, is dict of dict

        self.geometry("870x520")
        self.minsize(500, 400)

        self.data_loader()  # Load Application Data
        self.set_theme()

        # ==================== Frame Instances ==========================
        self.main_menu_frame = menus.MainMenu(
            master=self,
            font=self.global_font
        )

        # =============== Configuration and location ====================
        self.set_frames_content()
        self.set_grid()

    def set_theme(self) -> None:
        """Set appearance mode, colors, global font and root atributes."""

        # Appearance and color
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Root attributes
        self.title(self.text["NAME_APPLICATION"])
        self.iconphoto(False, self.images["app_logo"])

    def data_loader(self) -> None:
        """Get data of json files."""

        # ======================= Text Load =============================
        self.text = loaders.text_loader(
            file="json_/texts.json",
            lang="es"
        )

        # ====================== Image Load =============================
        self.images = {}
        images = loaders.image_loader(
            file="json_/images.json"
        )

        for k, v in images.items():
            self.images[k] = tk.PhotoImage(
                file=v["path"]
            ).subsample(
                x=v["size"],
                y=v["size"]
            )

        # ====================== Color Load =============================
        self.colors = loaders.color_loader(
            file="json_/colors.json"
        )

    def set_grid(self):
        """Set grid of widgets."""

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.main_menu_frame.grid(
            row=0, column=0,
            sticky="ns"
        )

    def set_frames_content(self):
        """Set texts, colors, images and commands in frames widgets."""

        # ==================== main_menu_frame ==========================
        self.main_menu_frame.title_label.configure(
            text=self.text["NAME_APPLICATION"]
        )
        self.main_menu_frame.new_registry_button.configure(
            text=self.text["NAME_NEWREG"]
        )
        self.main_menu_frame.configuration_button.configure(
            text=self.text["NAME_CONFIG"]
        )
        self.main_menu_frame.update_button.configure(
            text=self.text["NAME_UPDATE"]
        )
        self.main_menu_frame.about_button.configure(
            text=self.text["NAME_ABOUT"]
        )
        self.main_menu_frame.exit_button.configure(
            text=self.text["NAME_EXIT"],
            fg_color=self.colors["normal"]["red_01"],
            hover_color=self.colors["hover"]["red_01"],
            command=self.destroy
        )
        self.main_menu_frame.version_label.configure(
            text=self.app_version,
        )

    def load_protocols(self):
        """Set protocols for widgets."""

        pass


if __name__ == "__main__":
    system_.run_isplatform("win32", "linux")

    APP_VERSION = refactor.make_version(
        version=__version__,
        date=__date__
    )

    application = TickeT4x(
        app_version=APP_VERSION
    )
    application.mainloop()
