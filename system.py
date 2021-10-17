from foldersystem import FSObject, Folder
from memento import Memento, MementoReal
from caretaker import Caretaker


class System:
    def __init__(self):
        self.root_folder = Folder("C")

    def create_memento(self) -> Memento:
        return MementoReal(self.root_folder)

    def restore(self, savepoint: Memento):
        self.root_folder = savepoint.folder_system.copy()

    def change_state(self):
        self.root_folder.create_file("Crash.exe")

    def print_folder_system(self):
        self.root_folder.print_fs(0)


def main():
    system = System()
    windows_folder = system.root_folder.create_folder("Windows")
    users_folder = windows_folder.create_folder("Users")
    user_file = users_folder.create_file("Admin")
    cats_file = windows_folder.create_file("Cats.jpg")
    caretaker = Caretaker()
    n = caretaker.save(system.create_memento())
    system.print_folder_system()
    system.change_state()
    system.print_folder_system()
    system.restore(caretaker.get_save(n))
    system.print_folder_system()
    system.root_folder.create_file("crash2.exe")
    system.print_folder_system()
    system.restore(caretaker.get_save(n))
    system.print_folder_system()


if __name__ == "__main__":
    main()
