import os
import tkinter as tk
from tkinter import font, messagebox, ttk
from tkinter.filedialog import askdirectory

from src.utils import convert_folder_img


class MyApp(tk.Tk):
    def __init__(self):
        super(MyApp, self).__init__()

        self.title("ConvertImg")
        self.geometry("600x200")
        self.resizable(width=False, height=False)
        file_dir = os.path.dirname(os.path.realpath(__file__))

        my_font = font.Font(root=None, size=24)

        self.l_title = ttk.Label(self, text="Convert Images", font=my_font)
        self.l_title.pack()

        self.frame = tk.Frame(self)
        self.frame.pack(pady=10)

        # Input Folder

        self.input_var = tk.StringVar(value=os.path.join(file_dir, "in"))

        self.l_input_folder = ttk.Label(self.frame, text="Input folder: ")
        self.l_input_folder.grid(column=0, row=0)
        self.e_input_folder = ttk.Entry(
            self.frame, width=50, textvariable=self.input_var
        )
        self.e_input_folder.grid(column=1, row=0)
        self.b_input_open_dir = ttk.Button(
            self.frame, text="Open Dir", command=self.open_directory_input
        )
        self.b_input_open_dir.grid(column=2, row=0, padx=(5, 0))

        # Output Folder

        self.output_var = tk.StringVar(value=os.path.join(file_dir, "out"))

        self.l_output_folder = ttk.Label(self.frame, text="Output folder: ")
        self.l_output_folder.grid(column=0, row=1)
        self.e_output_folder = ttk.Entry(
            self.frame, width=50, textvariable=self.output_var
        )
        self.e_output_folder.grid(column=1, row=1)
        self.b_out_open_dir = ttk.Button(
            self.frame, text="Open Dir", command=self.open_directory_out
        )
        self.b_out_open_dir.grid(column=2, row=1, padx=(5, 0))

        # Choose format

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        self.l_choose_format = ttk.Label(self.frame2, text="Choose the output format: ")
        self.l_choose_format.grid(column=0, row=0)

        formats_options = ["png", "jpeg", "webp", "tiff"]
        self.format_var = tk.StringVar(value=formats_options[0])
        self.cb_formats = ttk.Combobox(
            self.frame2,
            state="readonly",
            values=formats_options,
            width=5,
            textvariable=self.format_var,
        )
        self.cb_formats.grid(column=1, row=0)

        # Processing
        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.b_convert = ttk.Button(
            self.frame3, text="Convert", command=self.convert_image
        )
        self.b_convert.pack()

    def convert_image(self):
        input_dir = self.input_var.get()
        output_dir = self.output_var.get()
        out_format = self.format_var.get()
        try:
            convert_folder_img(
                input_folder=input_dir, output_dir=output_dir, format=out_format
            )
            messagebox.showinfo(
                title="Images converted",
                message="The images were converted to `{}` with the format `{}`".format(
                    output_dir, out_format
                ),
            )
        except SystemError as e:
            messagebox.showerror(title="Error", message=str(e))

    def open_directory_input(self):
        filename = askdirectory()
        self.input_var.set(value=filename)

    def open_directory_out(self):
        filename = askdirectory()
        self.output_var.set(value=filename)


if __name__ == "__main__":
    root = MyApp()
    root.mainloop()
