from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains


class DemoHomePage:

    def __init__(self, driver):
        self.driver = driver        
        
    def open_elements(self, wait):
        # Open "Elements" page
        try:
            element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".category-cards div:nth-of-type(1) path"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('element', e))

        ActionChains(self.driver).move_to_element(element).click().perform()