from optics_tools.validation import Validator


class Equipment:
    def __init__(self, equipment_id, name, category, status="Available"):
        self.equipment_id = equipment_id
        self.name = name
        self.category = category
        self.status = status

    @property
    def equipment_id(self):
        return self.__equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        Validator.id_validator(equipment_id)
        self.__equipment_id = equipment_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        Validator.name_validator(name)
        self.__name = name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        Validator.category_validator(category)
        self.__category = category

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        Validator.status_validator(status)
        self.__status = status

    def __repr__(self):
        return f"Equipment({self.equipment_id}, {self.name}, {self.category}, {self.status})"

    def to_tuple(self):
        return (self.equipment_id, self.name, self.category, self.status, "-")


# لیزر یک تجهیز است که طول موج هم دارد
class Laser(Equipment):
    def __init__(self, equipment_id, name, status, wavelength):
        super().__init__(equipment_id, name, "Laser", status)
        self.wavelength = wavelength

    @property
    def wavelength(self):
        return self.__wavelength

    @wavelength.setter
    def wavelength(self, wavelength):
        Validator.wavelength_validator(wavelength)
        self.__wavelength = wavelength

    def __repr__(self):
        return f"Laser({self.equipment_id}, {self.name}, {self.status}, {self.wavelength} nm)"

    def to_tuple(self):
        return (self.equipment_id, self.name, self.category, self.status, self.wavelength)
