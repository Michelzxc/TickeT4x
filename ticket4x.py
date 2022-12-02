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
from PIL import Image
import tkinter as tk
import customtkinter as ctk

from app import system_, loaders, refactor
from ui.widgets import menus, information, configuration

__version__ = "0.2.1"
__date__ = "2022-12-02"

SOURCE_CODE = "https://github.com/Michelzxc/TickeT4x"

ALLOW_DEBUG = False  # Enable checkout tools
# -----------------------------------------------------------------------


class TickeT4x(ctk.CTk):

    def __init__(self, *args,
                 app_version=None,
                 **kwargs):

        super().__init__(*args, **kwargs)

        self.app_version = app_version

        self.text_font = None
        self.text = None  # Application Texts
        self.images = None  # Application Images in PhotoImage
        self.pathsize_images = None  # Raw path and size dictionary
        self.colors = None  # Hex colors, is dict of dict

        self.geometry("870x520")
        self.minsize(500, 400)

        self.data_loader()  # Load Application Data
        self.set_theme()

        # ==================== main_menu_frame ==========================

        # Frame Instance
        self.main_menu_frame = menus.MainMenu(
            master=self,
            font=self.text_font
        )

        # Frame Inject Contents
        self.main_menu_frame.title_label.configure(
            text=self.text["NAME_APPLICATION"]
        )
        self.main_menu_frame.new_registry_button.configure(
            text=self.text["NAME_NEWREG"],
            fg_color=self.colors["normal"]["light_blue_01"],
            hover_color=self.colors["hover"]["light_blue_01"]
        )
        self.main_menu_frame.configuration_button.configure(
            text=self.text["NAME_CONFIG"],
            fg_color=self.colors["normal"]["light_blue_01"],
            hover_color=self.colors["hover"]["light_blue_01"],
            command=self.toplevel_mainconfiguration
        )
        self.main_menu_frame.update_button.configure(
            text=self.text["NAME_UPDATE"],
            fg_color=self.colors["normal"]["light_blue_01"],
            hover_color=self.colors["hover"]["light_blue_01"]
        )
        self.main_menu_frame.about_button.configure(
            text=self.text["NAME_ABOUT"],
            fg_color=self.colors["normal"]["light_blue_01"],
            hover_color=self.colors["hover"]["light_blue_01"],
            command=self.toplevel_about
        )
        self.main_menu_frame.exit_button.configure(
            text=self.text["NAME_EXIT"],
            fg_color=self.colors["normal"]["red_03"],
            hover_color=self.colors["hover"]["red_03"],
            command=self.destroy
        )
        self.main_menu_frame.version_label.configure(
            text=self.app_version
        )

        # Grid Set
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.main_menu_frame.grid(
            row=0, column=0,
            sticky="ns"
        )

    def data_loader(self) -> None:
        """Get data of json files."""

        # ======================= Text Load =============================

        self.text, self.text_font = loaders.text_loader(
            file="json_/texts.json",
            lang="es"
        )

        # ====================== Image Load =============================

        self.images = {}
        images = loaders.image_loader(
            file="json_/images.json"
        )

        self.pathsize_images = images.copy()

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

    def set_theme(self) -> None:
        """Set appearance mode, colors, global font and root atributes."""

        # Appearance and color
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Root attributes
        self.title(self.text["NAME_APPLICATION"])
        self.iconphoto(False, self.images["app_logo_title"])

    def toplevel_mainconfiguration(self):
        """Create CTkTopLevel for configuration frame."""

        window_config = ctk.CTkToplevel(self)
        window_config.title(self.text["NAME_CONFIG"])
        window_config.iconphoto(False, self.images["settings_title"])

        configuration_frame = configuration.ConfigurationFrame(
            master=window_config,
            font=self.text_font
        )

        configuration_frame.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )

    def toplevel_about(self):
        """Create a CTkTopLevel for about frame."""

        window_about = ctk.CTkToplevel(self)
        window_about.title(self.text["NAME_ABOUT"])
        window_about.iconphoto(False, self.images["info_about_title"])

        # Frame Instance
        about_frame = information.AboutFrame(
            master=window_about,
            font=self.text_font
        )

        # Frame Inject Contents
        about_frame.app_logo.configure(
            image=ctk.CTkImage(
                dark_image=Image.open(
                    self.pathsize_images["app_logo_about"]["path"]
                ),
                size=(
                    self.pathsize_images["app_logo_about"]["size"],
                    self.pathsize_images["app_logo_about"]["size"]
                )
            )
        )
        about_frame.app_name.configure(
            text=self.text["NAME_APPLICATION"]
        )
        about_frame.description.configure(
            text=self.text["DESC_APP"]
        )
        about_frame.version.configure(
            text=__version__
        )
        about_frame.source.configure(
            text=SOURCE_CODE
        )
        about_frame.licence.configure(
            text=self.text["NAME_LICENCE"],
            fg_color=self.colors["normal"]["light_blue_01"],
            hover_color=self.colors["hover"]["light_blue_01"],
            command=self.toplevel_license
        )
        about_frame.exit.configure(
            text=self.text["NAME_CLOSE"],
            fg_color=self.colors["normal"]["red_03"],
            hover_color=self.colors["hover"]["red_03"],
            command=window_about.destroy
        )

        # Grid Set
        about_frame.grid(
            row=0,
            column=0,
            padx=12,
            pady=12
        )

    def toplevel_license(self):
        """Create CTkTopLevel to see License."""

        window_license = ctk.CTkToplevel(self)
        window_license.title(self.text["NAME_LICENCE"])
        window_license.iconphoto(False, self.images["apache_license_title"])

        window_license.geometry("600x600")

        license_text = ctk.CTkTextbox(
            master=window_license,
            corner_radius=0,
            font=(self.text_font, 14)
        )

        try:
            with open("LICENSE") as license_file:
                raw = -1
                for line in license_file:
                    raw += 1
                    str_raw = "%d.0" % raw
                    license_text.insert(index=str_raw, text=line)

        except FileNotFoundError:
            print("LICENSE file is not found.")

        window_license.grid_rowconfigure(0, weight=1)
        window_license.grid_columnconfigure(0, weight=1)

        license_text.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )

        license_text.configure(state="disabled")


if __name__ == "__main__":
    system_.run_isplatform("win32", "linux")

    # ======================= Testing Block =============================
    if ALLOW_DEBUG:
        try:
            import __debug as debug
            debug.test_a1()
            debug.check_date_version(
                date=__date__,
                version=__version__
            )

        except ImportError:
            print("_debug module is not available, "
                  "debug process aborted.")
            print("Application is run.\n")
    # ===================================================================

    APP_VERSION = refactor.make_version(
        version=__version__,
        date=__date__
    )
    # ======================= Main Application ==========================
    application = TickeT4x(
        app_version=APP_VERSION
    )

    application.mainloop()
