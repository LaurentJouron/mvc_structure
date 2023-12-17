from mvc.utils.bases.menu import BaseMenu

class ExitView(BaseMenu):
    def exit_program(self):
        self._space_presentation(" EXIT EPIC EVENTS ")

    def good_by(self):
        self._space_presentation("Good day and see you soon...\n")