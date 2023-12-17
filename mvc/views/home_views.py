from ..utils.bases.menu import BaseMenu


class HomeView(BaseMenu):
    home_menu: dict = {
        "1": "...",
        "2": "...",
        "3": "...",
    }

    def display_menu(self, menu_dict):
        self._display_menu(menu_dict=menu_dict)
        return self._response_menu(menu_dict=menu_dict)
