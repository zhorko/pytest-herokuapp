from selenium.webdriver.common.by import By

class HeroHomePage:

    def __init__(self, driver):
        self.driver = driver        
        
    def open_dropdown(self):
        # Open "Dropdown" page
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/dropdown']").click()
    
    def open_checkboxes(self):
        # Open "Dropdown" page
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/checkboxes']").click()