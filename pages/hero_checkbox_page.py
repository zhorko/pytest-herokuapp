from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class HeroCheckPage:

    def __init__(self, driver):
        self.driver = driver        
            
    def click_check_1(self, wait):
        # Click on first checkbox
        try:
            checkB = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#checkboxes input"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('hero_checkbox', e))

        # Check whether first checkbox is unchecked and check it
        if not checkB[0].is_selected():
            checkB[0].click()
        else:
            pass
        
        # Check whether second checkbox is checked and uncheck it
        if checkB[1].is_selected():
            checkB[1].click()
        else:
            pass