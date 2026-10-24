import tkinter as tk
from tkinter import ttk


BG = "#FFF0F5"
PINK = "#F8BBD0"
DARK_PINK = "#EC407A"
TEXT = "#5D2A42"
WHITE = "#FFFFFF"
FONT = ("Arial", 10)


def apply_style(win):
    win.configure(bg=BG)
    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("Treeview", background=WHITE, fieldbackground=WHITE,
                    foreground=TEXT, rowheight=26, font=FONT)
    style.configure("Treeview.Heading", background=PINK, foreground=TEXT,
                    font=("Arial", 10, "bold"), relief="flat")
    style.map("Treeview", background=[("selected", DARK_PINK)],
              foreground=[("selected", WHITE)])
    style.map("Treeview.Heading", background=[("active", PINK)])
    style.configure("TCombobox", fieldbackground=WHITE, background=PINK, foreground=TEXT)


def make_label(win, text, x, y, title=False):
    font = ("Arial", 16, "bold") if title else FONT
    color = DARK_PINK if title else TEXT
    label = tk.Label(win, text=text, bg=BG, fg=color, font=font)
    label.place(x=x, y=y)
    return label


def make_entry(win, variable, x, y, width=18):
    entry = tk.Entry(win, textvariable=variable, width=width, bg=WHITE, fg=TEXT,
                     relief="solid", bd=1, font=FONT)
    entry.place(x=x, y=y)
    return entry


def make_combo(win, variable, values, x, y, width=16, before_open=None):
    combo = ttk.Combobox(win, textvariable=variable, values=values,
                         state="readonly", width=width)
    if before_open is not None:
        combo.configure(postcommand=before_open)
    combo.place(x=x, y=y)
    return combo


def make_button(win, text, command, x, y, width=14):
    button = tk.Button(win, text=text, command=command, width=width, bg=DARK_PINK,
                       fg=WHITE, activebackground=PINK, activeforeground=TEXT,
                       relief="flat", font=("Arial", 10, "bold"), cursor="hand2")
    button.place(x=x, y=y)
    return button
