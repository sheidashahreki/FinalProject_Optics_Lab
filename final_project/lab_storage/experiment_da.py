import os
import pickle


class ExperimentDa:
    def __init__(self):
        folder = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(folder, exist_ok=True)
        self.filename = os.path.join(folder, "experiments.dat")

    def save(self, experiment):
        experiment_list = self.find_all()
        experiment_list.append(experiment)
        file = open(self.filename, "wb")
        pickle.dump(experiment_list, file)
        file.close()

    def find_all(self):
        if not os.path.exists(self.filename):
            return []
        else:
            file = open(self.filename, "rb")
            experiment_list = pickle.load(file)
            file.close()
            return experiment_list
