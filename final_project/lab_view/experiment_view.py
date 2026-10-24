from tkinter import *
from tkinter import ttk, messagebox

from lab_controller.experiment_controller import ExperimentController
from optics_tools.validation import Validator
from lab_view import theme


class ExperimentView:
    def __init__(self, parent):
        self.controller = ExperimentController()

        self.win = Toplevel(parent)
        self.win.geometry("930x400")
        self.win.title("Experiments")
        self.win.configure(bg=theme.BG)

        # ExperimentID
        theme.make_label(self.win, "Experiment Id", 20, 20)
        self.experiment_id = StringVar()
        theme.make_entry(self.win, self.experiment_id, 130, 20)

        # Laser
        theme.make_label(self.win, "Laser", 20, 60)
        self.laser = StringVar()
        self.laser_combo = theme.make_combo(self.win, self.laser, [], 130, 60,
                                            before_open=self.load_lasers)

        # Kind
        theme.make_label(self.win, "Type", 20, 100)
        self.kind = StringVar()
        theme.make_combo(self.win, self.kind, Validator.KINDS, 130, 100)

        # Slit
        theme.make_label(self.win, "Slit Size (um)", 20, 140)
        self.slit = StringVar()
        theme.make_entry(self.win, self.slit, 130, 140)
        theme.make_label(self.win, "width a / distance d", 130, 165)

        # Distance
        theme.make_label(self.win, "Screen Dist. (m)", 20, 200)
        self.distance = StringVar()
        theme.make_entry(self.win, self.distance, 130, 200)

        # Order
        theme.make_label(self.win, "Order (m)", 20, 240)
        self.order = StringVar()
        theme.make_entry(self.win, self.order, 130, 240)

        # جدول
        self.table = ttk.Treeview(self.win, show="headings", height=12,
                                  columns=("id", "laser", "type", "slit", "dist", "order", "result", "date"))
        self.table.place(x=300, y=20)

        self.table.column("id", width=40)
        self.table.column("laser", width=120)
        self.table.column("type", width=90)
        self.table.column("slit", width=70)
        self.table.column("dist", width=70)
        self.table.column("order", width=45)
        self.table.column("result", width=90)
        self.table.column("date", width=90)

        self.table.heading("id", text="Id")
        self.table.heading("laser", text="Laser")
        self.table.heading("type", text="Type")
        self.table.heading("slit", text="Slit (um)")
        self.table.heading("dist", text="L (m)")
        self.table.heading("order", text="m")
        self.table.heading("result", text="Result (mm)")
        self.table.heading("date", text="Date")

        theme.make_button(self.win, "Save Experiment", self.save_click, 20, 300, width=22)
        self.reset_form()

    # لیست لیزرها و جدول را دوباره از فایل می‌خواند
    def reset_form(self):
        self.experiment_id.set("")
        self.kind.set("Single Slit")
        self.slit.set("")
        self.distance.set("")
        self.order.set("1")
        self.laser.set("")

        self.load_lasers()

        # Clear Table
        for item in self.table.get_children():
            self.table.delete(item)

        # Set All Experiments On Table
        success, experiment_list = self.controller.find_all()
        if success:
            for experiment in experiment_list:
                self.table.insert("", END, values=experiment.to_tuple())
        else:
            messagebox.showerror("Error", experiment_list)

    # لیست لیزرها را از فایل می‌خواند
    def load_lasers(self):
        success, lasers = self.controller.find_lasers()
        if success:
            names = []
            for laser in lasers:
                names.append(f"{laser.equipment_id} - {laser.name}")
            self.laser_combo["values"] = names
        else:
            messagebox.showerror("Error", lasers)

    # دکمه ذخیره فشرده شود
    def save_click(self):

        laser_id = self.laser.get().split(" - ")[0]

        success, message = self.controller.save(
            self.experiment_id.get(),
            laser_id,
            self.kind.get(),
            self.slit.get(),
            self.distance.get(),
            self.order.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)
