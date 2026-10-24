from tkinter import *
from tkinter import messagebox

from lab_controller.calc_controller import CalcController
from optics_tools.validation import Validator
from lab_view import theme


class CalcView:
    def __init__(self, parent):
        self.controller = CalcController()

        self.win = Toplevel(parent)
        self.win.geometry("400x420")
        self.win.title("Optical Calculations")
        self.win.configure(bg=theme.BG)

        theme.make_label(self.win, "Diffraction / Interference", 20, 15, title=True)

        # Kind
        theme.make_label(self.win, "Type", 20, 70)
        self.kind = StringVar(value="Single Slit")
        theme.make_combo(self.win, self.kind, Validator.KINDS, 160, 70)

        # Wavelength
        theme.make_label(self.win, "Wavelength (nm)", 20, 110)
        self.wavelength = StringVar(value="632.8")
        theme.make_entry(self.win, self.wavelength, 160, 110)

        # Slit
        theme.make_label(self.win, "Slit Size (um)", 20, 150)
        self.size = StringVar()
        theme.make_entry(self.win, self.size, 160, 150)

        # Distance
        theme.make_label(self.win, "Screen Dist. (m)", 20, 190)
        self.distance = StringVar()
        theme.make_entry(self.win, self.distance, 160, 190)

        # Order
        theme.make_label(self.win, "Order (m)", 20, 230)
        self.order = StringVar(value="1")
        theme.make_entry(self.win, self.order, 160, 230)

        theme.make_button(self.win, "Calculate", self.calculate_click, 20, 280, width=20)

        # Result
        self.result = StringVar()
        Label(self.win, textvariable=self.result, bg=theme.WHITE, fg=theme.TEXT,
              font=theme.FONT, width=44, height=4, justify=LEFT,
              relief="solid", bd=1).place(x=20, y=325)

    # دکمه محاسبه فشرده شود
    def calculate_click(self):
        success, message = self.controller.calculate(
            self.kind.get(),
            self.wavelength.get(),
            self.size.get(),
            self.distance.get(),
            self.order.get()
        )

        if success:
            self.result.set(message)
        else:
            self.result.set("")
            messagebox.showerror("Error", message)
