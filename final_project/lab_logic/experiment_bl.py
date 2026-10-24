from lab_storage.experiment_da import ExperimentDa
from lab_model.equipment import Laser


class ExperimentBL:
    def __init__(self):
        self.experiment_da = ExperimentDa()

    def save(self, experiment):
        if not isinstance(experiment.laser, Laser):
            raise ValueError("Selected Equipment Is Not A Laser")
        if experiment.laser.status == "Broken":
            raise ValueError("This Laser Is Broken")
        for item in self.experiment_da.find_all():
            if item.experiment_id == experiment.experiment_id:
                raise ValueError("Experiment Id Already Exists")

        # محاسبه نتیجه آزمایش با طول موج لیزر انتخاب‌شده
        experiment.result = experiment.position()

        self.experiment_da.save(experiment)

    def find_all(self):
        return self.experiment_da.find_all()
