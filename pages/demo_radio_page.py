from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class DemoRadioPage:

    def __init__(self, driver):
        self.driver = driver        
            
    def click_radio(self, wait, radio_text):
        # Click on radio button with specified text
        match radio_text.lower():
            case "yes":
                try:
                    radio_yes = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#yesRadio"))
                    )
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('radio_yes', e))
                    return "Unable to find element"

                self.driver.execute_script("arguments[0].click();", radio_yes)
        
            case "impressive":
                try:
                    radio_impressive = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#impressiveRadio"))
                    )
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('radio_impressive', e))
                    return "Unable to find element"
                
                self.driver.execute_script("arguments[0].click();", radio_impressive)
            
            case _:
                return 1, "Wrong text for selector"
            
    def get_radio_status(self, wait, radio_text) -> bool:
        match radio_text.lower():
            case "yes":
                try:
                    radio_yes = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#yesRadio"))
                    )
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('radio_yes', e))
                    return "Unable to find element"

                return radio_yes.is_selected()
        
            case "impressive":
                try:
                    radio_impressive = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#impressiveRadio"))
                    )
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('radio_impressive', e))
                    return "Unable to find element"
                
                return radio_impressive.is_selected()
            
            case _:
                return 1, "Wrong text for selector"
