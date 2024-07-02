import pytest
from pages.vehicle_customization_page import VehicleCustomizationPage

def test_model_3_customization(driver):
    customization_page = VehicleCustomizationPage(driver, "model3")
    customization_page.open()
    assert "Model 3" in customization_page.get_vehicle_name()

    customization_page.select_variant("Long Range")
    assert "Long Range" in customization_page.get_selected_variant()

    customization_page.select_color("Red")
    assert "Red" in customization_page.get_selected_color()

    price = customization_page.get_total_price()
    assert price > 0
