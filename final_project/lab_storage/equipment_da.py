import os
import pickle



class EquipmentDa:
    def __init__(self):
        folder = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(folder, exist_ok=True)
        self.filename = os.path.join(folder, "equipments.dat")

    def save(self, equipment):
        equipment_list = self.find_all()
        equipment_list.append(equipment)
        self.save_all(equipment_list)

    def update(self, equipment):
        equipment_list = self.find_all()
        for i in range(len(equipment_list)):
            if equipment_list[i].equipment_id == equipment.equipment_id:
                equipment_list[i] = equipment
        self.save_all(equipment_list)

    def save_all(self, equipment_list):
        file = open(self.filename, "wb")
        pickle.dump(equipment_list, file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            equipment_list = pickle.load(file)
            file.close()
            return equipment_list

    def find_by_id(self, equipment_id):
        for equipment in self.find_all():
            if equipment.equipment_id == equipment_id:
                return equipment
        return None
