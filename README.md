# Optics & Laser Lab Manager

My Python final project for the programming course.
It is a small desktop app (Tkinter) that manages the equipment of an optics and laser lab, saves experiments, and calculates single slit diffraction and double slit interference.

## What it can do

- **Equipment:** add lasers, lenses, slits, mirrors and other equipment, see them in a table, and change their status (Available / In Use / Broken).
- **Experiments:** choose a laser, choose Single Slit or Double Slit, enter the slit size, screen distance and order. The program calculates the result and saves it with the date.
- **Calculations:** a free calculator for the same formulas. It does not save anything.
- Data is saved in files, so it is still there when you close and open the program again.

## How to run

You need Python 3 (Tkinter comes with it).

```
python main.py
```

Run it from the main project folder (the one that has `main.py`).

## How to use

1. Open **Equipment** and add at least one laser (Type = Laser, wavelength in nm, for example `632.8`).
2. Open **Experiments**, click on the Laser box and choose your laser, then fill the other boxes and press Save.
3. Use **Calculations** if you only want a quick answer.

## Formulas

For both experiments the program first finds the angle, then the position on the screen:

```
sin(theta) = m * lambda / size
y = L * tan(theta)
```

- **Single slit:** `size` is the slit width a, and y is the position of the m-th **dark** fringe. The central maximum width is 2 times the first dark fringe.
- **Double slit:** `size` is the distance between slits d, and y is the position of the m-th **bright** fringe. The distance between two bright fringes is `lambda * L / d`.

If `m * lambda` is bigger than or equal to the slit size, that order does not exist and the program shows an error.

**Example:** He-Ne laser (632.8 nm), slit width 100 um, screen at 2 m, order 1 gives about 12.656 mm for the first dark fringe.

## Project structure

I used the layered structure that we learned in class.

```
main.py            starts the program
lab_view/          Tkinter windows
lab_controller/    error handling and creating objects
lab_logic/         business rules (duplicate id, broken laser, ...)
lab_storage/       saving and loading with pickle
lab_model/         Equipment, Laser, Experiment
optics_tools/      Validator
lab_test/          small test file
```

## Main classes

- `Equipment`
- `Laser` (inherits from `Equipment`, uses `super()`)
- `Experiment` (has the optics formulas)
- `Validator`

Other classes (DA, BL, Controller, View) are just the layers.

## Things I used

Classes and inheritance, `@property` getters and setters, `@staticmethod`, `pickle` for files, `re` for validation, `try/except`, Tkinter with `ttk.Treeview` and `ttk.Combobox`.
