from tkinter import *
from tkinter import ttk, messagebox

from lab_controller.equipment_controller import EquipmentController
from optics_tools.validation import Validator
from lab_view import theme


class EquipmentView:
    def __init__(self, parent):
        self.controller = EquipmentController()

        self.win = Toplevel(parent)
        self.win.geometry("780x400")
        self.win.title("Equipment")
        self.win.configure(bg=theme.BG)

        # EquipmentID
        theme.make_label(self.win, "Equipment Id", 20, 20)
        self.equipment_id = StringVar()
        theme.make_entry(self.win, self.equipment_id, 130, 20)

        # Name
        theme.make_label(self.win, "Name", 20, 60)
        self.name = StringVar()
        theme.make_entry(self.win, self.name, 130, 60)

        # Category
        theme.make_label(self.win, "Type", 20, 100)
        self.category = StringVar()
        theme.make_combo(self.win, self.category, Validator.CATEGORIES, 130, 100)

        # Status
        theme.make_label(self.win, "Status", 20, 140)
        self.status = StringVar()
        theme.make_combo(self.win, self.status, Validator.STATUSES, 130, 140)

        # Wavelength
        theme.make_label(self.win, "Wavelength (nm)", 20, 180)
        self.wavelength = StringVar()
        theme.make_entry(self.win, self.wavelength, 130, 180)
        theme.make_label(self.win, "(only for Laser)", 130, 205)

        # جدول
        self.table = ttk.Treeview(self.win, show="headings", height=12,
                                  columns=("id", "name", "type", "status", "wavelength"))
        self.table.place(x=300, y=20)

        self.table.column("id", width=40)
        self.table.column("name", width=150)
        self.table.column("type", width=80)
        self.table.column("status", width=80)
        self.table.column("wavelength", width=100)

        self.table.heading("id", text="Id")
        self.table.heading("name", text="Name")
        self.table.heading("type", text="Type")
        self.table.heading("status", text="Status")
        self.table.heading("wavelength", text="Wavelength (nm)")

        self.table.bind("<ButtonRelease-1>", self.table_click)

        theme.make_button(self.win, "Save", self.save_click, 20, 250)
        theme.make_button(self.win, "Update Status", self.status_click, 150, 250)
        self.reset_form()

    # فرم را ریست می‌کند جدول را خالی می‌کند تمام تجهیزات را از فایل می‌خواند
    def reset_form(self):
        self.equipment_id.set("")
        self.name.set("")
        self.category.set("Laser")
        self.status.set("Available")
        self.wavelength.set("")

        # Clear Table
        for item in self.table.get_children():
            self.table.delete(item)

        # Set All Equipment On Table
        success, equipment_list = self.controller.find_all()
        if success:
            for equipment in equipment_list:
                self.table.insert("", END, values=equipment.to_tuple())
        else:
            messagebox.showerror("Error", equipment_list)

    # دکمه ذخیره فشرده شود
    def save_click(self):
        success, message = self.controller.save(
            self.equipment_id.get(),
            self.name.get(),
            self.category.get(),
            self.status.get(),
            self.wavelength.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    # تغییر وضعیت تجهیز انتخاب‌شده در جدول
    def status_click(self):
        success, message = self.controller.change_status(
            self.equipment_id.get(),
            self.status.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    # وقتی روی جدول کلیک کنیم اطلاعات را نمایش می دهد
    def table_click(self, event):
        selected_id = self.table.focus()
        if not selected_id:
            return
        selected_equipment = self.table.item(selected_id)["values"]

        if selected_equipment:
            self.equipment_id.set(str(selected_equipment[0]))
            self.name.set(str(selected_equipment[1]))
            self.category.set(str(selected_equipment[2]))
            self.status.set(str(selected_equipment[3]))
            if selected_equipment[2] == "Laser":
                self.wavelength.set(str(selected_equipment[4]))
            else:
                self.wavelength.set("")
