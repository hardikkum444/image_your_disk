from pathlib import Path
from pathlib import Path
import subprocess
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets3/frame0")

def center_window(window,height=600,width=500):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
center_window(window)
window.wm_iconname("Image your disk")
window.title("IYD Imaging Process")
im = Image.open('assets0/favicon.ico')
photo = ImageTk.PhotoImage(im)
window.wm_iconphoto(True, photo)
window.wm_iconname("IYD")
window.geometry("600x500")
window.configure(bg = "#545252")

canvas = Canvas(
    window,
    bg = "#545252",
    height = 500,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    124.0,
    455.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_1.place(
    x=0.0,
    y=0.0,
    width=271.0,
    height=500.0
)

selected_format = StringVar()

def on_checkbox_click():
    if raw_var.get() == 1 and dd_var.get() == 0:
        selected_format.set("RAW")
    elif dd_var.get() == 1 and raw_var.get() == 0:
        selected_format.set("DD")
    else:
        messagebox.showwarning("Warning", "Please Select 1 Option!")
    # print(f"Selected format: {selected_format.get()}")


# Variables for checkbuttons
raw_var = IntVar()
dd_var = IntVar()

checkbutton_raw = Checkbutton(
    window,
    text="RAW",
    variable=raw_var,
    onvalue=1,
    offvalue=0,
    width=8,
    command=on_checkbox_click,
    bg="#D9D9D9",
    font=("Arial", 12),
    relief="raised",
    padx=10,
    pady=5,

)
checkbutton_raw.place(x=377, y=189)

checkbutton_dd = Checkbutton(
    window,
    text="DD",
    variable=dd_var,
    onvalue=1,
    width=8,
    offvalue=0,
    command=on_checkbox_click,
    bg="#D9D9D9",
    font=("Arial", 12),
    relief="raised",
    padx=10,
    pady=5,
)
checkbutton_dd.place(x=377, y=83)
def on_next_click():
    if dd_var.get() == 0 and raw_var.get() == 0:
        messagebox.showwarning("Warning", "Please Select 1 Option!")
    elif dd_var.get() == 1 and raw_var.get() == 1:
        messagebox.showwarning("Warning", "Please Select Only 1 Option!")
    else:
        window.destroy()
        import sys
        # sys.path.append("build")
        import gui4

def on_back_click():
    window.destroy()
    import sys
    # sys.path.append("build")
    # import gui2
    # subprocess.run(["python3", "gui2.py"])
    subprocess.run(["sudo", "myenv/bin/python3", "gui2.py"])


next_button = Button(window, text="Next", command=on_next_click, width=10, bg="#333333", fg="white")
next_button.place(x=452, y=389)

back_button = Button(window, text="Back", command=on_back_click, width=10, bg="#333333", fg="white")
back_button.place(x=312, y=389)

window.resizable(False, False)
window.mainloop()
