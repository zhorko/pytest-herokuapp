from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class DemoElemPage:

    def __init__(self, driver):
        self.driver = driver        

    def open_radio(self, wait):
        # Open "Radio Button" page
        try:
            radio_site = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li#item-2"))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('radio_site', e))