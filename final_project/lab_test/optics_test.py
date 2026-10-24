from lab_model.equipment import Equipment, Laser
from lab_model.experiment import Experiment

# تست مدل
laser1 = Laser(1, "He-Ne Laser", "Available", 632.8)
lens1 = Equipment(2, "Lens f50", "Lens")
print(laser1)
print(lens1)
print(laser1.to_tuple())
print(lens1.to_tuple())
print(isinstance(laser1, Equipment))     # True (ارث‌بری)

# تست محاسبات: He-Ne ، شکاف 100 um ، پرده 2 m
single = Experiment(1, laser1, "Single Slit", 100, 2, 1)
print(single.position())          # حدود 12.656 mm
print(single.extra_result())      # حدود 25.313 mm

# شکاف دوگانه: d = 250 um ، پرده 1.5 m ، مرتبه 2
double = Experiment(2, laser1, "Double Slit", 250, 1.5, 2)
print(double.position())          # حدود 7.594 mm
print(double.extra_result())      # حدود 3.797 mm

# تست خطا
try:
    Laser(3, "Bad Laser", "Available", 5)
except ValueError as e:
    print("Error:", e)
