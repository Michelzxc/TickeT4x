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

from app.system_ import run_isplatform
from app import loaders

__version__ = "0.1.2"
__date__ = "2022-11-28"
# -----------------------------------------------------------------------


class TickeT4x(object):
    def __init__(self):
        self.root = ctk.CTk()

        self.global_font = None
        self.text = None  # Application Texts
        self.images = None  # Application Images

        self.root.geometry("870x520")
        self.root.minsize(500, 400)

        self.data_loader()  # Load Application Data
        self.set_theme()

    def set_theme(self) -> None:
        """Set appearance mode, colors, global font and root atributes."""

        # Appearance and color
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Root attributes
        self.root.title(self.text["NAME_APPLICATION"])
        self.root.iconphoto(False, self.images["app_logo"])

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

    def set_grid(self):
        """Set grid of widgets."""

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


# -----------------------------------------------------------------------
if __name__ == "__main__":
    run_isplatform("win32", "linux")

    application = TickeT4x()
    application.root.mainloop()
