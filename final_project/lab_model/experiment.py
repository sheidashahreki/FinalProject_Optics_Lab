import math
from datetime import date

from optics_tools.validation import Validator


class Experiment:
    def __init__(self, experiment_id, laser, kind, slit_um, distance_m, order):
        self.experiment_id = experiment_id
        self.laser = laser
        self.kind = kind
        self.slit_um = slit_um
        self.distance_m = distance_m
        self.order = order
        self.result = 0.0            # (mm)
        self.date = date.today()

    @property
    def experiment_id(self):
        return self.__experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        Validator.id_validator(experiment_id)
        self.__experiment_id = experiment_id

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        Validator.kind_validator(kind)
        self.__kind = kind

    @property
    def slit_um(self):
        return self.__slit_um

    @slit_um.setter
    def slit_um(self, slit_um):
        Validator.positive_validator(slit_um, "Slit Size")
        self.__slit_um = slit_um

    @property
    def distance_m(self):
        return self.__distance_m

    @distance_m.setter
    def distance_m(self, distance_m):
        Validator.positive_validator(distance_m, "Distance")
        self.__distance_m = distance_m

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        Validator.order_validator(order)
        self.__order = order

    # sin(theta) = m * lambda / size   ->   y = L * tan(theta)
    # شکاف یگانه: مکان m-امین نوار تاریک ، شکاف دوگانه: مکان m-امین نوار روشن (خروجی mm)
    def _position(self, order):
        ratio = order * self.laser.wavelength * 1e-9 / (self.slit_um * 1e-6)
        if ratio >= 1:
            raise ValueError("This Order Does Not Exist (m * wavelength >= slit size)")
        theta = math.asin(ratio)
        return self.distance_m * math.tan(theta) * 1000

    def position(self):
        return self._position(self.order)

    # شکاف یگانه: پهنای بیشینه مرکزی = 2 * مکان اولین مینیمم
    # شکاف دوگانه: فاصله دو نوار روشن متوالی = lambda * L / d
    def extra_result(self):
        if self.kind == "Single Slit":
            return 2 * self._position(1)
        return self.laser.wavelength * 1e-9 * self.distance_m / (self.slit_um * 1e-6) * 1000

    def __repr__(self):
        return f"Experiment({self.experiment_id}, {self.laser.name}, {self.kind}, {self.result:.3f} mm)"

    def to_tuple(self):
        return (self.experiment_id, self.laser.name, self.kind, self.slit_um,
                self.distance_m, self.order, round(self.result, 3), str(self.date))
