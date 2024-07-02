from .base_page import BasePage
from selenium.webdriver.common.by import By

class VehicleCustomizationPage(BasePage):
    VEHICLE_NAME = (By.CSS_SELECTOR, ".tds-text--h1")
    VARIANT_BUTTONS = (By.CSS_SELECTOR, "[data-group-id='powertrain'] button")
    COLOR_BUTTONS = (By.CSS_SELECTOR, "[data-group-id='paint'] button")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".tds-text--h2")

    def __init__(self, driver, model):
        super().__init__(driver)
        self.model = model

    def open(self):
        super().open(f"{self.model}/design")

    def get_vehicle_name(self):
        return self.get_text(self.VEHICLE_NAME)

    def select_variant(self, variant_name):
        variants = self.find_elements(self.VARIANT_BUTTONS)
        for variant in variants:
            if variant_name.lower() in variant.text.lower():
                variant.click()
                break

    def get_selected_variant(self):
        variants = self.find_elements(self.VARIANT_BUTTONS)
        return next(variant.text for variant in variants if "selected" in variant.get_attribute("class"))

    def select_color(self, color_name):
        colors = self.find_elements(self.COLOR_BUTTONS)
        for color in colors:
            if color_name.lower() in color.get_attribute("aria-label").lower():
                color.click()
                break

    def get_selected_color(self):
        colors = self.find_elements(self.COLOR_BUTTONS)
        return next(color.get_attribute("aria-label") for color in colors if "selected" in color.get_attribute("class"))

    def get_total_price(self):
        price_text = self.get_text(self.TOTAL_PRICE)
        return int(price_text.replace("$", "").replace(",", ""))
