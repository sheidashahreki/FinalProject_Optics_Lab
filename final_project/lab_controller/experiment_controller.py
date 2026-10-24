from lab_logic.equipment_bl import EquipmentBL
from lab_logic.experiment_bl import ExperimentBL
from lab_model.equipment import Laser
from lab_model.experiment import Experiment
from optics_tools.validation import Validator


class ExperimentController:
    def __init__(self):
        self.experiment_bl = ExperimentBL()
        self.equipment_bl = EquipmentBL()

    def save(self, experiment_id, laser_id, kind, slit_um, distance_m, order):
        try:
            experiment_id = Validator.to_int(experiment_id, "Experiment Id")
            if str(laser_id).strip() == "":
                raise ValueError("Please Select A Laser (If The List Is Empty, Register A Laser In Equipment First)")
            laser_id = Validator.to_int(laser_id, "Laser")
            slit_um = Validator.to_float(slit_um, "Slit Size")
            distance_m = Validator.to_float(distance_m, "Distance")
            order = Validator.to_int(order, "Order")

            laser = self.equipment_bl.find_by_id(laser_id)
            if laser is None:
                raise ValueError("Laser Not Found")

            experiment = Experiment(experiment_id, laser, kind, slit_um, distance_m, order)
            self.experiment_bl.save(experiment)
            return True, f"Experiment Saved (Result = {experiment.result:.3f} mm)"
        except Exception as e:
            return False, f"Save Failed : {e}"

    def find_all(self):
        try:
            return True, self.experiment_bl.find_all()
        except Exception as e:
            return False, f"Load Failed : {e}"

    # فقط تجهیزاتی که لیزر هستند (برای کمبوباکس)
    def find_lasers(self):
        try:
            lasers = []
            for equipment in self.equipment_bl.find_all():
                if isinstance(equipment, Laser):
                    lasers.append(equipment)
            return True, lasers
        except Exception as e:
            return False, f"Load Failed : {e}"
