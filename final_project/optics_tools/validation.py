import re


class Validator:
    CATEGORIES = ["Laser", "Lens", "Mirror", "Slit", "Detector", "Screen", "Other"]
    STATUSES = ["Available", "In Use", "Broken"]
    KINDS = ["Single Slit", "Double Slit"]

    @staticmethod
    def id_validator(value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Invalid Id (Must Be A Positive Integer)")

    @staticmethod
    def name_validator(name):
        if not isinstance(name, str) or not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9 \-]{1,39}$", name):
            raise ValueError("Invalid Name")

    @staticmethod
    def category_validator(category):
        if category not in Validator.CATEGORIES:
            raise ValueError("Invalid Category")

    @staticmethod
    def status_validator(status):
        if status not in Validator.STATUSES:
            raise ValueError("Invalid Status")

    @staticmethod
    def kind_validator(kind):
        if kind not in Validator.KINDS:
            raise ValueError("Invalid Experiment Type")

    @staticmethod
    def wavelength_validator(wavelength):
        if not isinstance(wavelength, (int, float)) or not 100 <= wavelength <= 12000:
            raise ValueError("Invalid Wavelength (100 - 12000 nm)")

    @staticmethod
    def positive_validator(value, label):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Invalid {label} (Must Be More Than 0)")

    @staticmethod
    def order_validator(order):
        if not isinstance(order, int) or not 1 <= order <= 20:
            raise ValueError("Invalid Order (1 - 20)")

    #تبدیل متن فرم به عدد
    @staticmethod
    def to_int(text, label):
        try:
            return int(str(text).strip())
        except ValueError:
            raise ValueError(f"{label} Must Be An Integer")

    @staticmethod
    def to_float(text, label):
        try:
            return float(str(text).strip())
        except ValueError:
            raise ValueError(f"{label} Must Be A Number")
