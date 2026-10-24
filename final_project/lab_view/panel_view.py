from tkinter import *

from lab_view import theme
from lab_view.equipment_view import EquipmentView
from lab_view.experiment_view import ExperimentView
from lab_view.calc_view import CalcView


class PanelView:
    def equipments_click(self):
        equipment_ui = EquipmentView(self.win)

    def experiments_click(self):
        experiment_ui = ExperimentView(self.win)

    def calculations_click(self):
        calc_ui = CalcView(self.win)

    def __init__(self):
        self.win = Tk()
        self.win.geometry("320x320")
        self.win.title("Optics & Laser Lab")
        theme.apply_style(self.win)

        theme.make_label(self.win, "Optics & Laser Lab", 45, 20, title=True)

        theme.make_button(self.win, "Equipment", self.equipments_click, 60, 90, width=22)
        theme.make_button(self.win, "Experiments", self.experiments_click, 60, 150, width=22)
        theme.make_button(self.win, "Calculations", self.calculations_click, 60, 210, width=22)

        self.win.mainloop()
