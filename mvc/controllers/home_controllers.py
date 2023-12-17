from ..utils.bases.controllers import BaseController
from ..views import HomeView

home_view = HomeView()


class ReceptionController(BaseController):
    def run(self):
        # reception_view.welcome()
        # reception_view.follow_instructions()
        while True:
            choice = home_view.display_menu(home_view.home_menu)
            if choice == "1":
                return ...  # action 1

            elif choice == "2":
                return ...  # action 2

            elif choice == "3":
                return ...  # action 3
