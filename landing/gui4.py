from pathlib import Path
import threading
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, Label
import subprocess
import createim
import tkinter as tk
from tkinter import ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/man44/Documents/imager/landing/assets4/frame0")

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
window.title("IYD Imaging Process")
center_window(window)
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
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=271.0,
    y=43.0,
    width=329.0,
    height=319.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    271.0,
    500.0,
    fill="#212121",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    128.0,
    249.0,
    image=image_image_1
)

canvas.create_rectangle(
    302.0,
    83.0,
    528.0,
    118.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    302.0,
    268.0,
    529.0,
    303.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    302.0,
    173.0,
    528.0,
    208.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    428.0,
    100.0,
    image=entry_image_1
)

def browse_file1():
    file_path = filedialog.askopenfilename()
    if file_path:
        # entry_1.delete(0, Tk.END)  # Clear any existing text
        entry_1.insert(0, file_path)  # Insert the selected file path

def browse_file3():
    file_path = filedialog.askdirectory()
    if file_path:
        # entry_1.delete(0, Tk.END)  # Clear any existing text
        entry_3.insert(0, file_path)  # Insert the selected file path



browse_button = Button(window, text="BF",fg="white",width=2,bg="#333333", command=browse_file1)
browse_button.pack(pady=10)
browse_button.place(x=546, y=85)



browse_button2 = Button(window, text="BF",fg="white",width=2,bg="#333333", command=browse_file3)
browse_button2.pack(pady=10)
browse_button2.place(x=546, y=269)




entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=328.0,
    y=83.0,
    width=200.0,
    height=32.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    428.0,
    190.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=328.0,
    y=173.0,
    width=200.0,
    height=32.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    427.0,
    284.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=328.0,
    y=268.0,
    width=198.0,
    height=31.0
)

final_name = entry_2.get()+"/"+entry_3.get()

def main_win():
    def create_image_task():
            progress_bar.start(10)
            start, end, md5, sh1 = createim.create_image(entry_1.get(), final_name)
            progress_label.config(text="Completed!")
            progress_bar.stop()
            window.destroy()

    window = tk.Tk()
    window.title("IYD-Creating Image")
    center_window(window)
    window.geometry("300x150")

    style = ttk.Style()
    style.configure("TProgressbar", thickness=20)

    progress_label = Label(window, text="Progressing...", font=("Arial", 12))
    progress_label.pack(pady=10)

    progress_bar = ttk.Progressbar(window, style="TProgressbar", orient="horizontal", length=250, mode="indeterminate")
    progress_bar.pack(pady=20)

    threading.Thread(target=create_image_task).start()

    window.mainloop()

def on_next_click():
    print("Next button clicked")
    # createim.create_image(entry_1.get(),entry_2.get(),entry_2.get())
    main_win()

def on_back_click():
    window.destroy()
    import sys
    # sys.path.append("build")
    # import gui3
    subprocess.run(["python3", "gui3.py"])

next_button = Button(window, text="Next", command=on_next_click, width=10, bg="#333333", fg="white")
next_button.place(x=452, y=415)

back_button = Button(window, text="Back", command=on_back_click, width=10, bg="#333333", fg="white")
back_button.place(x=312, y=415)

window.resizable(False, False)
window.mainloop()