import pytest
from pages.home_page import HomePage

def test_home_page_title(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert "Electric Cars, Solar & Clean Energy | Tesla" in home_page.get_title()

def test_menu_items(driver):
    home_page = HomePage(driver)
    home_page.open()
    menu_items = home_page.get_menu_items()
    expected_items = ["Vehicles", "Energy", "Charging", "Discover", "Shop"]
    assert all(item in menu_items for item in expected_items)

def test_vehicle_links(driver):
    home_page = HomePage(driver)
    home_page.open()
    vehicle_links = home_page.get_vehicle_links()
    expected_vehicles = ["Model S", "Model 3", "Model X", "Model Y"]
    assert all(vehicle in vehicle_links for vehicle in expected_vehicles)
