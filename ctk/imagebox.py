from tkinter import PhotoImage
from customtkinter import CTkButton


class NCTkImageBox(CTkButton):
    """Allow draw image and resize."""

    def __init__(self, *args,
                 master,
                 width: int = 0,
                 height: int = 0,
                 size: int = None,
                 image: PhotoImage,
                 **kwargs):

        self.image = image
        if size is not None and size > 0:
            self.image = self.image.subsample(size, size)

        super().__init__(*args, master=master,
                         width=width, height=height,
                         image=self.image, compound="left",
                         text="", fg_color=None, hover=False,
                         **kwargs)
