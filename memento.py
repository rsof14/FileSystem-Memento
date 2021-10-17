from foldersystem import FSObject


class Memento:
    pass


class MementoReal(Memento):
    def __init__(self, folder_system: FSObject):
        self.folder_system = folder_system.copy()
