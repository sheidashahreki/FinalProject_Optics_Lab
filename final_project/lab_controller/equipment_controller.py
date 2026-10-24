from lab_logic.equipment_bl import EquipmentBL
from lab_model.equipment import Equipment, Laser
from optics_tools.validation import Validator




class EquipmentController:
    def __init__(self):
        self.equipment_bl = EquipmentBL()

    def save(self, equipment_id, name, category, status, wavelength):
        try:
            equipment_id = Validator.to_int(equipment_id, "Equipment Id")
            if category == "Laser":
                wavelength = Validator.to_float(wavelength, "Wavelength")
                equipment = Laser(equipment_id, name, status, wavelength)
            else:
                equipment = Equipment(equipment_id, name, category, status)
            self.equipment_bl.save(equipment)
            return True, "Equipment Saved"
        except Exception as e:
            return False, f"Save Failed : {e}"

    def change_status(self, equipment_id, status):
        try:
            equipment_id = Validator.to_int(equipment_id, "Equipment Id")
            self.equipment_bl.change_status(equipment_id, status)
            return True, "Status Updated"
        except Exception as e:
            return False, f"Update Failed : {e}"

    def find_all(self):
        try:
            return True, self.equipment_bl.find_all()
        except Exception as e:
            return False, f"Load Failed : {e}"
