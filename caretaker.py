from memento import Memento


class Caretaker:
    def __init__(self):
        self.savepoints = []

    def save(self, savepoint: Memento):
        self.savepoints.append(savepoint)
        return len(self.savepoints) - 1

    def get_save(self, n: int) -> Memento:
        return self.savepoints[n]
