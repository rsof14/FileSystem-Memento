from abc import abstractmethod, ABC


class FSObject(ABC):
    def __init__(self, name):
        self.name = name
        self.children = []

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child
        return None

    def copy(self):
        pass

    def print_fs(self, offset: int):
        pass

    def create_folder(self, name):
        pass

    def create_file(self, name):
        pass


class File(FSObject):
    def create_folder(self, name):
        return "Нельзя создавать объекты в файле"

    def create_file(self, name):
        return "Нельзя создавать объекты в файле"

    def print_fs(self, offset: int):
        print(f"{' ' * (2 * offset)} - {self.name}")

    def copy(self):
        return File(self.name)


class Folder(FSObject):
    def create_folder(self, name):
        new_folder = Folder(name)
        self.children.append(new_folder)
        return new_folder

    def create_file(self, name):
        new_file = File(name)
        self.children.append(new_file)
        return new_file

    def print_fs(self, offset: int):
        print(f"{' ' * (2 * offset)} - {self.name}/")
        for child in self.children:
            child.print_fs(offset + 1)

    def copy(self):
        copy_children = []
        for child in self.children:
            copy_children.append(child.copy())
        folder_copy = Folder(self.name)
        folder_copy.children = copy_children
        return folder_copy

