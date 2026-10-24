from lab_model.equipment import Laser
from lab_model.experiment import Experiment
from optics_tools.validation import Validator


class CalcController:
    def calculate(self, kind, wavelength, size, distance, order):
        try:
            wavelength = Validator.to_float(wavelength, "Wavelength")
            size = Validator.to_float(size, "Slit Size")
            distance = Validator.to_float(distance, "Distance")
            order = Validator.to_int(order, "Order")

            # برای محاسبه آزاد یک لیزر و آزمایش موقت می‌سازیم (ذخیره نمی‌شه)
            laser = Laser(1, "Temp", "Available", wavelength)
            experiment = Experiment(1, laser, kind, size, distance, order)

            position = experiment.position()
            extra = experiment.extra_result()
            if kind == "Single Slit":
                text = (f"Dark fringe m={order} at y = {position:.3f} mm\n"
                        f"Central maximum width = {extra:.3f} mm")
            else:
                text = (f"Bright fringe m={order} at y = {position:.3f} mm\n"
                        f"Fringe spacing = {extra:.3f} mm")
            return True, text
        except Exception as e:
            return False, f"Calculation Failed : {e}"
