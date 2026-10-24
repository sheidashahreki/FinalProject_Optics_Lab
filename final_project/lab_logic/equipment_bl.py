from lab_storage.equipment_da import EquipmentDa



class EquipmentBL:
    def __init__(self):
        self.equipment_da = EquipmentDa()

    def save(self, equipment):
        if self.equipment_da.find_by_id(equipment.equipment_id):
            raise ValueError("Equipment Id Already Exists")
        self.equipment_da.save(equipment)

    def change_status(self, equipment_id, status):
        equipment = self.equipment_da.find_by_id(equipment_id)
        if equipment is None:
            raise ValueError("Equipment Not Found")
        equipment.status = status
        self.equipment_da.update(equipment)

    def find_all(self):
        return self.equipment_da.find_all()

    def find_by_id(self, equipment_id):
        return self.equipment_da.find_by_id(equipment_id)
