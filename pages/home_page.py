from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    MENU_ITEMS = (By.CSS_SELECTOR, "#tds-menu-header-main a")
    VEHICLE_LINKS = (By.CSS_SELECTOR, ".tcl-homepage-hero__content a")

    def get_menu_items(self):
        menu_elements = self.find_elements(self.MENU_ITEMS)
        return [element.text for element in menu_elements]

    def get_vehicle_links(self):
        vehicle_elements = self.find_elements(self.VEHICLE_LINKS)
        return [element.text for element in vehicle_elements]
