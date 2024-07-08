from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HeroDropPage:

    def __init__(self, driver):
        self.driver = driver

    def select_option(self, number: int):
        # Find dropdown
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#dropdown"))
        dropdown.select_by_index(number)

        # Return selected option
        return dropdown.first_selected_option
